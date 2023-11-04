import os
import json
import argparse


class Phonebook:
    def __init__(self, data_path="phonebook.json"):
        self.datafile_path = data_path
        self.phonebook = {}
        if os.path.exists(self.datafile_path):
            with open(self.datafile_path, "r") as file:
                self.phonebook = json.load(file)

    def add_contact(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        telephone_number = input("Enter telephone number: ")
        city_or_state = input("Enter city or state: ")

        if telephone_number and first_name and last_name:
            self.phonebook[telephone_number] = {
                "first_name": first_name,
                "last_name": last_name,
                "address": city_or_state,
            }

            with open(self.datafile_path, "w") as file_obj:
                json.dump(self.phonebook, file_obj, indent=4)
                print(self.phonebook)
        else:
            print("Invalid input. Both name and telephone number are required.")

    def search_by_pattern(self, search_term, field):
        if field in ["first_name", "last_name", "address"]:

            return {number: contact for number, contact in self.phonebook.items()
                    if search_term.lower() in contact[field].lower()}

        elif field == "full_name":
            return {number: contact for number, contact in self.phonebook.items()
                    if search_term.lower() in (contact['first_name'] + ' ' + contact['last_name']).lower()}

        elif field == "phone":
            return {number: contact for number, contact in self.phonebook.items()
                    if search_term in number}

        else:
            return {}

    def search_by_name(self):
        search_term = input("Enter name or full name: ")
        return self.search_by_pattern(search_term, "first_name")

    def search_by_surname(self):
        search_term = input("Enter name or full name: ")
        return self.search_by_pattern(search_term, "last_name")

    def search_by_fullname(self):
        search_term = input("Enter name or full name: ")
        return self.search_by_pattern(search_term, "full_name")

    def search_by_phone(self):
        search_term = input("Enter phone number: ")
        return self.search_by_pattern(search_term, "phone")

    def search_by_city(self):
        search_term = input("Enter city or address: ")
        return self.search_by_pattern(search_term, "address")

    def update_phonebook(self):
        phone = input("Enter telephone number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        city_or_state = input("Enter city or state: ")

        updated_phonebook = {}
        if phone and first_name and last_name:
            updated_phonebook[phone] = {
                "first_name": first_name,
                "last_name": last_name,
                "address": city_or_state,
            }
            self.phonebook.update(updated_phonebook)

            with open(self.datafile_path, "w") as file_obj:
                json.dump(self.phonebook, file_obj, indent=4)
                print(self.phonebook)

    def delete_phone(self):
        number = input("Enter telephone number to delete: ")
        if number in self.phonebook:
            del self.phonebook[number]

            with open(self.datafile_path, "w") as file_obj:
                json.dump(self.phonebook, file_obj, indent=4)

            print(f"Phone number {number} deleted.")
        else:
            print(f"Phone number {number} not found in the phonebook.")

    def run(self):
        while True:
            print("Please select options:")
            print("+----------------+")
            print("1: Add new entries")
            print("2: Search by name, surname, full name")
            print("3: Search by telephone number")
            print("4: Search by city or state")
            print("5: Delete a record for a given telephone number")
            print("6: Update a record for a given telephone number")
            print("7: Exit the program")
            print("+------------------+")

            user_choice = input("Enter number: ")
            allowed_input = ["1", "2", "3", "4", "5", "6", "7"]

            action_by_choice = {
                "1": self.add_contact,
                "2": self.search_by_fullname,
                "3": self.search_by_phone,
                "4": self.search_by_city,
                "5": self.delete_phone,
                "6": self.update_phonebook,
                "7": exit,
            }

            if user_choice in allowed_input:
                action = action_by_choice[user_choice]
                if action in [self.search_by_fullname, self.search_by_phone, self.search_by_city]:
                    results = action()
                    print(results)
                else:
                    action()
                    print("===========>")
            else:
                print("Please enter correct number")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", help="Phonebook file path")
    args = parser.parse_args()

    current_dir = os.path.dirname(os.path.realpath(__file__))
    datafile_path = os.path.join(current_dir, (args.data_path + ".json"))

    phonebook = Phonebook(datafile_path)
    phonebook.run()
