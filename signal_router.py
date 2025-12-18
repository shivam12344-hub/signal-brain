from datetime import datetime

# Weight configuration (tune later)
WEIGHTS = {
    "govt": 0.30,
    "tender": 0.35,
    "corporate": 0.25,
    "market": 0.10
}


def score_bias(items, positive_key="impact"):
    """
    Count positive vs negative hints and return bias + score.
    """
    pos, neg = 0, 0

    for it in items:
        val = it.get(positive_key, "").lower()
        if val in ["positive", "bullish", "up"]:
            pos += 1
        elif val in ["negative", "bearish", "down"]:
            neg += 1

    if pos > neg:
        return "BULLISH", pos - neg
    elif neg > pos:
        return "BEARISH", neg - pos
    else:
        return "NEUTRAL", 0


def merge_signals(govt, tenders, corporate, market):
    """
    Merge all data streams into ONE actionable signal.
    """

    # Govt / Tender / Corporate bias
    bias_g, score_g = score_bias(govt)
    bias_t, score_t = score_bias(tenders, positive_key="status")
    bias_c, score_c = score_bias(corporate)

    # Market bias
    market_bias = "BULLISH" if market.get("risk_level") in ["low", "moderate"] else "BEARISH"
    score_m = 1

    # Weighted conviction score
    total_score = (
        score_g * WEIGHTS["govt"] +
        score_t * WEIGHTS["tender"] +
        score_c * WEIGHTS["corporate"] +
        score_m * WEIGHTS["market"]
    )

    conviction = round(total_score * 100)

    # Final bias (majority vote)
    biases = [bias_g, bias_t, bias_c, market_bias]
    final_bias = max(set(biases), key=biases.count)

    # Action decision
    decision = "WAIT"
    if conviction >= 70:
        if final_bias == "BULLISH":
            decision = "BUY"
        elif final_bias == "BEARISH":
            decision = "SELL"

    return {
        "decision": decision,
        "final_bias": final_bias,
        "conviction_score": conviction,
        "timestamp": datetime.now()
    }
