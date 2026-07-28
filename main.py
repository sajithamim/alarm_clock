import threading
from datetime import datetime
from alarm import Alarm, AlarmManager
from utils import parse_time
from scheduler import AlarmScheduler

def display_menu():
    """Display the main menu options"""
    print("\n===Alarm clock===")
    print("1. Set Alarm")
    print("2. View Alarms")
    print("3. Delete Alarm")
    print("4. Exit")


def main():
    manager = AlarmManager()

    scheduler = AlarmScheduler(manager)

    monitor_thread = threading.Thread(
        target=scheduler.monitor_alarms,
        daemon=True
    )
    monitor_thread.start()

    while True:
        display_menu()

        choice = input("Enter your choice (1-4):")

        if choice == "1":
            time_input = input("Enter alarm time (HH:MM): ")

            alarm_time = parse_time(time_input)

            if alarm_time is None:
                print("Invalid time format")
                continue

            label = input("Enter alarm label: ")

            alarm = Alarm(
                alarm_time=alarm_time,
                label=label
            )

            manager.add_alarm(alarm)

            print("Alarm added successfully!")
        
        elif choice == "2":
            alarms = manager.list_alarms()

            if not alarms:
                print("No alarms found")

            else:
                print("\n===== Your Alarms =====")

                for index, alarm in enumerate(alarms, start=1):
                    print(f"{index}. {alarm.display()}")

                print("=======================")

        elif choice == "3":
            alarm_number = int(input("Enter alarm number to delete: "))
            deleted = manager.delete_alarm(alarm_number - 1)

            if deleted:
                print("Alarm deleted successfully.")
            else:
                print("Invalid alarm number.")
        
        elif choice == "4":
            print("Thank you for choosing Alarm Clock")
            break

        else:
            print("Invalid choice.Please select a valid number")

if __name__ == "__main__":
    main()