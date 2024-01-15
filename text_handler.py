from requirements import PasswordRequirements
from matcher import is_valid_password


class PasswordFileProcessor:
    def __init__(
        self,
        requirements: PasswordRequirements,
        input_file_name: str,
        output_file_name: str,
    ):
        self.requirements = requirements
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    def process(self):
        with open(
            self.input_file_name, "r", encoding="iso-8859-1", errors="ignore"
        ) as input_file, open(self.output_file_name, "w") as output_file:
            for line in input_file:
                password = line.strip()
                if is_valid_password(password, self.requirements):
                    output_file.write(password + "\n")
