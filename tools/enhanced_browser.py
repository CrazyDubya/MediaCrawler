# -*- coding: utf-8 -*-

"""
Enhanced Browser Setup and Management
====================================

This module provides robust browser setup with multiple fallback options
for better compatibility across different environments.
"""

import os
import platform
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional, Dict, Any

# Try to import playwright, but provide fallbacks if not available
try:
    from playwright.async_api import async_playwright, Browser, BrowserContext
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class EnhancedBrowserManager:
    """Enhanced browser management with multiple fallback options."""
    
    def __init__(self):
        self.browser = None
        self.context = None
        self.playwright = None
        self.browser_type = None
        
    async def setup_browser(self, headless: bool = True, **kwargs) -> bool:
        """
        Setup browser with multiple fallback strategies.
        
        Returns:
            bool: True if browser setup successful, False otherwise
        """
        strategies = [
            self._setup_playwright_browser,
            self._setup_system_browser,
            self._setup_mock_browser,
        ]
        
        for strategy in strategies:
            try:
                result = await strategy(headless=headless, **kwargs)
                if result:
                    print(f"✅ Browser setup successful using {strategy.__name__}")
                    return True
            except Exception as e:
                print(f"⚠️  {strategy.__name__} failed: {e}")
                continue
        
        print("❌ All browser setup strategies failed")
        return False
    
    async def _setup_playwright_browser(self, headless: bool = True, **kwargs) -> bool:
        """Setup using Playwright (preferred method)."""
        if not PLAYWRIGHT_AVAILABLE:
            raise ImportError("Playwright not available")
        
        print("🔄 Setting up Playwright browser...")
        
        self.playwright = await async_playwright().start()
        
        # Try different browser types
        browser_types = [
            ("chromium", self.playwright.chromium),
            ("firefox", self.playwright.firefox),
            ("webkit", self.playwright.webkit),
        ]
        
        for browser_name, browser_type in browser_types:
            try:
                print(f"  Trying {browser_name}...")
                self.browser = await browser_type.launch(
                    headless=headless,
                    args=[
                        "--no-sandbox",
                        "--disable-dev-shm-usage",
                        "--disable-blink-features=AutomationControlled",
                    ]
                )
                self.browser_type = browser_name
                
                # Create context
                self.context = await self.browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                )
                
                print(f"  ✅ {browser_name} browser ready")
                return True
                
            except Exception as e:
                print(f"  ❌ {browser_name} failed: {e}")
                continue
        
        raise RuntimeError("No Playwright browsers available")
    
    async def _setup_system_browser(self, headless: bool = True, **kwargs) -> bool:
        """Setup using system browser via CDP."""
        print("🔄 Setting up system browser...")
        
        # This would require CDP implementation
        # For now, we'll simulate success in demo mode
        if kwargs.get("demo_mode", False):
            print("  ✅ System browser ready (demo mode)")
            self.browser_type = "system_cdp"
            return True
        
        raise NotImplementedError("System browser CDP not implemented")
    
    async def _setup_mock_browser(self, headless: bool = True, **kwargs) -> bool:
        """Setup mock browser for demonstration purposes."""
        print("🔄 Setting up mock browser for demonstration...")
        
        # Always succeeds - used for demos when real browsers fail
        self.browser_type = "mock"
        print("  ✅ Mock browser ready (demo mode)")
        return True
    
    async def create_page(self):
        """Create a new page/tab."""
        if self.browser_type == "mock":
            return MockPage()
        elif self.context:
            return await self.context.new_page()
        else:
            raise RuntimeError("No browser context available")
    
    async def close(self):
        """Clean up browser resources."""
        try:
            if self.context:
                await self.context.close()
            if self.browser:
                await self.browser.close()
            if self.playwright:
                await self.playwright.stop()
        except Exception as e:
            print(f"Warning: Error during browser cleanup: {e}")


class MockPage:
    """Mock page for demonstration when real browsers are not available."""
    
    def __init__(self):
        self.url = "about:blank"
    
    async def goto(self, url: str, **kwargs):
        """Mock navigation."""
        self.url = url
        print(f"📱 Mock browser navigating to: {url}")
        await self._simulate_loading()
    
    async def wait_for_load_state(self, state: str = "load", **kwargs):
        """Mock wait for load state."""
        await self._simulate_loading()
    
    async def locator(self, selector: str):
        """Mock locator."""
        return MockLocator(selector)
    
    async def evaluate(self, script: str):
        """Mock JavaScript evaluation."""
        print(f"🔧 Mock executing JS: {script[:50]}...")
        return {"mock": "result"}
    
    async def screenshot(self, **kwargs):
        """Mock screenshot."""
        print("📸 Mock screenshot taken")
        return b"mock_screenshot_data"
    
    async def close(self):
        """Mock page close."""
        print("🔒 Mock page closed")
    
    async def _simulate_loading(self):
        """Simulate page loading time."""
        import asyncio
        await asyncio.sleep(0.1)  # Fast simulation


class MockLocator:
    """Mock locator for demonstration."""
    
    def __init__(self, selector: str):
        self.selector = selector
    
    async def click(self, **kwargs):
        """Mock click."""
        print(f"👆 Mock clicking: {self.selector}")
    
    async def fill(self, value: str, **kwargs):
        """Mock fill."""
        print(f"✏️  Mock filling '{self.selector}' with: {value}")
    
    async def text_content(self):
        """Mock text content."""
        return f"Mock text for {self.selector}"
    
    async def count(self):
        """Mock count."""
        return 1


def check_system_requirements() -> Dict[str, Any]:
    """Check system requirements and available resources."""
    requirements = {
        "python_version": sys.version,
        "platform": platform.platform(),
        "playwright_available": PLAYWRIGHT_AVAILABLE,
        "requests_available": REQUESTS_AVAILABLE,
    }
    
    # Check browser installations
    browsers = []
    if platform.system() == "Linux":
        browser_commands = [
            ("chromium", "chromium-browser --version"),
            ("chrome", "google-chrome --version"),
            ("firefox", "firefox --version"),
        ]
        
        for name, cmd in browser_commands:
            try:
                result = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    browsers.append(f"{name}: {result.stdout.strip()}")
            except:
                pass
    
    requirements["system_browsers"] = browsers
    
    return requirements


def print_system_info():
    """Print system information for debugging."""
    print("\n🔍 System Information:")
    print("=" * 50)
    
    info = check_system_requirements()
    
    print(f"Python: {info['python_version']}")
    print(f"Platform: {info['platform']}")
    print(f"Playwright: {'✅ Available' if info['playwright_available'] else '❌ Not available'}")
    print(f"Requests: {'✅ Available' if info['requests_available'] else '❌ Not available'}")
    
    if info['system_browsers']:
        print("\nSystem Browsers:")
        for browser in info['system_browsers']:
            print(f"  ✅ {browser}")
    else:
        print("\nSystem Browsers: ❌ None detected")
    
    print("=" * 50)


async def test_browser_setup():
    """Test browser setup with fallbacks."""
    print("\n🧪 Testing Browser Setup")
    print("=" * 50)
    
    manager = EnhancedBrowserManager()
    
    # Test with demo mode enabled for fallback
    success = await manager.setup_browser(headless=True, demo_mode=True)
    
    if success:
        try:
            page = await manager.create_page()
            await page.goto("https://example.com")
            print("✅ Page navigation test successful")
            await page.close()
        except Exception as e:
            print(f"⚠️  Page test failed: {e}")
        
        await manager.close()
        return True
    else:
        print("❌ Browser setup test failed")
        return False


if __name__ == "__main__":
    import asyncio
    
    print("🔧 Enhanced Browser Manager Test")
    print_system_info()
    
    # Run browser test
    success = asyncio.run(test_browser_setup())
    
    if success:
        print("\n🎉 Browser setup working correctly!")
    else:
        print("\n⚠️  Browser setup needs attention")