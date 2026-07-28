# scheduler.py

import time
from datetime import datetime


class AlarmScheduler:

    def __init__(self, manager):
        self.manager = manager
        self.running = True


    def monitor_alarms(self):

        while self.running:

            current_time = datetime.now().strftime("%H:%M")

            for alarm in self.manager.alarms[:]:

                if alarm.alarm_time.strftime("%H:%M") == current_time:

                    print("\n⏰ Alarm Ringing!")
                    print("Message", alarm.label)

                    self.manager.delete_alarm(
                        self.manager.alarms.index(alarm)
                    )

            time.sleep(1)


    def stop(self):
        self.running = False