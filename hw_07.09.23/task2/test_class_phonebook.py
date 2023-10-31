import json
from unittest.mock import patch

from pytest import fixture

from class_phonebook import Phonebook


@fixture(autouse=True)
def json_file():
    file = "phonebook.json"
    with open(file, "w") as fp:
        json.dump({}, fp)

    yield


def test_add_contact_first(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'John')

    phonebook = Phonebook()
    phonebook.add_contact()

    with open("phonebook.json", "r") as file:
        phonebook_data = json.load(file)
        assert len(phonebook_data) == 1
        assert list(phonebook_data.values())[0]["first_name"] == "John"


def test_add_contact_second(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Nolan')

    phonebook = Phonebook()
    phonebook.add_contact()

    with open("phonebook.json", "r") as file:
        phonebook_data = json.load(file)
        assert len(phonebook_data) == 1
        assert list(phonebook_data.values())[0]["last_name"] == "Nolan"


def test_add_contact(monkeypatch):
    user_input = ["pety", "shi", "0636363", "II"]

    def mock_input(prompt):
        return user_input.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    phonebook = Phonebook()
    phonebook.add_contact()

    with open("phonebook.json", "r") as file:
        phonebook_data = json.load(file)
        assert len(phonebook_data) == 1
        assert list(phonebook_data.values())[0]["first_name"] == "pety"
        assert list(phonebook_data.values())[0]["last_name"] == "shi"
        assert list(phonebook_data.values())[0]["address"] == "II"


def test_search_by_pattern():
    phonebook = Phonebook()
    phonebook.phonebook = {
        "1234": {"first_name": "Den", "last_name": "Last", "address": "UA"},
        "4321": {"first_name": "Nick", "last_name": "First", "address": "AU"},
    }

    result = phonebook.search_by_pattern("Nick", "first_name")
    assert len(result) == 1
    assert "4321" in result


def test_delete_phone():
    phonebook = Phonebook()
    phonebook.phonebook = {
        "1234": {"first_name": "Den", "last_name": "Last", "address": "UA"},
        "4321": {"first_name": "Nick", "last_name": "First", "address": "AU"},
    }

    with patch('builtins.input', return_value="1234"):
        phonebook.delete_phone()

    assert "1234" not in phonebook.phonebook
    assert "4321" in phonebook.phonebook


def test_update_phonebook(monkeypatch):
    phonebook = Phonebook()
    phonebook.phonebook = {
        "1234": {"first_name": "Den", "last_name": "Last", "address": "UA"},
        "4321": {"first_name": "Nick", "last_name": "First", "address": "AU"},
    }
    user_input = ["0636363", "pety", "shi", "II"]

    def mock_input(prompt):
        return user_input.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    phonebook.update_phonebook()
    update_data = phonebook.phonebook["0636363"]
    assert update_data["first_name"] == "pety"
    assert update_data["last_name"] == "shi"
    assert update_data["address"] == "II"
