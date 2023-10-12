import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_path", help="Phonebook file path")
args = parser.parse_args()

current_dir = os.path.dirname(os.path.realpath(__file__))

PHONEBOOK = {}

datafile_path = os.path.join(current_dir, (args.data_path + ".json"))

if os.path.exists(datafile_path):
    with open(datafile_path, "r") as file:
        PHONEBOOK = json.load(file)


def add_contact():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    full_name = first_name + " " + last_name
    telephone_number = input("Enter telephone number: ")
    city_or_state = input("Enter city or state: ")

    if telephone_number and full_name:
        PHONEBOOK[telephone_number] = {
            "first_name": first_name,
            "last_name": last_name,
            "full_name": full_name,
            "address": city_or_state,
        }

        with open(datafile_path, "w") as file_obj:
            json.dump(PHONEBOOK, file_obj, indent=4)
            print(PHONEBOOK)

    else:
        print("Invalid input. Both name and telephone number are required.")


def search(type_: str) -> dict:
    return {number: contact for number, contact in PHONEBOOK.items() if type_.lower() in contact['full_name'].lower()}


def update_phonebook(phone):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    full_name = first_name + " " + last_name
    city_or_state = input("Enter city or state: ")

    updated_phonebook = {}
    if phone and full_name:
        updated_phonebook[phone] = {
            "first_name": first_name,
            "last_name": last_name,
            "full_name": full_name,
            "address": city_or_state,
        }
        PHONEBOOK.update(updated_phonebook)

        with open(datafile_path, "w") as file_obj:
            json.dump(PHONEBOOK, file_obj, indent=4)
            print(PHONEBOOK)


def delete_phone():
    number = input("Enter telephone number to delete: ")
    if number in PHONEBOOK:
        del PHONEBOOK[number]

        with open(datafile_path, "w") as file_obj:
            json.dump(PHONEBOOK, file_obj, indent=4)

        print(f"Phone number {number} deleted.")
    else:
        print(f"Phone number {number} not found in the phonebook.")


while True:

    print("Please select options")
    print("+-----------------+")
    print("1: Add new entries")
    print("2: Search by name, surname, full name")
    print("3: Search by telephone number")
    print("4: Search by city or state")
    print("5: Delete a record for a given telephone number")
    print("6: Update a record for a given telephone number")
    print("7: Exit the program")
    print("+------------------+")

    user_chose = input("Chose number: ")
    allowed_input = ["1", "2", "3", "4", "5", "6", "7"]

    if user_chose in allowed_input:
        if user_chose == "1":
            add_contact()

        if user_chose == "2":
            search_element = input("Enter name, surname or full name: ")
            search(search_element)
            print("===========>")
            print(PHONEBOOK)

        if user_chose == "3":
            search_element = input("Enter telephone number: ")
            search(search_element)
            print("===========>")
            print(PHONEBOOK)

        if user_chose == "4":
            search_element = input("Enter city or state: ")
            search(search_element)
            print("===========>")
            print(PHONEBOOK)

        if user_chose == "5":
            delete_phone()
            print("===========>")
            print(PHONEBOOK)

        if user_chose == "6":
            search_element = input("Enter telephone number: ")
            update_phonebook(search_element)
            print("===========>")
            print(PHONEBOOK)

        if user_chose == "7":
            print("Good bye")
            exit()

    else:
        "Please enter correct number"
