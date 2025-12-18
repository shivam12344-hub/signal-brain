from datetime import datetime

# SAFE MODE tender ingestion
# (Future: CPPP / GeM automation yahin connect hoga)

KEYWORDS_INFRA = [
    "highway", "road", "railway", "metro",
    "bridge", "construction", "corridor"
]

KEYWORDS_DEFENCE = [
    "defence", "missile", "radar", "naval", "air force"
]

KEYWORDS_ENERGY = [
    "power", "solar", "wind", "transmission", "grid"
]


def detect_sector(text: str) -> str:
    text = text.lower()

    for k in KEYWORDS_INFRA:
        if k in text:
            return "infrastructure"

    for k in KEYWORDS_DEFENCE:
        if k in text:
            return "defence"

    for k in KEYWORDS_ENERGY:
        if k in text:
            return "energy"

    return "general"


def fetch_tenders():
    """
    SAFE MODE:
    Returns structured tender-like signals.
    Never crashes if real source is unavailable.
    """

    raw_tenders = [
        "Railways issues tender for new signalling corridor",
        "NHAI invites bids for highway expansion project",
        "Ministry of Defence floats radar system procurement",
    ]

    tenders = []

    for t in raw_tenders:
        sector = detect_sector(t)

        tenders.append({
            "source": "tender",
            "headline": t,
            "sector": sector,
            "impact": "positive",
            "time": datetime.now()
        })

    return tenders
