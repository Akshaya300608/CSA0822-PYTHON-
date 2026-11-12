Python
Run

students = {
    "Akshaya": ["P", "P", "P"],
    "Priya": ["A", "A", "A"],
    "Kavi": ["P", "A", "P"]
}

def calculate_percentage(attendance):
    present = attendance.count("P")
    return (present / len(attendance)) * 100

def absent_three_days(attendance):
    return all(day == "A" for day in attendance)

def generate_report():
    print("ATTENDANCE REPORT")
    for name, attendance in students.items():
        percentage = calculate_percentage(attendance)
        print(name, "-", percentage, "%")

    print("\nAbsent for three consecutive days:")
    for name, attendance in students.items():
        if absent_three_days(attendance):
            print(name)

if __name__ == "__main__":
    generate_report()
