"""Exemple Python code to test Pylint capabilities."""


def run_pylint_uncompliant_code():
    """
    Contains code that does not comply with Pylint checks.
    The associated Pylint message is indicated with each statement.
    """
    # Pylint performs some basic styles checks, for example :
    # Ensure the max length of each line (line-too-long), or that no variable
    # is unused (unused-variable)
    line_too_long = "This line is waaaaaaaaaaay waaaaaaaaaaaaaaaaaayyyyyyyyyyyyy toooooooooooooooooooo looooooooooooooooooooooong !!!!!"

    # Pylint also performs some style checks, which a formatter can help fix:
    # For example, there are 5 spaces at the and of the following line,
    # which raises trailing-whitespaces. A formatter like black can remove these spaces
    # automatically when saving the file.
    line_too_long = line_too_long * 2     

    # But Pylint also suggests more advanced refactorings in order to keep the code
    # as Pythonic as possible.
    min([y**2 for y in list(range(10))])  # (consider-using-generator)

    # Some Pylint checks can be disabled project-wide (cf. the config in pyproject.toml),
    # but we can also disable checks on specific code portions:

    # On a single line
    some_usunsed_variable = 6  # pylint: disable=unused-variable

    # On the next line
    numbers = [
        1,
        1,
        2,
        2,
    ]  # pylint: disable-next=unnecessary-comprehension,unused-variable
    unique_numbers = {number for number in numbers}

    # Inside a block of code
    for number in (0, 1, 2, 3, 4, 5):
        # pylint:disable=consider-using-in

        # The following line should raise consider-using-in but it is disabled in the whole block
        if number == 1 or number == 2:
            print("The number is 1 or 2.")

        # The following line should raise consider-using-in but it is disabled in the whole block
        if number == 3 or number == 4:
            print("The number is 3 or 4.")


def main():
    """Main function."""
    run_pylint_uncompliant_code()


if __name__ == "__main__":
    main()
