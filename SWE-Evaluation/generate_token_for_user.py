# Replace with actual script filename
from google_docs_script import get_services


def generate_token_as(token_filename):
    get_services(token_file=token_filename)
    print(f"Token saved as: {token_filename}")


if __name__ == "__main__":
    email = input("Enter email (e.g. evalswe02): ").strip()
    token_filename = f"token_{email}.json"
    generate_token_as(token_filename)
