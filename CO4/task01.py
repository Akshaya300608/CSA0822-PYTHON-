from decimal import Decimal, InvalidOperation
import tempfile

def process_mess_bill(filename):

    total = Decimal("0.00")
    report = []
    rejected = []

    try:
        with open(filename, "r", encoding="utf-8") as file:

            for line_number, line in enumerate(file, start=1):

                line = line.strip()

                if not line:
                    continue

                try:
                    parts = line.split(",")

                    if len(parts) != 3:
                        raise ValueError("Expected 3 fields")

                    register_no = parts[0].strip()
                    name = parts[1].strip()

                    if not register_no or not name:
                        raise ValueError("Missing register number or name")

                    try:
                        amount = Decimal(parts[2].strip())
                    except InvalidOperation:
                        raise ValueError("Invalid amount")

                    if not amount.is_finite() or amount < 0:
                        raise ValueError("Invalid amount")

                    total += amount
                    report.append(name + " " + format(amount, ".2f"))

                except ValueError as error:
                    rejected.append(
                        (line_number, line, str(error))
                    )

        print("MESS BILL REPORT")
        print("----------------------")

        for record in report:
            print(record)

        print("\nTotal Amount: Rs.", format(total, ".2f"))

        print("\nRejected Records:")

        if rejected:
            for item in rejected:
                print(item)
        else:
            print("No rejected records")

    except FileNotFoundError:
        print("Error: File not found")

    except PermissionError:
        print("Error: Permission denied")


# Create sample file in temporary location
data = (
    "192311001,Arun,1250.50\n"
    "192311002,Priya,1500.00\n"
    "192311003,Ravi,1200.75\n"
    "192311004,Kumar,invalid\n"
    "192311005,Divya\n"
)

with tempfile.NamedTemporaryFile(
    mode="w",
    suffix=".txt",
    encoding="utf-8",
    delete=False
) as file:

    file.write(data)
    filename = file.name

# Process the file
process_mess_bill(filename)
