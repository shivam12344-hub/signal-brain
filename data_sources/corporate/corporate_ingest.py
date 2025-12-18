import feedparser
from datetime import datetime

CORPORATE_FEEDS = [
    "https://www.moneycontrol.com/rss/latestnews.xml",
    "https://economictimes.indiatimes.com/rssfeedsdefault.cms"
]

KEYWORDS_POSITIVE = ["appoints", "expansion", "profit", "growth", "acquires"]
KEYWORDS_NEGATIVE = ["resigns", "loss", "decline", "penalty", "fraud"]

def detect_impact(text):
    text = text.lower()
    for k in KEYWORDS_POSITIVE:
        if k in text:
            return "positive"
    for k in KEYWORDS_NEGATIVE:
        if k in text:
            return "negative"
    return "neutral"

def fetch_corporate_events():
    events = []

    for feed_url in CORPORATE_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:10]:
            headline = entry.title
            impact = detect_impact(headline)

            events.append({
                "headline": headline,
                "impact": impact,
                "time": datetime.now()
            })

    return events
