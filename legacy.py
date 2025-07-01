'''
Context
I have a short COBOL program OLDADD in legacy.cbl that adds two 4‑digit numbers read from STDIN and prints the result.

Instruction
Convert this program to modern Python 3.12.

Constraints
• Use functions, no global input() calls.
• Keep it under 25 lines.
• Include type hints and a brief docstring.

Persona
Act as a seasoned Python developer.

Style
Google‑style docstring; follow PEP‑8.
'''


def add_two_numbers(a: int, b: int) -> int:
    """Add two 4-digit integers and return the sum.

    Args:
        a (int): First 4-digit integer.
        b (int): Second 4-digit integer.

    Returns:
        int: The sum of a and b.
    """
    return a + b


def main() -> None:
    """Prompt for two 4-digit numbers, add them, and display the result."""
    a = int(input("Enter first 4-digit number: "))
    b = int(input("Enter second 4-digit number: "))
    result = add_two_numbers(a, b)
    print(result)


if __name__ == "__main__":
    main()