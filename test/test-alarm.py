from alarm import Alarm, AlarmManager
from utils import parse_time

def test_add_alarm():

    manager = AlarmManager()

    alarm = Alarm(
        alarm_time="07:30",
        label="Wake up"
    )

    manager.add_alarm(alarm)

    assert len(manager.list_alarms()) == 1

def test_delete_alarm():

    manager = AlarmManager()

    alarm = Alarm(
        alarm_time="07:30",
        label="Wake up"
    )

    manager.add_alarm(alarm)

    deleted = manager.delete_alarm(0)

    assert deleted.label == "Wake up"
    assert len(manager.list_alarms()) == 0

def test_invalid_time():

    result = parse_time("invalid")

    assert result is None

def test_valid_time():

    result = parse_time("07:30")

    assert result is not None