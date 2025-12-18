"""
news_ingest.py
Responsible for collecting raw news signals from external sources
"""

import datetime

def fetch_news():
    """
    Later this will fetch from APIs, RSS, govt sites, filings, etc.
    For now we simulate incoming news.
    """
    now = datetime.datetime.now()

    news = [
        {
            "source": "simulation",
            "headline": "Government announces new infra push",
            "impact": "positive",
            "sector": "infrastructure",
            "time": now
        },
        {
            "source": "simulation",
            "headline": "Global crude prices spike sharply",
            "impact": "negative",
            "sector": "energy",
            "time": now
        }
    ]

    return news


if __name__ == "__main__":
    data = fetch_news()
    for item in data:
        print(item)
