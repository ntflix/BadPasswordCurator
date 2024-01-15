from enum import Enum
import re


class PasswordRequirement(Enum):
    LOWERCASE = ("lowercase", re.compile(r"[a-z]"))
    UPPERCASE = ("uppercase", re.compile(r"[A-Z]"))
    NUMERIC = ("numeric", re.compile(r"\d"))
    SPECIAL_CHAR = ("specialChar", re.compile(r"\W"))

    def __str__(self):
        return self.value[0]

    def __repr__(self):
        return str(self)

    @property
    def regex(self):
        return self.value[1]

    def __hash__(self):
        return hash(str(self))

    @staticmethod
    def from_string(string: str):
        for req in PasswordRequirement:
            if str(req) == string:
                return req
        raise ValueError(f"Invalid password requirement: {string}")


class PasswordRequirements:
    requirements: set[PasswordRequirement] = set()

    def __init__(
        self, min_length: int, requirements: dict[str, bool], min_req_count: int
    ):
        self.min_length = min_length
        self.min_req_count = min_req_count
        for req, value in requirements.items():
            if value:
                self.requirements.add(PasswordRequirement.from_string(req))


def create_password_requirements(
    reqs: dict[str, bool | dict[str, bool] | int]
) -> PasswordRequirements:
    assert type(reqs) == dict
    assert type(reqs["minLength"]) == int
    assert type(reqs["minReqCount"]) == int
    assert type(reqs["requirements"]) == dict
    assert all(
        type(value) == bool for value in reqs["requirements"].values()
    ), "All values in requirements must be boolean"

    min_length: int = reqs["minLength"]
    min_req_count: int = reqs["minReqCount"]
    requirements: dict[str, bool] = reqs["requirements"]
    return PasswordRequirements(min_length, requirements, min_req_count)
