# HARSHITH G
# 25BTRAD040
# Python Programming
# Lab Experiment - 1

# ---------------------------------------------------------------
# Lab Exercise 1: Installing Python, Setting up VS Code / PyCharm,
# Jupyter Notebook
# (Theory only - no code. Verify install with: python --version)
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Lab Exercise 2: Write and execute a basic Python program
# ---------------------------------------------------------------
print("----- Lab Exercise 2 -----")

name = "harshith"
print("My name is", name)

a = 10
b = 20
sum = a + b
print("First number:", a)
print("Second number:", b)
print("Sum:", sum)

# ---------------------------------------------------------------
# Lab Exercise 3: Programs using variables, operators, and input/output
# ---------------------------------------------------------------
print("\n----- Lab Exercise 3 -----")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
print("Product =", a * b)

# Simple Interest
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100
print("Simple Interest =", si)

# ---------------------------------------------------------------
# Lab Exercise 4: Simple calculator and area calculation programs
# ---------------------------------------------------------------
print("\n----- Lab Exercise 4 -----")

# Simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)

# Area of circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area of circle =", area)
