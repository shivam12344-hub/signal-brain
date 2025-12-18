def calculate_confidence(signal):
    strength = signal.get("strength", 0)

    if strength >= 80:
        grade = "VERY HIGH CONVICTION"
    elif strength >= 65:
        grade = "HIGH CONVICTION"
    elif strength >= 50:
        grade = "MEDIUM CONVICTION"
    else:
        grade = "LOW CONVICTION"

    return {
        "headline": signal.get("headline"),
        "bias": signal.get("bias"),
        "confidence_score": strength,
        "grade": grade
    }
