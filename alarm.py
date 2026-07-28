import time
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Alarm:
    alarm_time: datetime
    label: str = "Alarm"
    is_active: bool = True

    def display(self):
        status = "Active" if self.is_active else "Inactive"

        return f"{self.alarm_time.strftime('%H:%M')} - {self.label} ({status})"


class AlarmManager:

    def __init__(self):
        self.alarms = []

    def add_alarm(self, alarm):
        self.alarms.append(alarm)

    def list_alarms(self):
        return self.alarms

    def delete_alarm(self, index):
        if 0 <= index < len(self.alarms):
            removed_alarm = self.alarms.pop(index)
            return removed_alarm

        return None
