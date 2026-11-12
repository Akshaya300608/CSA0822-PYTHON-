Run
import time

# Creating 200,000 items
items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]


# Method 1: Using +=
def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


# Method 2: Using join()
def build_join(parts):
    return ";".join(parts) + ";"


# Method 3: Using f-string for each line
def build_fstring(parts):
    return "".join(f"{p};" for p in parts)


# Measuring average execution time
def measure(function, data):
    total_time = 0

    for i in range(3):
        start = time.perf_counter()
        result = function(data)
        end = time.perf_counter()

        total_time += end - start

    average = total_time / 3
    return result, average


sizes = [1000, 10000, 200000]

print("MONTHLY SMS BILL STATEMENT")
print("----------------------------------------")

for size in sizes:
    data = items[:size]

    a, time_plus = measure(build_plus, data)
    b, time_join = measure(build_join, data)
    c, time_fstring = measure(build_fstring, data)

    print("\nNumber of items:", size)
    print("Same output:", a == b == c)
    print("String length:", len(a))
    print("+= Average time:", round(time_plus, 6), "seconds")
    print("join() Average time:", round(time_join, 6), "seconds")
    print("f-string Average time:", round(time_fstring, 6), "seconds")
9. ALTERNATIVE METHOD – USING io.StringIO
Instead of building the entire statement using += or join(), we can use StringIO to write the statement line by line.
Python
Run
from io import StringIO

def build_stringio(parts):
    output = StringIO()

    for p in parts:
        output.write(p + ";")

    return output.getvalue()


items = ["Item0:Rs0", "Item1:Rs1", "Item2:Rs2"]

result = build_stringio(items)

print(result)
