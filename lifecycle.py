# lifecycle.py
# Controls the life and death of a signal

from datetime import datetime, timedelta


class SignalLifecycle:
    def __init__(self):
        self.max_idle_hours = 24  # kill signal if nothing new happens

    def should_create(self, confidence):
        """
        Decide if a signal deserves to be born
        """
        return confidence >= 40

    def classify_stage(self, confidence):
        """
        Decide signal stage based on confidence
        """
        if confidence >= 90:
            return "STRONG_ACTION"
        elif confidence >= 75:
            return "ACTION"
        elif confidence >= 60:
            return "WATCH"
        else:
            return "IGNORE"

    def should_notify(self, previous_stage, new_stage):
        """
        Notify only on meaningful upgrades
        """
        if previous_stage is None:
            return new_stage in ["ACTION", "STRONG_ACTION"]

        order = ["IGNORE", "WATCH", "ACTION", "STRONG_ACTION"]
        return order.index(new_stage) > order.index(previous_stage)

    def is_expired(self, last_update_time):
        """
        Kill signal if inactive for too long
        """
        return datetime.now() - last_update_time > timedelta(hours=self.max_idle_hours)
