BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
 
farmer_entries = [
    ("F001", 10.0, 3.5, 8.5, "Morning"),
    ("F002", 8.5, 4.2, 8.7, "Evening"),
    ("F003", 12.0, 3.1, 8.3, "Morning")
]
 
print("Rate-card constants:")
print("Base rate:", BASE_RATE)
print("Standard fat:", STANDARD_FAT)
print("Standard SNF:", STANDARD_SNF)
 
print("\nFarmer entries:")
for farmer_id, litres, fat, snf, shift in farmer_entries:
    print(farmer_id, litres, fat, snf, shift)
    print("Types:", type(farmer_id).__name__,
          type(litres).__name__, type(fat).__name__,
          type(snf).__name__, type(shift).__name__)
