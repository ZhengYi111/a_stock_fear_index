import feedparser
import pandas as pd
from datetime import datetime

def get_36kr_rss_news():
    """通过RSS获取36氪最新新闻"""
    rss_urls = [
        "https://rss.36kr.com/news/",           # 快讯
        "https://rss.36kr.com/news/flash",      # 实时快讯
        "https://rss.36kr.com/news/tech",       # 科技新闻
        "https://rss.36kr.com/news/finance"     # 金融新闻
    ]
    
    all_articles = []
    
    for url in rss_urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                article = {
                    'title': entry.title,
                    'link': entry.link,
                    'published': entry.published,
                    'summary': entry.summary,
                    'source': '36kr',
                    'category': url.split('/')[-1]  # 分类
                }
                all_articles.append(article)
                
            print(f"✅ 成功获取36氪 {len(feed.entries)} 条新闻")
        except Exception as e:
            print(f"❌ 获取36氪RSS失败: {e}")
    
    return pd.DataFrame(all_articles)