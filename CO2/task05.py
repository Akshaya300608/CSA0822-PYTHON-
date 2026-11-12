Python
Run
# Mutable default argument problem


# Global variable
count = 10

def global_example():
    global count
    count = count + 5
    print("Global count:", count)


# Nonlocal variable
def nonlocal_example():
    number = 10

    def change_number():
        nonlocal number
        number = number + 5

    change_number()
    print("Nonlocal number:", number)


# Testing buggy function
print("BUGGY FUNCTION:")
print(add_item_buggy("Tea"), add_item_buggy("Vada"))

print("Default values:", add_item_buggy.__defaults__)


# Testing corrected function
print("\nCORRECTED FUNCTION:")
print(add_item("Tea"), add_item("Vada"))


# Three independent customer orders
print("\nCUSTOMER ORDERS:")

customer1 = add_item("Tea")
customer2 = add_item("Vada")
customer3 = add_item("Coffee")

print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)


# Bill calculation
total, gst = calculate_bill(200)

print("\nBILL DETAILS:")
print("GST:", gst)
print("Total Amount:", total)


# Scope demonstrations
print("\nVARIABLE SCOPE:")
local_example()
global_example()
nonlocal_example()
9. ALTERNATIVE METHOD – PASSING THE LIST EXPLICITLY
Instead of using None as the default parameter, we can create a separate list for each customer and pass it directly to the function.
Python
Run
def add_item(item, order):
    order.append(item)
    return order


customer1 = []
customer2 = []
customer3 = []

add_item("Tea", customer1)
add_item("Vada", customer2)
add_item("Coffee", customer3)

print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)
