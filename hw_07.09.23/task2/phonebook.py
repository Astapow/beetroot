import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_path", help="Phonebook file path")
args = parser.parse_args()

current_dir = os.path.dirname(os.path.realpath(__file__))

PHONEBOOK = {}

datafile_path = os.path.join(current_dir, (args.data_path + ".json"))


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
    else:
        print("Invalid input. Both name and telephone number are required.")


if os.path.exists(datafile_path):
    with open(datafile_path, "r") as file:
        PHONEBOOK = json.load(file)

add_contact()

with open(datafile_path, "w") as file:
    json.dump(PHONEBOOK, file, indent=4)
    print(PHONEBOOK)
