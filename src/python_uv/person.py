"""Simple greeting function and Person class."""


# --- Function ---
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


# --- Class ---
class Person:
    """A simple class representing a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> str:
        """Introduce the person."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
