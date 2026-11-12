def separate_if(units, ration, senior):
    result = []

    if units <= 100:
        result.append("Full Subsidy")

    if 101 <= units <= 200 and ration == "yes":
        result.append("Partial Subsidy")

    if units > 200 and senior == "yes":
        result.append("Special Subsidy")

    if len(result) == 0:
        result.append("No Subsidy")

    return ", ".join(result)


def if_elif_else(units, ration, senior):

    if units <= 100:
        return "Full Subsidy"

    elif 101 <= units <= 200 and ration == "yes":
        return "Partial Subsidy"

    elif units > 200 and senior == "yes":
        return "Special Subsidy"

    else:
        return "No Subsidy"


print("ELECTRICITY SUBSIDY ELIGIBILITY")

for i in range(1, 9):
    print("\nHousehold", i)

    units = int(input("Enter electricity units: "))
    ration = input("Ration card (yes/no): ").lower()
    senior = input("Member above 80 years (yes/no): ").lower()

    result1 = separate_if(units, ration, senior)
    result2 = if_elif_else(units, ration, senior)

    print("Separate if:", result1)
    print("If-elif-else:", result2)
