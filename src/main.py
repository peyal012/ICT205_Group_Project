# src/main.py
from math_operations import add, subtract, multiply, divide

def main():
    print("Simple Calculator")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    try:
        print(f"{a} / {b} = {divide(a, b)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
 
