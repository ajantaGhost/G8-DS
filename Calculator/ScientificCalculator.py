import sys

# --- 1. Basic Arithmetic Operations ---
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error: Division by zero" if b == 0 else a / b
def modulus(a, b): return "Error: Modulus by zero" if b == 0 else a % b

# --- 2. Advanced Mathematical Functions ---
def power(a, b): return a ** b
def square_root(n): return "Error: Negative number" if n < 0 else n ** 0.5

def factorial(n):
    if n < 0:
        return "Error: Negative input"
    elif n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def exponential(x):
    # Approximate e^x using Taylor series (first 15 terms)
    result = 1.0
    term = 1.0
    for i in range(1, 15):
        term *= x / i
        result += term
    return result

def natural_log(x, iterations=1000):
    if x <= 0:
        return "Error: Invalid input"
    result = 0.0
    y = (x - 1) / (x + 1)
    for i in range(1, iterations * 2, 2):
        result += (1 / i) * (y ** i)
    return 2 * result

def log_base_10(x):
    ln10 = 2.302585093  # Approx value of ln(10)
    ln_x = natural_log(x)
    return "Error" if isinstance(ln_x, str) else ln_x / ln10

def sin(x):  # x in radians
    x = x % (2 * 3.14159)
    term = x
    result = x
    for i in range(1, 10):
        term *= -1 * x * x / ((2 * i) * (2 * i + 1))
        result += term
    return result

def cos(x):  # x in radians
    x = x % (2 * 3.14159)
    term = 1
    result = 1
    for i in range(1, 10):
        term *= -1 * x * x / ((2 * i - 1) * (2 * i))
        result += term
    return result

def tan(x):
    cosine = cos(x)
    return "Error: tan undefined" if cosine == 0 else sin(x) / cosine

# --- 3. Number System Conversions ---
def decimal_to_binary(n): return bin(n)[2:]
def decimal_to_octal(n): return oct(n)[2:]
def decimal_to_hex(n): return hex(n)[2:]
def binary_to_decimal(s): return int(s, 2)
def octal_to_decimal(s): return int(s, 8)
def hex_to_decimal(s): return int(s, 16)

# --- 4. Angle and Unit Handling ---
def deg_to_rad(deg): return deg * (3.14159 / 180)
def rad_to_deg(rad): return rad * (180 / 3.14159)

# --- 5. Constants ---
PI = 3.14159
E = 2.71828

# --- Menu Display ---
def display_menu():
    print("\n===== SCIENTIFIC CALCULATOR MENU =====")
    print("1. Basic Arithmetic")
    print("2. Advanced Math Functions")
    print("3. Number System Conversion")
    print("4. Angle Conversion")
    print("5. Constants (π, e)")
    print("0. Exit")

def basic_arithmetic_menu():
    print("\n-- BASIC ARITHMETIC OPERATIONS --")
    print("1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. Modulus")
    choice = int(input("Choose operation: "))
    a, b = float(input("Enter first number: ")), float(input("Enter second number: "))
    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", subtract(a, b))
    elif choice == 3:
        print("Result:", multiply(a, b))
    elif choice == 4:
        print("Result:", divide(a, b))
    elif choice == 5:
        print("Result:", modulus(a, b))
    else:
        print("Invalid operation.")

def advanced_functions_menu():
    print("\n-- ADVANCED MATH FUNCTIONS --")
    print("1. Power | 2. Square Root | 3. Factorial | 4. Exponential")
    print("5. Natural Log | 6. Log Base 10 | 7. sin | 8. cos | 9. tan")
    choice = int(input("Choose operation: "))
    if choice == 1:
        a, b = float(input("Base: ")), float(input("Exponent: "))
        print("Result:", power(a, b))
    elif choice == 2:
        n = float(input("Enter number: "))
        print("Result:", square_root(n))
    elif choice == 3:
        n = int(input("Enter integer: "))
        print("Result:", factorial(n))
    elif choice == 4:
        x = float(input("Enter x: "))
        print("Result:", exponential(x))
    elif choice == 5:
        x = float(input("Enter x: "))
        print("Result:", natural_log(x))
    elif choice == 6:
        x = float(input("Enter x: "))
        print("Result:", log_base_10(x))
    elif choice in [7, 8, 9]:
        angle = float(input("Enter angle in degrees: "))
        rad = deg_to_rad(angle)
        if choice == 7:
            print("sin:", sin(rad))
        elif choice == 8:
            print("cos:", cos(rad))
        elif choice == 9:
            print("tan:", tan(rad))
    else:
        print("Invalid operation.")

def number_conversion_menu():
    print("\n-- NUMBER SYSTEM CONVERSION --")
    print("1. Decimal to Binary/Octal/Hex")
    print("2. Binary/Octal/Hex to Decimal")
    choice = int(input("Choose conversion: "))
    if choice == 1:
        n = int(input("Enter decimal number: "))
        print("Binary:", decimal_to_binary(n))
        print("Octal:", decimal_to_octal(n))
        print("Hex:", decimal_to_hex(n))
    elif choice == 2:
        base = input("Enter base (bin/oct/hex): ").lower()
        s = input("Enter number: ")
        if base == "bin":
            print("Decimal:", binary_to_decimal(s))
        elif base == "oct":
            print("Decimal:", octal_to_decimal(s))
        elif base == "hex":
            print("Decimal:", hex_to_decimal(s))
        else:
            print("Invalid base.")
    else:
        print("Invalid choice.")

def angle_conversion_menu():
    print("\n-- ANGLE CONVERSION --")
    print("1. Degrees to Radians | 2. Radians to Degrees")
    choice = int(input("Choose option: "))
    if choice == 1:
        deg = float(input("Enter degrees: "))
        print("Radians:", deg_to_rad(deg))
    elif choice == 2:
        rad = float(input("Enter radians: "))
        print("Degrees:", rad_to_deg(rad))
    else:
        print("Invalid choice.")

def constants_menu():
    print("\n-- CONSTANTS AND SPECIAL VALUES --")
    print("π (pi):", PI)
    print("e (Euler's number):", E)

# --- Main Program ---
while True:
    try:
        display_menu()
        opt = int(input("Enter your choice: "))
        if opt == 0:
            print("Thank you for using the calculator.")
            sys.exit()
        elif opt == 1:
            basic_arithmetic_menu()
        elif opt == 2:
            advanced_functions_menu()
        elif opt == 3:
            number_conversion_menu()
        elif opt == 4:
            angle_conversion_menu()
        elif opt == 5:
            constants_menu()
        else:
            print("Invalid main menu choice.")
    except Exception as e:
        print("Error:", e)
