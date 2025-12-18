import time
from signal_router import merge_signals
from alerts import send_telegram
from history import add_signal

from data_sources.govt.govt_ingest import fetch_govt_updates
from data_sources.corporate.corporate_ingest import fetch_corporate_events
from data_sources.market.market_ingest import fetch_market_snapshot

INTERVAL_SECONDS = 300  # every 5 minutes
ALERT_MIN_CONVICTION = 75  # smart threshold


def run_scheduler():
    print("🚀 Signal Brain LIVE Automation Started")

    while True:
        try:
            govt = fetch_govt_updates()
            corp = fetch_corporate_events()
            market = fetch_market_snapshot()

            signal = merge_signals(
                govt=govt,
                tenders=[],
                corporate=corp,
                market=market
            )

            print("✅ AUTO SIGNAL GENERATED:")
            print(signal)

            # save to history
            add_signal(signal)

            # Telegram alert ONLY for STRONG BUY / SELL
            if (
                signal.get("decision") in ["BUY", "SELL"]
                and signal.get("conviction_score", 0) >= ALERT_MIN_CONVICTION
            ):
                msg = (
                    "📢 SIGNAL ALERT (HIGH CONVICTION)\n"
                    f"Decision: {signal.get('decision')}\n"
                    f"Bias: {signal.get('final_bias')}\n"
                    f"Conviction: {signal.get('conviction_score')}\n"
                    f"Time: {signal.get('timestamp')}"
                )
                send_telegram(msg)

        except Exception as e:
            print("❌ ERROR:", e)

        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    run_scheduler()
