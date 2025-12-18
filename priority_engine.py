def evaluate_priority(signal):
    """
    Decide how important a signal is.
    """

    strength = signal.get("strength", 0)
    sector = signal.get("sector", "").lower()
    bias = signal.get("bias", "").upper()

    priority = "IGNORE"
    urgency = "LOW"
    tag = "NORMAL"

    # --- Base confidence rules ---
    if strength >= 80:
        priority = "ACT"
        urgency = "HIGH"
    elif strength >= 65:
        priority = "WATCH"
        urgency = "MEDIUM"
    elif strength >= 50:
        priority = "WATCH"
        urgency = "LOW"

    # --- Sector boost (strategic sectors) ---
    strategic_sectors = ["infrastructure", "energy", "defence", "banking"]

    if sector in strategic_sectors and strength >= 65:
        priority = "ACT"
        urgency = "HIGH"

    # --- Rare signal logic ---
    if strength >= 75 and bias in ["BULLISH", "BEARISH"]:
        tag = "RARE"
        priority = "ACT"
        urgency = "IMMEDIATE"

    return {
        "priority": priority,
        "urgency": urgency,
        "tag": tag
    }
