from requirements import PasswordRequirement, PasswordRequirements


def is_valid_password(
    password: str,
    reqs: PasswordRequirements,
) -> bool:
    """
    - We use regular expressions to check if the password meets each condition (lowercase, uppercase, numeric, special character).
    - We then iterate over each condition, and if a condition is `True` in `reqs['requirements']` and the password satisfies this condition, we increment `fulfilled`.
    - The function finally returns `True` if the password meets the minimum length and minimum requirement count.

    This function expects `password` as a string and `reqs` as a dictionary following the schema. It will return `True` if the password meets the requirements and `False` otherwise. The requirements will be represented in Python as a dictionary which can be easily translated from the JSON criteria.

    **Disclaimer:** Regular expressions and Python's built-in string methods(Processed through the `re` module) are cpu-intensive tasks, for very long strings and/or a large number of criteria these could take a sizable amount of time to complete. It's worth keeping this in mind given the scale and use-case of your system.
    """

    if len(password) < reqs.min_length:
        return False

    fulfilled = 0
    for requirement in PasswordRequirement:
        if requirement in reqs.requirements and requirement.regex.search(password):
            fulfilled += 1

    if fulfilled < reqs.min_req_count:
        return False

    return True
