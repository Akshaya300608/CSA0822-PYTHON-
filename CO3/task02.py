# Tuple as dictionary key
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print("BUS STOP DETAILS")
for (lat, lon), name in stops.items():
    print(name, lat, lon)


# Incorrect grid
rows, cols = 3, 4

bad = [[0] * cols] * rows
bad[0][1] = 7

# Correct grid
good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7

print("\nGRID COMPARISON")
print("bad :", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])


# Aliasing
original = [10, 20, 30]
alias = original
alias.append(40)

print("\nALIASING")
print("Original:", original)
print("Alias:", alias)
print("Same object:", original is alias)


# Shallow copy using slicing
shallow = original[:]

print("\nSHALLOW COPYING")
print("Original:", original)
print("Shallow copy:", shallow)
print("Same object:", original is shallow)


# Deep copy demonstration without importing copy
data = [[1, 2], [3, 4]]

deep = [row[:] for row in data]
deep[0][0] = 99

print("\nDEEP COPY")
print("Original:", data)
print("Deep copy:", deep)


# Tuple unpacking
print("\nTUPLE UNPACKING")
for (lat, lon), name in stops.items():
    print(name, lat, lon)


# List as dictionary key
print("\nLIST AS DICTIONARY KEY")

try:
    sample = {[13.0418, 80.2341]: "T. Nagar"}
except TypeError:
    print("TypeError: List cannot be used as dictionary key")


# List and tuple memory comparison
print("\nMEMORY COMPARISON")

numbers_list = list(range(1000))
numbers_tuple = tuple(range(1000))

print("List length:", len(numbers_list))
print("Tuple length:", len(numbers_tuple))


# List inside tuple
student = ("Akshaya", [80, 90, 85])
student[1].append(95)

print("\nLIST INSIDE TUPLE")
print(student)
