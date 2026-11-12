Run
def normalise(text):
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text.upper()


def is_valid(reg):
    if len(reg) != 9 and len(reg) != 10:
        return False

    state = reg[:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    if not state.isalpha():
        return False

    if not district.isdigit():
        return False

    if len(series) < 1 or len(series) > 2:
        return False

    if not series.isalpha():
        return False

    if not number.isdigit():
        return False

    return True


def format_receipt(reg):
    state = reg[:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    return state + " " + district + " " + series + " " + number


vehicles = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "mh 12 cd 5678",
    "KL-07-XY-9876"
]

print("VEHICLE REGISTRATION VALIDATOR")

for raw in vehicles:
    reg = normalise(raw)

    if is_valid(reg):
        print(raw, "->", reg, "VALID")
        print("Receipt:", format_receipt(reg))
    else:
        print(raw, "->", reg, "INVALID")
7. ALTERNATIVE METHOD – REGULAR EXPRESSION
The same validation can be performed using a regular expression with Python's re module.
Python
Run
import re

def validate_regex(reg):
    pattern = r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}"

    if re.fullmatch(pattern, reg):
        return True
    else:
        return False


reg = "TN09AB1234"

if validate_regex(reg):
    print("Valid Registration Number")
else:
    print("Invalid Registration Number")
