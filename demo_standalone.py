#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MediaCrawler Standalone Demo
===========================

This standalone demo showcases the MediaCrawler interface and functionality
without requiring the full dependency stack. Perfect for demonstrations
and getting started quickly.

Features demonstrated:
- Interactive menu system
- Platform selection and configuration
- Simulated data collection and export
- Performance analytics visualization
- Fallback implementations for all features

For educational and research purposes only.
"""

import asyncio
import json
import os
import sys
import time
import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    print("Note: pandas not available, using fallback implementations")

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.layout import Layout
from rich.live import Live


class StandaloneMediaCrawlerDemo:
    """Standalone demo for MediaCrawler functionality."""
    
    def __init__(self):
        self.console = Console()
        self.platforms = {
            "1": ("xhs", "XiaoHongShu (小红书)", "Popular lifestyle and shopping platform"),
            "2": ("dy", "Douyin (抖音)", "Short video platform"),
            "3": ("ks", "Kuaishou (快手)", "Short video and live streaming"),
            "4": ("bili", "Bilibili (哔哩哔哩)", "Video sharing and community"),
            "5": ("wb", "Weibo (微博)", "Social media microblogging"),
            "6": ("tieba", "Baidu Tieba (百度贴吧)", "Online forums and communities"),
            "7": ("zhihu", "Zhihu (知乎)", "Q&A knowledge sharing platform")
        }
        self.demo_results = {}
        self.output_dir = Path("demo_output")
        self.output_dir.mkdir(exist_ok=True)

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
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=all_keys)
            writer.writeheader()
            for item in data_list:
                if isinstance(item, dict):
                    writer.writerow(item)

    def display_welcome(self):
        """Display welcome screen with project information."""
        welcome_text = Text()
        welcome_text.append("🔥 MediaCrawler Interactive Demo 🕷️\n\n", style="bold red")
        welcome_text.append("A comprehensive social media data collection tool supporting:\n", style="cyan")
        welcome_text.append("• Multi-platform crawling across 7+ major platforms\n", style="green")
        welcome_text.append("• Advanced search and filtering capabilities\n", style="green")
        welcome_text.append("• Creator profile and content analysis\n", style="green")
        welcome_text.append("• Comments and engagement extraction\n", style="green")
        welcome_text.append("• Data export in multiple formats\n", style="green")
        welcome_text.append("• Word cloud and analytics generation\n", style="green")
        welcome_text.append("\n⚠️  Educational and Research Use Only ⚠️", style="bold yellow")
        welcome_text.append("\n📝 Note: This is a demonstration mode with simulated data", style="italic blue")
        
        panel = Panel(
            welcome_text,
            title="Welcome to MediaCrawler Demo",
            border_style="blue",
            expand=False
        )
        self.console.print(panel)
        self.console.print()

    def display_platforms(self):
        """Display available platforms in a table."""
        table = Table(title="🌐 Supported Platforms", show_header=True, header_style="bold magenta")
        table.add_column("Option", style="cyan", width=8)
        table.add_column("Platform", style="green", width=25)
        table.add_column("Description", style="yellow")
        
        for key, (code, name, desc) in self.platforms.items():
            table.add_row(key, name, desc)
        
        table.add_row("8", "All Platforms", "Run demo on all platforms (limited data)")
        table.add_row("9", "Performance Test", "Benchmark performance across platforms")
        table.add_row("0", "Exit", "Exit the demo")
        
        self.console.print(table)
        self.console.print()

    def generate_sample_data(self, platform_code: str, search_term: str = "demo") -> Dict:
        """Generate realistic sample data for demonstration."""
        import random
        
        # Sample post data
        posts = []
        for i in range(random.randint(5, 15)):
            post = {
                "id": f"{platform_code}_{i+1:03d}",
                "title": f"Sample {search_term} post #{i+1}",
                "content": f"This is a sample post about {search_term}. Content varies by platform.",
                "author": f"user_{random.randint(1000, 9999)}",
                "likes": random.randint(10, 10000),
                "comments": random.randint(0, 500),
                "shares": random.randint(0, 100),
                "timestamp": datetime.now().isoformat(),
                "url": f"https://{platform_code}.example.com/post/{i+1}"
            }
            posts.append(post)
        
        # Sample analytics
        analytics = {
            "total_posts": len(posts),
            "avg_engagement": sum(p["likes"] + p["comments"] + p["shares"] for p in posts) / len(posts),
            "top_keywords": [search_term, "content", "social", "media", "demo"],
            "processing_time": random.uniform(1.2, 4.8),
            "success_rate": random.uniform(0.85, 0.98)
        }
        
        return {
            "platform": platform_code,
            "search_term": search_term,
            "posts": posts,
            "analytics": analytics,
            "timestamp": datetime.now().isoformat()
        }

    async def simulate_crawling(self, platform_code: str, platform_name: str, search_term: str):
        """Simulate the crawling process with realistic timing and progress."""
        demo_dir = self.output_dir
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            console=self.console
        ) as progress:
            
            # Initialize crawler task
            task = progress.add_task(f"🚀 Initializing {platform_name} crawler...", total=100)
            await asyncio.sleep(0.8)
            progress.update(task, advance=20)
            
            # Search task
            progress.update(task, description=f"🔍 Searching for '{search_term}'...")
            await asyncio.sleep(1.2)
            progress.update(task, advance=30)
            
            # Data extraction
            progress.update(task, description="📊 Extracting post data...")
            await asyncio.sleep(1.5)
            progress.update(task, advance=25)
            
            # Analytics
            progress.update(task, description="📈 Generating analytics...")
            await asyncio.sleep(1.0)
            progress.update(task, advance=15)
            
            # Export
            progress.update(task, description="💾 Exporting data...")
            demo_data = self.generate_sample_data(platform_code, search_term)
            
            # Save JSON
            json_file = demo_dir / f"{platform_code}_demo_results.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(demo_data, f, indent=2, ensure_ascii=False)
            
            # Save CSV
            csv_file = demo_dir / f"{platform_code}_demo_summary.csv"
            if PANDAS_AVAILABLE:
                df = pd.DataFrame(demo_data["posts"])
                df.to_csv(csv_file, index=False, encoding="utf-8")
            else:
                self._export_to_csv_fallback(demo_data["posts"], csv_file)
            
            # Generate word cloud data
            wordcloud_file = demo_dir / f"{platform_code}_wordcloud_demo.txt"
            with open(wordcloud_file, 'w', encoding='utf-8') as f:
                f.write(f"Keywords for {platform_name}:\n")
                f.write(f"Search term: {search_term}\n")
                f.write("Top keywords: " + ", ".join(demo_data["analytics"]["top_keywords"]))
            
            await asyncio.sleep(0.5)
            progress.update(task, advance=10)
            
        # Store results
        self.demo_results[platform_code] = demo_data
        
        # Display results summary
        self.display_results_summary(platform_name, demo_data)
        
        self.console.print(f"✅ [green]Demo completed successfully for {platform_name}![/green]")
        self.console.print(f"📁 Results saved to: {demo_dir}")
        self.console.print(f"   • JSON: {json_file}")
        self.console.print(f"   • CSV: {csv_file}")
        self.console.print(f"   • Word Cloud: {wordcloud_file}")
        self.console.print()

    def display_results_summary(self, platform_name: str, data: Dict):
        """Display a summary of the crawling results."""
        analytics = data["analytics"]
        
        table = Table(title=f"📊 Results Summary - {platform_name}", show_header=True, header_style="bold cyan")
        table.add_column("Metric", style="yellow", width=20)
        table.add_column("Value", style="green", width=30)
        
        table.add_row("Total Posts", str(analytics["total_posts"]))
        table.add_row("Avg Engagement", f"{analytics['avg_engagement']:.1f}")
        table.add_row("Processing Time", f"{analytics['processing_time']:.2f}s")
        table.add_row("Success Rate", f"{analytics['success_rate']:.1%}")
        table.add_row("Top Keywords", ", ".join(analytics["top_keywords"][:3]))
        
        self.console.print(table)
        self.console.print()

    async def run_all_platforms_demo(self):
        """Run a quick demo across all platforms."""
        self.console.print("[bold cyan]🚀 Running quick demo across all platforms...[/bold cyan]\n")
        
        all_results = {}
        
        for key, (code, name, desc) in self.platforms.items():
            self.console.print(f"[bold yellow]Running demo for {name}...[/bold yellow]")
            
            # Quick simulated crawl
            demo_data = self.generate_sample_data(code, "trending")
            all_results[code] = demo_data
            
            # Save individual results
            json_file = self.output_dir / f"{code}_demo_results.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(demo_data, f, indent=2, ensure_ascii=False)
            
            self.console.print(f"✅ [green]{name} demo completed[/green]")
            await asyncio.sleep(0.5)
        
        # Generate comprehensive summary
        self.generate_comprehensive_summary(all_results)
        
        self.console.print("\n[bold green]🎉 All platforms demo completed successfully![/bold green]")

    def generate_comprehensive_summary(self, all_results: Dict):
        """Generate a comprehensive summary report."""
        summary_data = []
        
        for platform_code, data in all_results.items():
            platform_name = next(name for code, name, desc in self.platforms.values() if code == platform_code)
            analytics = data["analytics"]
            
            summary_data.append({
                "Platform": platform_name,
                "Platform_Code": platform_code,
                "Posts_Found": analytics["total_posts"],
                "Avg_Engagement": round(analytics["avg_engagement"], 2),
                "Processing_Time": round(analytics["processing_time"], 2),
                "Success_Rate": round(analytics["success_rate"], 3),
                "Timestamp": data["timestamp"]
            })
        
        # Save comprehensive report
        report_file = self.output_dir / "comprehensive_demo_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump({
                "summary": summary_data,
                "total_platforms": len(all_results),
                "generated_at": datetime.now().isoformat(),
                "demo_version": "1.0.0"
            }, f, indent=2, ensure_ascii=False)
        
        # Save CSV summary
        csv_file = self.output_dir / "demo_results_summary.csv"
        if PANDAS_AVAILABLE:
            df = pd.DataFrame(summary_data)
            df.to_csv(csv_file, index=False, encoding="utf-8")
        else:
            self._export_to_csv_fallback(summary_data, csv_file)
        
        self.console.print(f"📁 Comprehensive report saved to: {report_file}")
        self.console.print(f"📁 CSV summary saved to: {csv_file}")

    async def run_performance_test(self):
        """Run a performance benchmarking test."""
        self.console.print("[bold cyan]🏁 Running performance benchmark...[/bold cyan]\n")
        
        performance_data = {}
        
        for key, (code, name, desc) in self.platforms.items():
            self.console.print(f"Testing {name}...")
            
            start_time = time.time()
            
            # Simulate variable performance
            import random
            processing_time = random.uniform(0.5, 3.0)
            await asyncio.sleep(processing_time)
            
            end_time = time.time()
            actual_time = end_time - start_time
            
            performance_data[code] = {
                "platform": name,
                "processing_time": actual_time,
                "simulated_posts": random.randint(10, 100),
                "throughput": random.randint(10, 100) / actual_time
            }
            
            self.console.print(f"  ⏱️  {actual_time:.2f}s | {performance_data[code]['throughput']:.1f} posts/sec")
        
        # Display performance summary
        self.display_performance_summary(performance_data)

    def display_performance_summary(self, performance_data: Dict):
        """Display performance benchmark results."""
        table = Table(title="🏁 Performance Benchmark Results", show_header=True, header_style="bold magenta")
        table.add_column("Platform", style="cyan", width=20)
        table.add_column("Time (s)", style="yellow", width=12)
        table.add_column("Posts", style="green", width=8)
        table.add_column("Throughput", style="blue", width=15)
        
        for data in performance_data.values():
            table.add_row(
                data["platform"],
                f"{data['processing_time']:.2f}",
                str(data["simulated_posts"]),
                f"{data['throughput']:.1f} posts/s"
            )
        
        self.console.print(table)
        self.console.print()

    async def run_demo(self):
        """Main demo loop."""
        self.display_welcome()
        
        while True:
            self.display_platforms()
            
            choice = Prompt.ask(
                "Select a platform to demo",
                choices=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                default="8"
            )
            
            if choice == "0":
                self.console.print("[bold yellow]👋 Thanks for trying MediaCrawler! Goodbye![/bold yellow]")
                break
            elif choice == "8":
                await self.run_all_platforms_demo()
            elif choice == "9":
                await self.run_performance_test()
            else:
                platform_code, platform_name, platform_desc = self.platforms[choice]
                
                self.console.print(f"\n[bold green]🎯 Selected: {platform_name}[/bold green]")
                self.console.print(f"📝 {platform_desc}\n")
                
                search_term = Prompt.ask(
                    "Enter search term for demo",
                    default="technology"
                )
                
                await self.simulate_crawling(platform_code, platform_name, search_term)
            
            if not Confirm.ask("\n🔄 Would you like to try another demo?", default=True):
                self.console.print("[bold yellow]👋 Thanks for trying MediaCrawler! Goodbye![/bold yellow]")
                break


async def main():
    """Main entry point for the standalone demo."""
    demo = StandaloneMediaCrawlerDemo()
    await demo.run_demo()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error running demo: {e}")
        print("This is a demonstration version. For full functionality, please install all dependencies.")