# 1. Using for loop and append()
def using_loop(data):
    celsius = []
    fahrenheit = []

    for temp in data:
        if -50 <= temp <= 50:
            celsius.append(temp)
            fahrenheit.append((temp * 9 / 5) + 32)

    return celsius, fahrenheit


# 2. Using list comprehension
def using_comprehension(data):
    celsius = [temp for temp in data if -50 <= temp <= 50]

    fahrenheit = [
        (temp * 9 / 5) + 32
        for temp in data if -50 <= temp <= 50
    ]

    return celsius, fahrenheit


# 3. Using map(), filter() and lambda
def using_map_filter(data):
    valid = list(filter(lambda x: -50 <= x <= 50, data))

    celsius = valid
    fahrenheit = list(map(lambda x: (x * 9 / 5) + 32, valid))

    return celsius, fahrenheit


# Display original readings
print("Original Readings:", readings)


# Execute all three methods
loop_c, loop_f = using_loop(readings)
comp_c, comp_f = using_comprehension(readings)
map_c, map_f = using_map_filter(readings)


# Display cleaned readings
print("\nValid Temperatures in Celsius:", comp_c)
print("Temperatures in Fahrenheit:", comp_f)


# 4. Alarm minutes using enumerate()
alarm_minutes = [
    minute
    for minute, temp in enumerate(readings)
    if -50 <= temp <= 50 and not (2 <= temp <= 8)
]

print("\nAlarm Minutes:", alarm_minutes)


# 5. Dictionary comprehension
temperature_dict = {
    minute: temp
    for minute, temp in enumerate(readings)
    if -50 <= temp <= 50
}

print("\nTemperature Dictionary:", temperature_dict)


# 6. Set comprehension
temperature_set = {
    temp for temp in readings if -50 <= temp <= 50
}

print("\nUnique Valid Temperatures:", sorted(temperature_set))


# 7. Verify all three methods
print("\nVERIFICATION")
print("Loop and Comprehension:",
      loop_c == comp_c and loop_f == comp_f)

print("Loop and Map Filter:",
      loop_c == map_c and loop_f == map_f)


# 8. All-valid readings test
all_valid = [3, 4, 5, 6, 7]

print("\nALL VALID TEST:")
print(using_comprehension(all_valid))


# 9. All-invalid readings test
all_invalid = [55, 60, -55, -70]

print("\nALL INVALID TEST:")
print(using_comprehension(all_invalid))


# 10. Alternative: Generator expression
generator_result = (
    temp for temp in readings if -50 <= temp <= 50
)

print("\nGENERATOR EXPRESSION")
print("Valid readings:", list(generator_result))


# 11. Complexity
print("\nCOMPLEXITY")
print("Time Complexity: O(n)")
print("List Comprehension Space: O(n)")
print("Generator Additional Space: O(1)")
