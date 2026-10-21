from decimal import Decimal
import sys
 
payments = ["33.40"] * 1000 + ["0.10"] * 3
 
def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total
 
def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total
 
print("Types:")
for value in (10, 10.0, "10", True, [10, 8.5]):
    print(value, type(value).__name__)
 
print("\nDivision examples:")
print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)
print("-7 // 2 =", -7 // 2)
 
print("\nMoney comparison:")
print("float :", total_float(payments))
print("Decimal:", total_decimal(payments))
print(0.1 + 0.2 == 0.3,
      Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
 
print("\nObject sizes:")
print("float object:", sys.getsizeof(10.0), "bytes")
print("Decimal object:", sys.getsizeof(Decimal("10.00")), "bytes")
