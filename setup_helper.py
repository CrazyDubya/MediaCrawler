#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MediaCrawler Setup and Browser Installation Helper
=================================================

This script helps with setting up MediaCrawler and provides fallback
options for browser installation issues.

Features:
- Automatic dependency detection and installation
- Browser setup with fallbacks
- Environment validation
- Demo mode for testing without full setup
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from typing import List, Tuple, Optional

def check_python_version() -> bool:
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major == 3 and version.minor >= 9:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible. Need Python 3.9+")
        return False

def check_command_exists(command: str) -> bool:
    """Check if a command exists in the system PATH."""
    return shutil.which(command) is not None

def install_package(package: str, use_pip3: bool = False) -> bool:
    """Try to install a Python package."""
    pip_cmd = "pip3" if use_pip3 else "pip"
    
    if not check_command_exists(pip_cmd):
        print(f"❌ {pip_cmd} not found in PATH")
        return False
    
    try:
        print(f"📦 Installing {package}...")
        result = subprocess.run([pip_cmd, "install", package], 
                              capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print(f"✅ Successfully installed {package}")
            return True
        else:
            print(f"❌ Failed to install {package}: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout installing {package}")
        return False
    except Exception as e:
        print(f"❌ Error installing {package}: {e}")
        return False

def install_system_dependencies() -> bool:
    """Install system dependencies if possible."""
    system_packages = {
        "ubuntu/debian": [
            "libjpeg-dev", "zlib1g-dev", "libfreetype6-dev", 
            "liblcms2-dev", "libwebp-dev", "tcl8.6-dev", "tk8.6-dev",
            "python3-dev", "gcc", "nodejs", "npm"
        ],
        "centos/rhel": [
            "libjpeg-turbo-devel", "zlib-devel", "freetype-devel",
            "lcms2-devel", "libwebp-devel", "tcl-devel", "tk-devel",
            "python3-devel", "gcc", "nodejs", "npm"
        ]
    }
    
    # Try to detect system and install packages
    if check_command_exists("apt-get"):
        print("🐧 Detected Debian/Ubuntu system")
        try:
            for package in system_packages["ubuntu/debian"]:
                subprocess.run(["sudo", "apt-get", "install", "-y", package], 
                             capture_output=True, timeout=60)
            return True
        except:
            print("⚠️  Could not install system packages automatically")
            return False
    elif check_command_exists("yum"):
        print("🎩 Detected CentOS/RHEL system")
        try:
            for package in system_packages["centos/rhel"]:
                subprocess.run(["sudo", "yum", "install", "-y", package], 
                             capture_output=True, timeout=60)
            return True
        except:
            print("⚠️  Could not install system packages automatically")
            return False
    else:
        print("⚠️  Unknown system, skipping system package installation")
        return False

def setup_minimal_environment() -> List[str]:
    """Set up minimal environment for demo functionality."""
    essential_packages = [
        "rich",        # For beautiful terminal output
        "asyncio",     # Already in stdlib, but check
    ]
    
    optional_packages = [
        "pandas",      # For data export
        "matplotlib",  # For plotting
        "wordcloud",   # For word clouds
        "playwright",  # For browser automation
        "httpx",       # For HTTP requests
        "pydantic",    # For data validation
    ]
    
    installed = []
    failed = []
    
    print("🚀 Setting up minimal environment...")
    
    # Try essential packages first
    for package in essential_packages:
        if package == "asyncio":  # Skip asyncio as it's builtin
            continue
            
        if install_package(package) or install_package(package, use_pip3=True):
            installed.append(package)
        else:
            failed.append(package)
    
    # Try optional packages
    print("\n📦 Installing optional packages...")
    for package in optional_packages:
        if install_package(package) or install_package(package, use_pip3=True):
            installed.append(package)
        else:
            failed.append(package)
            print(f"⚠️  {package} installation failed, will use fallback")
    
    return installed, failed

def setup_playwright_browsers() -> bool:
    """Set up Playwright browsers with fallbacks."""
    try:
        print("🌐 Setting up Playwright browsers...")
        
        # Try to install playwright first
        if not install_package("playwright"):
            print("❌ Could not install Playwright")
            return False
        
        # Try to install browsers
        result = subprocess.run(["python", "-m", "playwright", "install"], 
                              capture_output=True, text=True, timeout=600)
        
        if result.returncode == 0:
            print("✅ Playwright browsers installed successfully")
            return True
        else:
            print("⚠️  Playwright browser installation had issues:")
            print(result.stderr)
            
            # Try alternative installation
            print("🔄 Trying alternative browser installation...")
            result = subprocess.run(["python", "-m", "playwright", "install", "chromium"], 
                                  capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print("✅ Chromium browser installed successfully")
                return True
            else:
                print("❌ Browser installation failed")
                return False
                
    except Exception as e:
        print(f"❌ Error setting up browsers: {e}")
        return False

def create_fallback_config() -> bool:
    """Create fallback configuration for demo mode."""
    config_content = '''# MediaCrawler Fallback Configuration
# This configuration enables demo mode without full dependencies

ENABLE_DEMO_MODE = True
USE_FALLBACK_IMPLEMENTATIONS = True
SIMULATE_BROWSER_ACTIONS = True

# Browser settings with fallbacks
BROWSER_TYPE = "chromium"  # or "firefox", "webkit"
HEADLESS = True
ENABLE_BROWSER_FALLBACK = True

# Demo settings
DEMO_OUTPUT_DIR = "demo_output"
GENERATE_SAMPLE_DATA = True
ENABLE_PERFORMANCE_METRICS = True

# Export formats
ENABLE_JSON_EXPORT = True
ENABLE_CSV_EXPORT = True
ENABLE_EXCEL_EXPORT = False  # Requires additional dependencies

print("Demo mode configuration created successfully!")
'''
    
    try:
        with open("demo_config.py", "w") as f:
            f.write(config_content)
        print("✅ Created fallback configuration: demo_config.py")
        return True
    except Exception as e:
        print(f"❌ Could not create fallback config: {e}")
        return False

def run_environment_check() -> dict:
    """Run comprehensive environment check."""
    results = {
        "python_version": check_python_version(),
        "pip_available": check_command_exists("pip") or check_command_exists("pip3"),
        "git_available": check_command_exists("git"),
        "node_available": check_command_exists("node") or check_command_exists("nodejs"),
        "npm_available": check_command_exists("npm"),
    }
    
    # Check Python packages
    required_packages = ["rich", "asyncio"]
    optional_packages = ["pandas", "playwright", "httpx", "pydantic"]
    
    results["required_packages"] = []
    results["optional_packages"] = []
    
    for package in required_packages:
        try:
            if package == "asyncio":
                import asyncio
                results["required_packages"].append(package)
            else:
                __import__(package)
                results["required_packages"].append(package)
        except ImportError:
            pass
    
    for package in optional_packages:
        try:
            __import__(package)
            results["optional_packages"].append(package)
        except ImportError:
            pass
    
    return results

def print_setup_summary(results: dict, installed: List[str], failed: List[str]):
    """Print a summary of the setup process."""
    print("\n" + "="*60)
    print("🎯 MEDIACRAWLER SETUP SUMMARY")
    print("="*60)
    
    print(f"\n✅ Python Version: {'OK' if results['python_version'] else 'NEEDS UPDATE'}")
    print(f"✅ Package Manager: {'Available' if results['pip_available'] else 'Missing'}")
    print(f"✅ Git: {'Available' if results['git_available'] else 'Missing'}")
    print(f"✅ Node.js: {'Available' if results['node_available'] else 'Missing'}")
    
    if installed:
        print(f"\n📦 INSTALLED PACKAGES ({len(installed)}):")
        for package in installed:
            print(f"   ✅ {package}")
    
    if failed:
        print(f"\n⚠️  FAILED PACKAGES ({len(failed)}):")
        for package in failed:
            print(f"   ❌ {package}")
    
    print(f"\n📊 Required Packages: {len(results['required_packages'])}/2")
    print(f"📊 Optional Packages: {len(results['optional_packages'])}/4")
    
    if len(results['required_packages']) >= 1:  # Rich is most important
        print("\n🎉 READY FOR DEMO MODE!")
        print("   You can run: python demo_standalone.py")
    else:
        print("\n⚠️  LIMITED FUNCTIONALITY")
        print("   Some packages are missing, but basic demo should work")
    
    print("\n📁 Demo files will be saved to: demo_output/")
    print("="*60)

def main():
    """Main setup function."""
    print("🚀 MediaCrawler Setup Helper")
    print("="*40)
    
    # Check environment
    print("\n1️⃣  Checking environment...")
    results = run_environment_check()
    
    if not results["python_version"]:
        print("❌ Python version incompatible. Please upgrade to Python 3.9+")
        return False
    
    # Install system dependencies
    print("\n2️⃣  Installing system dependencies...")
    install_system_dependencies()
    
    # Set up Python environment
    print("\n3️⃣  Setting up Python packages...")
    installed, failed = setup_minimal_environment()
    
    # Try browser setup
    print("\n4️⃣  Setting up browsers...")
    browser_success = setup_playwright_browsers()
    if not browser_success:
        print("⚠️  Browser setup failed, but demo mode will work with simulated data")
    
    # Create fallback config
    print("\n5️⃣  Creating fallback configuration...")
    create_fallback_config()
    
    # Final check
    print("\n6️⃣  Final environment check...")
    final_results = run_environment_check()
    
    # Print summary
    print_setup_summary(final_results, installed, failed)
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if success:
            print("\n🎉 Setup completed! Try running:")
            print("   python demo_standalone.py")
        else:
            print("\n❌ Setup had issues. Check the output above.")
    except KeyboardInterrupt:
        print("\n\n👋 Setup interrupted by user.")
    except Exception as e:
        print(f"\n❌ Setup error: {e}")