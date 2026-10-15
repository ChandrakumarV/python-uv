"""A beginner-friendly project demonstrating Python functions and classes."""

from python_uv.calculator import Calculator, add, multiply
from python_uv.person import Person, greet


def main() -> None:
    print("--- Python UV Demo ---")

    # 1. Using functions
    message = greet("Alice")
    print(message)

    sum_result = add(5, 3)
    print("5 + 3 =", sum_result)

    product_result = multiply(4, 2)
    print("4 * 2 =", product_result)

    # 2. Using classes
    person = Person(name="Bob", age=25)
    print(person.introduce())

    calc = Calculator(brand="Casio")
    print(calc.describe())


if __name__ == "__main__":
    main()
