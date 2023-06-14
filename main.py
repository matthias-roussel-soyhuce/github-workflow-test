"""Exemple Python code to test Pylint capabilities."""

from src.backend.functions import hello as hello_backend
from src.frontend.functions import hello as hello_frontend

def run_pylint_uncompliant_code():
    """
    Contains code that does not comply with Pylint checks.
    The associated Pylint message is indicated with each statement.
    """
    # Pylint performs some basic styles checks, for example ensure the max length
    # of each line (line-too-long)
    line_too_long = "This line is waaaaaaaaaaay waaaaaaaaaaaaaaaaaayyyyyyyyyyyyy toooooooooooooooooooo looooooooooooooooooooooong !!!!!"

    # Pylint also performs some style checks, which a formatter can help fix:
    # For example, there are 5 spaces at the and of the following line,
    # which raises trailing-whitespaces. A formatter like black can remove these spaces
    # automatically when saving the file.
    line_too_long = line_too_long * 2

    # But Pylint also suggests more advanced refactorings in order to keep the code
    # as Pythonic as possible.
    min([y**2 for y in list(range(10))])  # (consider-using-generator)

    # If Pylint raises a message that cannot be solved, we can disable this message.
    # It is possible to disable messages at different scopes :

    # 1. On a single line:
    try:
        impossible_sum = line_too_long + 2
    except:  # pylint: disable=bare-except
        print("Error !")

    # 2. On the next line:
    numbers = [
        1,
        1,
        2,
        2,
    ]  # pylint: disable-next=unnecessary-comprehension
    unique_numbers = {number for number in numbers}

    # 3. Inside a block of code:
    for number in (0, 1, 2, 3, 4, 5):
        # pylint:disable=consider-using-in

        # The following line should raise consider-using-in but it is disabled in the whole block
        if number == 1 or number == 2:
            print("The number is 1 or 2.")

        # The following line should raise consider-using-in but it is disabled in the whole block
        if number == 3 or number == 4:
            print("The number is 3 or 4.")

    # 4. Project-wide, in the pyproject.toml config file:
    # This line should raise the Pylint message unused-variable, but it has been disabled 
    # project-wide in the config.
    some_unused_variable = 5


def main():
    """Main function."""
    run_pylint_uncompliant_code()
    hello_backend()
    hello_frontend()


if __name__ == "__main__":
    main()
