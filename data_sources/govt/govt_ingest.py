import feedparser
from datetime import datetime

PIB_FEEDS = [
    "https://pib.gov.in/RssMain.aspx?ModId=1&Lang=1",
    "https://pib.gov.in/RssMain.aspx?ModId=6&Lang=1"
]

KEYWORDS_POSITIVE = [
    "approve", "launch", "investment", "expansion",
    "policy", "scheme", "mission", "boost"
]

KEYWORDS_NEGATIVE = [
    "ban", "halt", "delay", "penalty", "withdraw", "cancel"
]

def detect_impact(text: str) -> str:
    text = text.lower()
    for k in KEYWORDS_POSITIVE:
        if k in text:
            return "positive"
    for k in KEYWORDS_NEGATIVE:
        if k in text:
            return "negative"
    return "neutral"

def fetch_govt_updates():
    updates = []

    for feed_url in PIB_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:10]:
            headline = entry.title
            summary = entry.get("summary", "")
            impact = detect_impact(headline + " " + summary)

            updates.append({
                "sector": "infrastructure",
                "headline": headline,
                "impact": impact,
                "time": datetime.now()
            })

    return updates
