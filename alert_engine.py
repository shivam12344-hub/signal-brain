from datetime import datetime

# Decide whether alert should be triggered
def should_alert(signal: dict) -> bool:
    confidence = signal.get("confidence", {})
    grade = confidence.get("grade", "")

    if grade in ["HIGH CONVICTION", "VERY HIGH CONVICTION"]:
        return True
    return False


# Build alert payload (future: push / email / app notification)
def build_alert(signal: dict) -> dict:
    return {
        "time": datetime.now().isoformat(),
        "headline": signal.get("headline"),
        "sector": signal.get("sector"),
        "bias": signal.get("bias"),
        "confidence": signal.get("confidence"),
        "priority": signal.get("priority"),
        "message": f"HIGH PRIORITY SIGNAL in {signal.get('sector')}"
    }
