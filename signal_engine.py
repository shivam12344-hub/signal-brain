def generate_signal(news):
    impact = news.get("impact", "neutral")
    sector = news.get("sector", "general")

    if impact == "positive":
        bias = "BULLISH"
        strength = 70
    elif impact == "negative":
        bias = "BEARISH"
        strength = 65
    else:
        bias = "NEUTRAL"
        strength = 50

    return {
        "sector": sector,
        "headline": news.get("headline"),
        "bias": bias,
        "strength": strength
    }
