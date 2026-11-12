Python
Run

import time

# 1. Elective registration details
ai_elective = {
    "192311001", "192311004", "192311007",
    "192311009", "192311004"
}

iot_elective = {
    "192311002", "192311004", "192311009",
    "192311010"
}

all_students = {
    f"1923110{i:02d}" for i in range(1, 11)
}

# 2. Set operations
both = ai_elective & iot_elective

exactly_one = ai_elective ^ iot_elective

ai_only = ai_elective - iot_elective

iot_only = iot_elective - ai_elective

registered = ai_elective | iot_elective

neither = all_students - registered

# 3. Sorted reports
print("ELECTIVE REGISTRATION REPORT")

print("AI Elective:", sorted(ai_elective))
print("IoT Elective:", sorted(iot_elective))
