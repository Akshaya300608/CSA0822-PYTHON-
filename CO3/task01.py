Python
Run
import time

# Function to normalise phone numbers
def normalise_number(number):
    digits = ""

    for ch in number:
        if ch.isdigit():
            digits += ch

    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]

    return digits


# Function to normalise names
def normalise_name(name):
    return " ".join(name.lower().split())


# Function to merge contacts
def merge_contacts(contacts):

    phone_index = {}
    groups = {}
    next_id = 0

    for contact in contacts:

        name = contact.get("name", "")
        numbers = contact.get("numbers", [])
        emails = contact.get("emails", [])

        valid_numbers = set()

        for number in numbers:
            normal = normalise_number(number)

            if len(normal) == 10:
                valid_numbers.add(normal)

        # Find existing contact groups
        matched_ids = set()

        for number in valid_numbers:
            if number in phone_index:
                matched_ids.add(phone_index[number])

        # Create a new group if no match exists
        if not matched_ids:
            group_id = next_id
            next_id += 1

            groups[group_id] = {
                "names": set(),
                "numbers": set(),
                "emails": set()
            }

        else:
            group_id = min(matched_ids)
