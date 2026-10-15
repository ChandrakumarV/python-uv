"""Simple math functions and a basic Calculator class."""


# --- Functions ---
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


# --- Class ---
class Calculator:
    """A simple calculator class."""

    def __init__(self, brand: str = "Casio") -> None:
        self.brand = brand

    def describe(self) -> str:
        """Return a description of the calculator."""
        return f"This is a {self.brand} calculator."
