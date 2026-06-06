import os

from modules.password_auditor import PasswordAuditor
from modules.report_generator import ReportGenerator


def clear():
    os.system("clear")


def pause():
    input("\nPress Enter to continue...")


def password_audit():

    password = input("\nEnter Password: ")

    result = PasswordAuditor.audit(password)

    print("\nAUDIT RESULTS")
    print("=" * 50)

    for key, value in result.items():
        print(f"{key}: {value}")

    pdf = ReportGenerator.generate(result)

    print(f"\nReport Saved: {pdf}")

    pause()


def dictionary_generator():

    os.system(
        "python modules/dictionary_generator.py"
    )

    pause()


def hash_generator():

    os.system(
        "python modules/hash_generator.py"
    )

    pause()


def hash_identifier():

    os.system(
        "python modules/hash_identifier.py"
    )

    pause()


def brute_force():

    os.system(
        "python modules/bruteforce_simulator.py"
    )

    pause()


def shadow_parser():

    os.system(
        "python modules/shadow_parser.py"
    )

    pause()


def hash_extractor():

    os.system(
        "python modules/hash_extractor.py"
    )

    pause()


while True:

    clear()

    print("=" * 60)
    print("PASSWORD CRACKING & CREDENTIAL ATTACK SUITE")
    print("=" * 60)

    print("1. Password Audit")
    print("2. Dictionary Generator")
    print("3. Hash Generator")
    print("4. Hash Identifier")
    print("5. Brute Force Simulator")
    print("6. Shadow Parser")
    print("7. Hash Extractor")
    print("8. Exit")

    choice = input("\nSelect Option: ")

    if choice == "1":
        password_audit()

    elif choice == "2":
        dictionary_generator()

    elif choice == "3":
        hash_generator()

    elif choice == "4":
        hash_identifier()

    elif choice == "5":
        brute_force()

    elif choice == "6":
        shadow_parser()

    elif choice == "7":
        hash_extractor()

    elif choice == "8":

        print("\nExiting Toolkit...")
        break

    else:

        print("\nInvalid Option")
        pause()
