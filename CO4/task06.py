# CO4 - QUESTION 6
# College Fest Registration Desk
# Single-file version for Programiz

# Sample department data
department_files = {
    "department1.txt": """
192311001,Akshaya,IT,akshaya@gmail.com,Dance;Singing
192311002,Priya,IT,priya@gmail.com,Singing;Drama
""",

    "department2.txt": """
192311003,Kavi,CSE,kavi@gmail.com,Dance
192311001,Akshaya,IT,akshaya@gmail.com,Dance
""",

    "department3.txt": """
192311004,Ram,ECE,ram@gmail.com,Drama
192311005,John,ECE,johngmail.com,Singing
""",

    "department4.txt": """
192311006,Meena,EEE,meena@gmail.com,Dance;Drama
192311008,Arun,MECH,arun@gmail.com,Singing
192311007
"""
}

# Five department files to process
file_names = [
    "department1.txt",
    "department2.txt",
    "department3.txt",
    "department4.txt",
    "department5.txt"
]

master = []
events = {}
errors = []
seen = set()


# Email validation
def valid_email(email):
    if "@" not in email:
        return False

    parts = email.split("@")

    if len(parts) != 2:
        return False

    if parts[0] == "" or "." not in parts[1]:
        return False

    if parts[1].startswith(".") or parts[1].endswith("."):
        return False

    return True


# Process department records
for filename in file_names:

    try:
        content = department_files[filename]

        lines = content.strip().split("\n")

        for line_number, line in enumerate(lines, 1):

            try:
                fields = line.strip().split(",")

                if len(fields) != 5:
                    raise ValueError("Damaged record")

                reg_no, name, dept, email, event_text = fields

                if not all([reg_no, name, dept, email, event_text]):
                    raise ValueError("Missing field")

                if not valid_email(email):
                    raise ValueError("Invalid email")

                if reg_no in seen:
                    raise ValueError("Duplicate registration")

                seen.add(reg_no)

                student = {
                    "Register No": reg_no,
                    "Name": name,
                    "Department": dept,
                    "Email": email
                }

                master.append(student)

                student_events = event_text.split(";")

                for event in student_events:
                    event = event.strip()

                    if event:
                        events.setdefault(event, []).append(name)

            except ValueError as error:
                errors.append(
                    filename + " - Line " +
                    str(line_number) + ": " + str(error)
                )

    except KeyError:
        errors.append(filename + ": File not found")

    except Exception as error:
        errors.append(filename + ": " + str(error))


# Display master list
print("COLLEGE FEST PROCESSING COMPLETED")

print("\nValid Registrations:", len(master))

print("\nMASTER LIST")

for student in master:
    print(
        student["Register No"],
        student["Name"],
        student["Department"],
        student["Email"]
    )


# Display event-wise participants
print("\nEVENT-WISE PARTICIPANTS")

for event, students in events.items():
    print(event, ":", ", ".join(students))


# Display summary
print("\nSUMMARY REPORT")

print("Total Students:", len(master))
print("Total Events:", len(events))
print("Total Errors:", len(errors))


# Display error log
print("\nERROR LOG")

for error in errors:
    print(error)
