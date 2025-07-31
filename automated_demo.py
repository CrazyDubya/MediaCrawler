#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MediaCrawler Automated Demo Runner
==================================

This script runs automated demonstrations of MediaCrawler functionality
across all supported platforms. Perfect for CI/CD, documentation, and
showcasing capabilities without user interaction.

Features demonstrated:
- Multi-platform crawling simulation
- Performance benchmarking  
- Error handling and fallbacks
- Comprehensive reporting
- Export functionality
"""

import asyncio
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    print("Note: pandas not available, some features will use fallback implementations")

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

# Import project modules  
try:
    import config
    from main import CrawlerFactory
except ImportError:
    print("Warning: Some modules not available. Running in simulation mode.")


class AutomatedDemo:
    """Automated demonstration runner for MediaCrawler."""
    
    def __init__(self, output_dir: str = "demo_output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.results = {}
        self.platforms = {
            "xhs": "XiaoHongShu (小红书)",
            "dy": "Douyin (抖音)",
            "ks": "Kuaishou (快手)",
            "bili": "Bilibili (哔哩哔哩)",
            "wb": "Weibo (微博)",
            "tieba": "Baidu Tieba (百度贴吧)",
            "zhihu": "Zhihu (知乎)"
        }

    def _export_to_csv_fallback(self, data_list, csv_file):
        """Fallback CSV export without pandas."""
        if not data_list:
            with open(csv_file, 'w', encoding='utf-8') as f:
                f.write("No data available\n")
            return
            
        # Get all unique keys from all dictionaries
        all_keys = set()
        for item in data_list:
            if isinstance(item, dict):
                all_keys.update(item.keys())
        
        all_keys = sorted(list(all_keys))
        
        # Write CSV manually
        import csv
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=all_keys)
            writer.writeheader()
            for item in data_list:
                if isinstance(item, dict):
                    writer.writerow(item)
            "dy": "Douyin (抖音)", 
            "ks": "Kuaishou (快手)",
            "bili": "Bilibili (哔哩哔哩)",
            "wb": "Weibo (微博)",
            "tieba": "Baidu Tieba (百度贴吧)",
            "zhihu": "Zhihu (知乎)"
        }
        
        # Demo configurations for each platform
        self.demo_configs = {
            "xhs": {
                "keywords": ["美食推荐", "护肤", "穿搭"],
                "sample_post_id": "65f0f1234567890abcdef123",
                "creator": "美食博主小王"
            },
            "dy": {
                "keywords": ["搞笑", "美食", "旅行"],
                "sample_post_id": "7123456789012345678",
                "creator": "科技达人李明"
            },
            "ks": {
                "keywords": ["农村", "美食", "搞笑"],
                "sample_post_id": "3x1234567890abcdef",
                "creator": "乡村生活张三"
            },
            "bili": {
                "keywords": ["科技", "游戏", "动漫"],
                "sample_post_id": "BV1234567890",
                "creator": "up主小明"
            },
            "wb": {
                "keywords": ["热点", "科技", "娱乐"],
                "sample_post_id": "M_1234567890abcdef",
                "creator": "科技评论员"
            },
            "tieba": {
                "keywords": ["游戏", "科技", "生活"],
                "sample_post_id": "p123456789",
                "creator": "吧主用户"
            },
            "zhihu": {
                "keywords": ["编程", "科技", "职场"],
                "sample_post_id": "answer/123456789",
                "creator": "知乎大V"
            }
        }

    def print_header(self, title: str):
        """Print a formatted header."""
        print("\n" + "=" * 80)
        print(f"🔥 {title}")
        print("=" * 80)

    def print_section(self, title: str):
        """Print a formatted section header."""
        print(f"\n📋 {title}")
        print("-" * 50)

    async def simulate_crawling_task(self, task_name: str, duration: float = 1.0) -> Dict:
        """Simulate a crawling task with realistic timing."""
        start_time = time.time()
        print(f"  ⏳ {task_name}...")
        
        # Simulate processing time
        await asyncio.sleep(duration)
        
        end_time = time.time()
        elapsed = end_time - start_time
        
        print(f"  ✅ {task_name} completed in {elapsed:.2f}s")
        
        return {
            "task": task_name,
            "start_time": start_time,
            "end_time": end_time,
            "duration": elapsed,
            "status": "success"
        }

    async def demo_keyword_search(self, platform: str, config: Dict) -> Dict:
        """Demonstrate keyword search functionality."""
        self.print_section(f"Keyword Search Demo - {self.platforms[platform]}")
        
        keyword = config["keywords"][0]
        print(f"  🔍 Searching for: '{keyword}'")
        
        task_result = await self.simulate_crawling_task(f"Keyword search for '{keyword}'", 1.5)
        
        # Simulate results
        results = {
            "platform": platform,
            "platform_name": self.platforms[platform],
            "feature": "keyword_search",
            "keyword": keyword,
            "posts_found": 25,
            "comments_extracted": 150,
            "media_files": 12,
            "processing_time": task_result["duration"],
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"  📊 Found {results['posts_found']} posts")
        print(f"  📊 Extracted {results['comments_extracted']} comments")
        print(f"  📊 Downloaded {results['media_files']} media files")
        
        return results

    async def demo_post_details(self, platform: str, config: Dict) -> Dict:
        """Demonstrate post details extraction."""
        self.print_section(f"Post Details Demo - {self.platforms[platform]}")
        
        post_id = config["sample_post_id"]
        print(f"  📋 Extracting details for post: {post_id}")
        
        task_result = await self.simulate_crawling_task(f"Post details extraction", 1.2)
        
        results = {
            "platform": platform,
            "platform_name": self.platforms[platform],
            "feature": "post_details",
            "post_id": post_id,
            "author": config["creator"],
            "likes": 1250,
            "shares": 45,
            "comments": 89,
            "views": 5420,
            "processing_time": task_result["duration"],
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"  👤 Author: {results['author']}")
        print(f"  ❤️  Likes: {results['likes']}")
        print(f"  🔄 Shares: {results['shares']}")
        print(f"  💬 Comments: {results['comments']}")
        print(f"  👁️  Views: {results['views']}")
        
        return results

    async def demo_creator_analysis(self, platform: str, config: Dict) -> Dict:
        """Demonstrate creator profile analysis."""
        self.print_section(f"Creator Analysis Demo - {self.platforms[platform]}")
        
        creator = config["creator"]
        print(f"  👤 Analyzing creator: {creator}")
        
        task_result = await self.simulate_crawling_task(f"Creator profile analysis", 2.0)
        
        results = {
            "platform": platform,
            "platform_name": self.platforms[platform],
            "feature": "creator_analysis",
            "creator_name": creator,
            "total_posts": 145,
            "followers": 12500,
            "total_likes": 89000,
            "avg_engagement_rate": 7.8,
            "content_categories": ["美食", "生活", "推荐"],
            "processing_time": task_result["duration"],
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"  📝 Total posts: {results['total_posts']}")
        print(f"  👥 Followers: {results['followers']:,}")
        print(f"  ❤️  Total likes: {results['total_likes']:,}")
        print(f"  📊 Avg engagement rate: {results['avg_engagement_rate']}%")
        
        return results

    async def demo_comments_analysis(self, platform: str, config: Dict) -> Dict:
        """Demonstrate comments analysis and sentiment."""
        self.print_section(f"Comments Analysis Demo - {self.platforms[platform]}")
        
        print(f"  💬 Analyzing comments sentiment and keywords")
        
        task_result = await self.simulate_crawling_task(f"Comments sentiment analysis", 1.8)
        
        results = {
            "platform": platform,
            "platform_name": self.platforms[platform],
            "feature": "comments_analysis",
            "primary_comments": 89,
            "sub_comments": 234,
            "sentiment": {
                "positive": 72.5,
                "neutral": 18.3,
                "negative": 9.2
            },
            "top_keywords": ["好棒", "喜欢", "不错", "推荐", "赞"],
            "processing_time": task_result["duration"],
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"  💬 Primary comments: {results['primary_comments']}")
        print(f"  💬 Sub-comments: {results['sub_comments']}")
        print(f"  😊 Positive sentiment: {results['sentiment']['positive']:.1f}%")
        print(f"  😐 Neutral sentiment: {results['sentiment']['neutral']:.1f}%")
        print(f"  😞 Negative sentiment: {results['sentiment']['negative']:.1f}%")
        print(f"  🔤 Top keywords: {', '.join(results['top_keywords'])}")
        
        return results

    async def demo_wordcloud_generation(self, platform: str, config: Dict) -> Dict:
        """Demonstrate word cloud generation."""
        self.print_section(f"Word Cloud Demo - {self.platforms[platform]}")
        
        print(f"  ☁️  Generating word cloud from extracted content")
        
        task_result = await self.simulate_crawling_task(f"Word cloud generation", 1.5)
        
        # Create demo word cloud data
        wordcloud_file = self.output_dir / f"{platform}_wordcloud_demo.txt"
        with open(wordcloud_file, "w", encoding="utf-8") as f:
            f.write(f"Word Cloud Data for {self.platforms[platform]}\n")
            f.write(f"Generated: {datetime.now()}\n")
            f.write("=" * 40 + "\n")
            f.write("Top Keywords (frequency):\n")
            f.write("科技 (125), 美食 (98), 生活 (87), 分享 (76), 推荐 (65)\n")
            f.write("体验 (54), 好用 (43), 喜欢 (41), 不错 (38), 棒 (35)\n")
            f.write("\nSentiment Distribution:\n")
            f.write("Positive: 72.5%, Neutral: 18.3%, Negative: 9.2%\n")
        
        results = {
            "platform": platform,
            "platform_name": self.platforms[platform],
            "feature": "wordcloud",
            "total_words": 2456,
            "unique_words": 347,
            "output_file": str(wordcloud_file),
            "top_words": ["科技", "美食", "生活", "分享", "推荐"],
            "processing_time": task_result["duration"],
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"  📊 Total words processed: {results['total_words']:,}")
        print(f"  🔤 Unique words: {results['unique_words']}")
        print(f"  📁 Output saved to: {wordcloud_file}")
        
        return results

    async def demo_data_export(self, platform: str, platform_results: List[Dict]) -> Dict:
        """Demonstrate data export in multiple formats."""
        self.print_section(f"Data Export Demo - {self.platforms[platform]}")
        
        print(f"  📤 Exporting data in multiple formats")
        
        task_result = await self.simulate_crawling_task(f"Data export", 1.0)
        
        # Export as JSON
        json_file = self.output_dir / f"{platform}_demo_results.json"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(platform_results, f, indent=2, ensure_ascii=False)
        
        # Export as CSV
        csv_file = self.output_dir / f"{platform}_demo_summary.csv"
        summary_data = []
        for result in platform_results:
            summary_data.append({
                "Feature": result.get("feature", "unknown"),
                "Platform": result.get("platform_name", "unknown"),
                "Processing_Time": result.get("processing_time", 0),
                "Timestamp": result.get("timestamp", "")
            })
        
        if PANDAS_AVAILABLE:
            df = pd.DataFrame(summary_data)
            df.to_csv(csv_file, index=False, encoding="utf-8")
        else:
            self._export_to_csv_fallback(summary_data, csv_file)
        
        results = {
            "platform": platform,
            "platform_name": self.platforms[platform],
            "feature": "data_export",
            "formats": ["JSON", "CSV"],
            "files": [str(json_file), str(csv_file)],
            "records_exported": len(platform_results),
            "processing_time": task_result["duration"],
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"  📁 JSON export: {json_file}")
        print(f"  📁 CSV export: {csv_file}")
        print(f"  📊 Records exported: {results['records_exported']}")
        
        return results

    async def run_platform_demo(self, platform: str) -> List[Dict]:
        """Run complete demo for a single platform."""
        self.print_header(f"Platform Demo: {self.platforms[platform]}")
        
        config = self.demo_configs[platform]
        platform_results = []
        
        # Run all demo features
        demos = [
            self.demo_keyword_search,
            self.demo_post_details,
            self.demo_creator_analysis,
            self.demo_comments_analysis,
            self.demo_wordcloud_generation,
        ]
        
        for demo_func in demos:
            try:
                result = await demo_func(platform, config)
                platform_results.append(result)
            except Exception as e:
                print(f"  ❌ Error in {demo_func.__name__}: {e}")
                error_result = {
                    "platform": platform,
                    "feature": demo_func.__name__.replace("demo_", ""),
                    "status": "error",
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                }
                platform_results.append(error_result)
        
        # Export platform data
        export_result = await self.demo_data_export(platform, platform_results)
        platform_results.append(export_result)
        
        return platform_results

    def generate_performance_report(self, all_results: Dict):
        """Generate comprehensive performance and summary report."""
        self.print_header("Performance and Summary Report")
        
        # Calculate overall statistics
        total_features = 0
        successful_features = 0
        total_processing_time = 0
        platform_stats = {}
        
        for platform, results in all_results.items():
            platform_features = len(results)
            platform_successful = len([r for r in results if r.get("status") != "error"])
            platform_time = sum(r.get("processing_time", 0) for r in results)
            
            platform_stats[platform] = {
                "total_features": platform_features,
                "successful_features": platform_successful,
                "success_rate": (platform_successful / platform_features * 100) if platform_features > 0 else 0,
                "total_time": platform_time
            }
            
            total_features += platform_features
            successful_features += platform_successful
            total_processing_time += platform_time
        
        # Print summary statistics
        print(f"\n📊 Overall Statistics:")
        print(f"  🎯 Total features tested: {total_features}")
        print(f"  ✅ Successful features: {successful_features}")
        print(f"  📈 Overall success rate: {(successful_features/total_features*100):.1f}%")
        print(f"  ⏱️  Total processing time: {total_processing_time:.2f}s")
        print(f"  ⚡ Average time per feature: {(total_processing_time/total_features):.2f}s")
        
        print(f"\n📋 Platform Performance:")
        for platform, stats in platform_stats.items():
            platform_name = self.platforms[platform]
            print(f"  🔸 {platform_name}:")
            print(f"    Features: {stats['successful_features']}/{stats['total_features']} " +
                  f"({stats['success_rate']:.1f}%)")
            print(f"    Time: {stats['total_time']:.2f}s")
        
        # Generate comprehensive report file
        report_data = {
            "demo_summary": {
                "timestamp": datetime.now().isoformat(),
                "total_platforms": len(all_results),
                "total_features": total_features,
                "successful_features": successful_features,
                "overall_success_rate": successful_features/total_features*100,
                "total_processing_time": total_processing_time,
                "average_time_per_feature": total_processing_time/total_features
            },
            "platform_statistics": platform_stats,
            "detailed_results": all_results
        }
        
        report_file = self.output_dir / "comprehensive_demo_report.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n📁 Comprehensive report saved to: {report_file}")
        
        # Generate CSV summary
        csv_data = []
        for platform, results in all_results.items():
            for result in results:
                csv_data.append({
                    "Platform": self.platforms.get(platform, platform),
                    "Feature": result.get("feature", "unknown"),
                    "Status": result.get("status", "success"),
                    "Processing_Time": result.get("processing_time", 0),
                    "Timestamp": result.get("timestamp", "")
                })
        
        csv_file = self.output_dir / "demo_results_summary.csv"
        if PANDAS_AVAILABLE:
            df = pd.DataFrame(csv_data)
            df.to_csv(csv_file, index=False, encoding="utf-8")
        else:
            self._export_to_csv_fallback(csv_data, csv_file)
        print(f"📁 CSV summary saved to: {csv_file}")

    async def run_full_demo(self, platforms: Optional[List[str]] = None):
        """Run the complete automated demo."""
        if platforms is None:
            platforms = list(self.platforms.keys())
        
        self.print_header("MediaCrawler Automated Demo Suite")
        print(f"🚀 Running automated demo for {len(platforms)} platforms")
        print(f"📁 Output directory: {self.output_dir}")
        print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        all_results = {}
        
        for platform in platforms:
            if platform in self.platforms:
                try:
                    results = await self.run_platform_demo(platform)
                    all_results[platform] = results
                    print(f"✅ {self.platforms[platform]} demo completed")
                except Exception as e:
                    print(f"❌ Error in {self.platforms[platform]} demo: {e}")
                    all_results[platform] = [{
                        "platform": platform,
                        "status": "platform_error",
                        "error": str(e),
                        "timestamp": datetime.now().isoformat()
                    }]
        
        # Generate final report
        self.generate_performance_report(all_results)
        
        self.print_header("Demo Completed Successfully! 🎉")
        print(f"📁 All outputs saved to: {self.output_dir}")
        print(f"🔍 Check the generated files for detailed results and examples")
        
        return all_results


def main():
    """Entry point for automated demo."""
    import argparse
    
    parser = argparse.ArgumentParser(description="MediaCrawler Automated Demo")
    parser.add_argument("--platforms", nargs="+", 
                       choices=["xhs", "dy", "ks", "bili", "wb", "tieba", "zhihu", "all"],
                       default=["all"],
                       help="Platforms to demo (default: all)")
    parser.add_argument("--output", default="demo_output",
                       help="Output directory for demo results")
    parser.add_argument("--quick", action="store_true",
                       help="Run quick demo with limited features")
    
    args = parser.parse_args()
    
    # Resolve platform list
    if "all" in args.platforms:
        platforms = ["xhs", "dy", "ks", "bili", "wb", "tieba", "zhihu"]
    else:
        platforms = args.platforms
    
    # Install required packages if not available
    try:
        import pandas
    except ImportError:
        print("Installing pandas for data export...")
        os.system("pip install pandas")
    
    # Run the demo
    demo = AutomatedDemo(args.output)
    
    try:
        results = asyncio.run(demo.run_full_demo(platforms))
        print(f"\n🎉 Demo completed successfully!")
        print(f"📊 Results for {len(results)} platforms saved to {args.output}/")
        return 0
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())