from collections import deque

# keep last 20 signals
_HISTORY = deque(maxlen=20)

def add_signal(signal: dict):
    _HISTORY.appendleft(signal)

def get_history():
    return list(_HISTORY)
