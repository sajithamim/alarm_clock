from utils import parse_time


def test_invalid_time():

    result = parse_time("invalid")

    assert result is None

def test_valid_time():

    result = parse_time("07:30")

    assert result is not None