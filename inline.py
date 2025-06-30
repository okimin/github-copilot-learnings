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

def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted lists into a single sorted list."""
    merged = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    # Append any remaining elements from either list
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

# Edge case 1: Both lists are empty
print("Merging two empty lists:", merge_sorted([], []))

# Edge case 2: One list is empty, the other is non-empty
print("Merging empty and non-empty list:", merge_sorted([], [1, 2, 3]))

# Edge case 3: Lists with duplicate elements
print("Merging lists with duplicates:", merge_sorted([1, 2, 2, 3], [2, 3, 4])) 

# Edge case 4: Lists with all elements in one list smaller than the other
print("Merging lists with all elements in one list smaller:", merge_sorted([1, 2, 3], [4, 5, 6]))

# Edge case 5: Lists with all elements in one list larger than the other
print("Merging lists with all elements in one list larger:", merge_sorted([4, 5, 6], [1, 2, 3]))

# Edge case 6: Lists with different lengths
print("Merging lists with different lengths:", merge_sorted([1, 2], [3, 4, 5]))


zzz = [q for q in range(2, 100) if all(q % w for w in range(2, int(q**0.5) + 1))]
print(zzz[:10])