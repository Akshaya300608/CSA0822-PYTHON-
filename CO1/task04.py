import math
 
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
 
def calculate_rate(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(
        BASE_RATE + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE, 2
    )
 
def calculate_payment(litres, fat, snf):
    return round(litres * calculate_rate(fat, snf), 2)
 
print("Rate:", calculate_rate(4.2, 8.7))
print("Payment:", calculate_payment(8.5, 4.2, 8.7))
 
raw_steps = (4.2 - 3.5) / 0.1
negative_steps = (3.1 - 3.5) / 0.1
print("Raw steps for fat 4.2:", raw_steps)
print("round, int, floor for fat 3.1:",
      round(negative_steps), int(negative_steps), math.floor(negative_steps))
print("Chained comparison:", 2.0 <= 4.2 <= 7.0)
