# MediaCrawler Fallback Configuration
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
