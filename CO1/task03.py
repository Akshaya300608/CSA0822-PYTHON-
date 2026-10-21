BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
 
farmer_id = "F001"
litres = 10
fat = 4.2
snf = 8.7
 
print("Farmer:", farmer_id)
print("Litres:", litres)
print("Fat:", fat)
print("SNF:", snf)
 
# Dynamic typing
value = 10
print(value, type(value).__name__)
value = "ten"
print(value, type(value).__name__)
 
# Multiple assignment and swapping
a, b = 5, 9
a, b = b, a
print("After swapping:", a, b)
 
RATE_CARD = {
    "base": BASE_RATE,
    "fat_step": FAT_STEP_VALUE,
    "snf_step": SNF_STEP_VALUE
}
print("Rate card:", RATE_CARD)
