# MediaCrawler - Enhanced Edition 🔥🕷️

**A powerful multi-platform social media data collection tool with comprehensive demo suite**

## 🌟 What's New in This Enhanced Edition

## 🌟 What's New in This Enhanced Edition

### ✨ Major Improvements Added

#### 🎯 **Comprehensive Demo Suite**
- **Interactive Demo (`demo_standalone.py`)** - Standalone demo with simulated data that works without full dependency installation
- **Enhanced Original Demo (`demo.py`)** - Improved with fallback support and better error handling
- **Automated Demo (`automated_demo.py`)** - Perfect for CI/CD pipelines and automated testing
- **Setup Helper (`setup_helper.py`)** - Automated environment setup with intelligent fallbacks

#### 🛠️ **Dependency Resilience & Browser Fixes**
- **Smart Fallbacks** - Works even when pandas, matplotlib, or Playwright fail to install
- **Network Resilience** - Continues functioning during PyPI network timeouts
- **Browser Installation Fixes** - Multiple fallback methods for Playwright browser setup
- **Cross-platform Support** - Enhanced compatibility across Linux distributions

#### 🎨 **Enhanced User Experience**
- **Rich Terminal Interface** - Beautiful colors, progress bars, tables, and panels
- **Real-time Progress Tracking** - Live updates during data collection simulation
- **Interactive Menu System** - Intuitive navigation with helpful descriptions
- **Performance Benchmarking** - Built-in speed and efficiency testing across platforms

#### 📊 **Advanced Analytics & Export**
- **Multiple Export Formats** - JSON, CSV with custom fallback implementations
- **Comprehensive Reporting** - Cross-platform analytics and performance summaries
- **Word Cloud Generation** - Visual content analysis with sample data
- **Performance Metrics** - Processing time, throughput, and success rate tracking

#### 🌍 **Complete English Documentation**
- **DEMO_GUIDE.md** - Comprehensive guide for all demo modes and features
- **Enhanced README** - Complete English documentation with examples
- **Troubleshooting Guide** - Solutions for common setup and runtime issues
- **Usage Examples** - Real-world scenarios and best practices

### 🚀 **Key Benefits**

✅ **Instant Setup** - Demo works immediately, even without full dependencies  
✅ **Network Resilient** - Functions during internet connectivity issues  
✅ **Cross-platform** - Works on Ubuntu, CentOS, Windows, macOS  
✅ **Educational Focus** - Perfect for learning and demonstration purposes  
✅ **Professional UI** - Rich terminal interface rivals modern CLI tools  
✅ **Comprehensive Testing** - Built-in validation and performance benchmarking  

### ✨ Key Enhancements
- **🎯 Interactive Demo Suite** - Two comprehensive demo modes (interactive & automated)
- **🌍 English Documentation** - Complete English translation and documentation  
- **⚡ Performance Optimizations** - Improved error handling and fallback mechanisms
- **📊 Analytics Dashboard** - Real-time performance metrics and reporting
- **🔧 Better Setup Experience** - Automated dependency installation and browser fallbacks
- **📁 Multiple Export Formats** - JSON, CSV, SQLite, Excel support with examples
- **🎨 Rich UI Experience** - Beautiful terminal interface with progress indicators

### 🚀 Demo Features
- **Interactive Demo (`demo.py`)** - User-friendly menu-driven demonstration
- **Automated Demo (`automated_demo.py`)** - CI/CD ready automated showcase
- **Performance Analytics** - Comprehensive metrics and reporting
- **Multi-format Export** - Real examples in JSON, CSV, and more
- **Word Cloud Generation** - Visual content analysis demonstrations

## 📋 Supported Platforms

| Platform | Keyword Search | Post Details | Creator Profile | Comments | Login Cache | IP Proxy | Word Cloud |
|----------|----------------|--------------|-----------------|----------|-------------|----------|------------|
| 小红书 (XiaoHongShu) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 抖音 (Douyin) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 快手 (Kuaishou) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 哔哩哔哩 (Bilibili) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 微博 (Weibo) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 百度贴吧 (Tieba) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 知乎 (Zhihu) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## 🎯 Quick Demo & Testing

### 🚀 Instant Demo (Recommended)
Experience MediaCrawler functionality immediately with our standalone demo:

```bash
# Step 1: Run setup helper (handles dependencies and fallbacks)
python setup_helper.py

# Step 2: Launch interactive demo
python demo_standalone.py
```

**Features showcased:**
- ✨ All 7+ platforms in one interactive session
- 📊 Real-time performance benchmarking  
- 💾 Multiple export formats (JSON, CSV)
- 🎨 Beautiful terminal interface with progress tracking
- 🔄 Fallback support when dependencies are missing

### 🏃‍♂️ Quick Start Options

| Demo Type | Command | Best For |
|-----------|---------|----------|
| **Standalone** | `python demo_standalone.py` | First-time users, testing |
| **Interactive** | `python demo.py` | Full crawler integration |
| **Automated** | `python automated_demo.py` | CI/CD, batch processing |
| **Performance** | `python demo_standalone.py` → Option 9 | Benchmarking |

### 🛠️ Setup & Installation

#### Option 1: Automated Setup (Recommended)
```bash
# Clone repository
git clone https://github.com/CrazyDubya/MediaCrawler.git
cd MediaCrawler

# Run automated setup with fallbacks
python setup_helper.py

# Start demo immediately
python demo_standalone.py
```

#### Option 2: Manual Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Install browsers (may require additional setup)
python -m playwright install

# Run full demo
python demo.py
```

#### Option 3: Minimal Setup (Works even with network issues)
```bash
# Install only essential packages
pip install rich

# Run resilient demo
python demo_standalone.py
```

### 📱 Demo Features

### Prerequisites
- **Python 3.9+** - [Download Python](https://python.org/downloads/)
- **Node.js 16+** - [Download Node.js](https://nodejs.org/) (for some platforms)

### Installation

```bash
# Clone the repository
git clone https://github.com/CrazyDubya/MediaCrawler.git
cd MediaCrawler

# Install dependencies
pip install -r requirements.txt

# Install browser drivers (optional - fallbacks available)
python -m playwright install
```

### Try the Demo First! 🎉

#### Interactive Demo
```bash
# Launch interactive demo with beautiful UI
python demo.py
```

#### Automated Demo (Great for CI/CD)
```bash
# Run automated demo for all platforms
python automated_demo.py

# Run demo for specific platforms
python automated_demo.py --platforms xhs dy bili

# Quick demo (limited features)
python automated_demo.py --quick

# Custom output directory
python automated_demo.py --output my_demo_results
```

### Production Usage

```bash
# Basic keyword search
python main.py --platform xhs --lt qrcode --type search

# Extract specific post details
python main.py --platform xhs --lt qrcode --type detail

# Analyze creator profile
python main.py --platform xhs --lt qrcode --type creator

# Export to different formats
python main.py --platform xhs --lt qrcode --type search --save_data_option sqlite
```

## 🎯 Demo Features Showcase

### 1. **Keyword Search Demo**
- Search content across all platforms
- Extract posts, comments, and media
- Real-time progress tracking
- Performance metrics

### 2. **Post Details Extraction**
- Detailed post metadata
- Author information
- Engagement metrics (likes, shares, views)
- Comments and sub-comments

### 3. **Creator Profile Analysis**
- Complete profile data
- Content statistics
- Engagement rate analysis
- Historical performance

### 4. **Comments Analysis & Sentiment**
- Primary and sub-comments extraction
- Sentiment analysis (positive/neutral/negative)
- Keyword frequency analysis
- Trending topics identification

### 5. **Word Cloud Generation**
- Visual content analysis
- Chinese text processing with jieba
- Custom word filtering
- Multiple output formats

### 6. **Data Export & Analytics**
- JSON, CSV, SQLite, Excel exports
- Performance analytics dashboard
- Comprehensive reporting
- Automated summaries

## 📊 Demo Output Examples

After running the demo, you'll find generated examples in `demo_output/`:

```
demo_output/
├── comprehensive_demo_report.json    # Complete analytics report
├── demo_results_summary.csv          # Summary in CSV format
├── xhs_demo_results.json            # XiaoHongShu results
├── dy_demo_results.json             # Douyin results
├── bili_wordcloud_demo.txt          # Word cloud data
└── platform_summaries.csv          # Performance comparison
```

### Sample JSON Output
```json
{
  "platform": "xhs",
  "platform_name": "XiaoHongShu (小红书)",
  "feature": "keyword_search",
  "keyword": "美食推荐",
  "posts_found": 25,
  "comments_extracted": 150,
  "media_files": 12,
  "processing_time": 1.50,
  "timestamp": "2025-07-31T04:45:16.344133"
}
```

## 🔧 Configuration Options

### Platform Selection
```python
# Available platforms
PLATFORMS = {
    "xhs": "XiaoHongShu (小红书)",
    "dy": "Douyin (抖音)",
    "ks": "Kuaishou (快手)",
    "bili": "Bilibili (哔哩哔哩)",
    "wb": "Weibo (微博)",
    "tieba": "Baidu Tieba (百度贴吧)",
    "zhihu": "Zhihu (知乎)"
}
```

### Login Types
- **qrcode** - QR code scanning (recommended)
- **phone** - Phone number + SMS verification
- **cookie** - Direct cookie authentication

### Data Export Options
- **json** - JSON format (default)
- **csv** - CSV spreadsheet
- **sqlite** - SQLite database
- **db** - MySQL database

### Advanced Features
- **IP Proxy Support** - Built-in proxy rotation
- **Headless Mode** - Background operation
- **Comment Extraction** - Multi-level comment support
- **Media Download** - Image and video extraction
- **Word Cloud** - Visual content analysis

## 📈 Performance Metrics

The enhanced demo provides comprehensive analytics:

- **Success Rates** - Per-platform and overall success tracking
- **Processing Times** - Feature-by-feature performance
- **Data Volume** - Posts, comments, media extraction counts
- **Error Handling** - Graceful degradation and recovery
- **Resource Usage** - Memory and network optimization

## 🛡️ Legal Compliance & Ethics

**⚠️ IMPORTANT: Educational and Research Use Only**

This tool is designed for:
- **Educational purposes** - Learning web scraping and data analysis
- **Research projects** - Academic and legitimate research
- **Personal learning** - Understanding social media data structures

**Please ensure you:**
- Respect platform Terms of Service
- Follow robots.txt guidelines  
- Implement reasonable rate limiting
- Comply with local data protection laws
- Use data responsibly and ethically

## 🔍 Troubleshooting

### Browser Installation Issues
```bash
# If playwright installation fails, use system browser
export PLAYWRIGHT_BROWSERS_PATH=0
python main.py --platform xhs --lt qrcode --type search
```

### Dependency Issues
```bash
# Install missing packages
pip install rich pandas matplotlib wordcloud

# For CJK text processing
pip install jieba
```

### Performance Optimization
```bash
# Increase concurrency (use carefully)
python main.py --platform xhs --max_concurrency 3

# Reduce data volume for testing
python main.py --platform xhs --max_notes 10
```

## 🤝 Contributing

We welcome contributions! Areas for improvement:

- **Additional Platforms** - Support for more social media sites
- **Enhanced Analytics** - More sophisticated data analysis
- **UI Improvements** - Better visualization and reporting
- **Performance** - Optimization and caching improvements
- **Documentation** - More examples and use cases

## 📚 Additional Resources

- **Original Documentation** - See `README.md` for detailed Chinese documentation
- **API Reference** - Check individual module documentation
- **Examples** - Browse `demo_output/` for real examples
- **Configuration** - Review `config/base_config.py` for all options

## 📞 Support

- **Issues** - Report bugs via GitHub Issues
- **Discussions** - Join community discussions
- **Documentation** - Check the comprehensive docs
- **Examples** - Run the demo for practical examples

---

## 🎉 Try It Now!

Get started in 30 seconds:

```bash
# Clone and enter directory
git clone https://github.com/CrazyDubya/MediaCrawler.git && cd MediaCrawler

# Install dependencies
pip install -r requirements.txt

# Run the interactive demo
python demo.py

# Or run automated demo
python automated_demo.py --platforms xhs dy
```

**Enjoy exploring the power of MediaCrawler!** 🚀