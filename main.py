from text_handler import PasswordFileProcessor
from requirements_loader import load_password_requirements

reqs = load_password_requirements("password_requirements.json")
processor = PasswordFileProcessor(reqs, "PwnedPasswordsTop100k.txt", "curated-100k.txt")
processor.process()
