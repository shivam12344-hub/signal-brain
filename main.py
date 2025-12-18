from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from data_sources.news.news_ingest import fetch_news
from signal_engine import generate_signal
from confidence import calculate_confidence
from priority_engine import evaluate_priority

app = FastAPI(title="Signal Brain API", version="1.0")
templates = Jinja2Templates(directory="templates")

# in-memory history (temporary)
SIGNAL_HISTORY = []

@app.get("/")
def root():
    return {"status": "Signal Brain running"}

@app.get("/signals")
def get_signals():
    news = fetch_news()
    signals = []

    for n in news:
        sig = generate_signal(n)
        sig["confidence"] = calculate_confidence(sig)
        sig["priority"] = evaluate_priority(sig)
        signals.append(sig)

    return signals

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    news = fetch_news()
    signals = []

    for n in news:
        sig = generate_signal(n)
        sig["confidence"] = calculate_confidence(sig)
        sig["priority"] = evaluate_priority(sig)
        signals.append(sig)

        SIGNAL_HISTORY.append(sig)

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "signals": signals}
    )

@app.get("/api/history")
def history():
    return SIGNAL_HISTORY[-50:]  # last 50 signals
