# Q3 - Exception Handling in Attendance Processor

# Custom exception
class InvalidRecord(Exception):
    pass


# TODO 1: Parse attendance record
def parse_line(line):

    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord(
            "expected 3 fields, found " + str(len(parts))
        )

    register = parts[0].strip()
    date = parts[1].strip()
    status = parts[2].strip()

    if register == "" or date == "":
        raise InvalidRecord("missing register number or date")

    if status != "P" and status != "A":
        raise InvalidRecord("invalid status " + repr(status))

    return register, date, status


# TODO 2: Process attendance records
def summarise(data):

    present = 0
    absent = 0
    errors = []

    lines = data.splitlines()

    try:
        for line_number, line in enumerate(lines, start=1):

            try:
                register, date, status = parse_line(line)

                if status == "P":
                    present += 1
                else:
                    absent += 1

            except InvalidRecord as error:
                errors.append((line_number, str(error)))

    except ValueError as error:
        print("Processing error:", error)

    else:
        print("Attendance records processed successfully.")

    finally:
        print("Processing completed.")

    return present, absent, errors


# Sample attendance data
data = (
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
)

# Display result
print(summarise(data))


# Test missing file concept
def test_missing_file():
    try:
        raise FileNotFoundError("Attendance file not found")

    except FileNotFoundError as error:
        print("Error:", error)

    finally:
        print("File checking completed.")


print("\nMISSING FILE TEST")
test_missing_file()
