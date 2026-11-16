# HARSHITH G
# 25BTRAD040
# PYTHON PROGRAMMING
# MINI PROJECT: Unit Converter or Bill Generator

# ---------------------------------------------------------------
# 1. Unit Converter
# ---------------------------------------------------------------
print("===== UNIT CONVERTER =====")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))
value = float(input("Enter the value: "))

if choice == 1:
    print("Miles =", value * 0.621371)
elif choice == 2:
    print("Kilometers =", value * 1.60934)
elif choice == 3:
    print("Fahrenheit =", (value * 9 / 5) + 32)
elif choice == 4:
    print("Celsius =", (value - 32) * 5 / 9)
else:
    print("Invalid choice")

# ---------------------------------------------------------------
# 2. Bill Generator
# ---------------------------------------------------------------
print("\n===== BILL GENERATOR =====")

item1 = input("Enter item 1: ")
price1 = float(input("Enter price: "))

item2 = input("Enter item 2: ")
price2 = float(input("Enter price: "))

item3 = input("Enter item 3: ")
price3 = float(input("Enter price: "))

total = price1 + price2 + price3
gst = total * 0.05
grand_total = total + gst

print("\n===== BILL =====")
print(item1, ":", price1)
print(item2, ":", price2)
print(item3, ":", price3)
print("--------------------")
print("Subtotal :", total)
print("GST (5%) :", gst)
print("Total Bill :", grand_total)
print("====================")
