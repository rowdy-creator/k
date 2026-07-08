import sys


def DivExp(a, b):
    
    assert a > 0, "Value of 'a' must be greater than 0"

  
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    c = a / b
    return c


try:
    
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))


    result = DivExp(a, b)
    print("Result (a,b) = ", result)

except AssertionError as ae:
    print("Assertion Error:", ae)

except ZeroDivisionError as zde:
    print("ZeroDivisionError:", zde)

except ValueError:
    print("Invalid input!")
