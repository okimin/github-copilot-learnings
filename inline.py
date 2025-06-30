import math

# Utility functions for math operations
def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius**2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Area of a circle with radius 5:", calculate_area(5))
print("Fibonacci sequence up to 10:", [fibonacci(i) for i in range(11)])