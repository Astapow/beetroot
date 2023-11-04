import pytest

from task3 import TVController, CHANNELS


def test_first_channel():
    controller = TVController(CHANNELS)
    assert controller.first_channel() == "BBC"

    with pytest.raises(ValueError, match="Channel list cannot be empty"):
        controller = TVController([])
        controller.first_channel()


def test_last_channel():
    controller = TVController(CHANNELS)
    assert controller.last_channel() == "TV1000"


def test_turn_channel():
    controller = TVController(CHANNELS)
    assert controller.turn_channel(1) == "BBC"
    assert controller.turn_channel(4) == "There is no such channel"


def test_next_channel():
    controller = TVController(CHANNELS)
    controller.next_channel()
    assert controller.next_channel() == "TV1000"
    controller.next_channel()
    assert controller.next_channel() == "Discovery"


def test_previous_channel():
    controller = TVController(CHANNELS)
    controller.previous_channel()
    assert controller.previous_channel() == "Discovery"


def test_current_channel():
    controller = TVController(CHANNELS)
    assert controller.current_channel() == "BBC"
    controller.next_channel()
    assert controller.current_channel() == "Discovery"


def test_is_exist():
    controller = TVController(CHANNELS)
    assert controller.is_exist(4) == "No"
    assert controller.is_exist(5) == "No"
    assert controller.is_exist(1) == "Yes"
    assert controller.is_exist("BBC") == "Yes"
    assert controller.is_exist("HBO") == "No"
