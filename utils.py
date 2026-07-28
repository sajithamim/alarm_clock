from datetime import datetime


def parse_time(time_string):
    """
    Convert user input time into datetime object.
    Expected format: HH:MM
    """

    try:
        alarm_time = datetime.strptime(time_string, "%H:%M")
        return alarm_time

    except ValueError:
        print("Please enter a number")