import json
from requirements import create_password_requirements
from requirements import PasswordRequirements


def load_password_requirements(file_name: str) -> PasswordRequirements:
    with open(file_name, "r") as file:
        reqs_json = json.load(file)

    try:
        return create_password_requirements(reqs_json)
    except (KeyError, AssertionError, ValueError) as e:
        raise ValueError("Invalid password requirements JSON") from e
