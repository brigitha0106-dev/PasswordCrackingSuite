from modules.password_auditor import (
    PasswordAuditor
)

from modules.report_generator import (
    ReportGenerator
)


def menu():

    print("\n")

    print(
        "PASSWORD CRACKING & "
        "CREDENTIAL ATTACK SUITE"
    )

    print("=" * 60)

    print("1. Password Audit")

    print("2. Exit")

    choice = input(
        "\nSelect Option: "
    )

    return choice


while True:

    option = menu()

    if option == "1":

        password = input(
            "\nEnter Password: "
        )

        result = (
            PasswordAuditor.audit(
                password
            )
        )

        print("\nAUDIT RESULT")

        print("=" * 40)

        for key, value in result.items():

            print(
                f"{key}: {value}"
            )

        pdf = (
            ReportGenerator.generate(
                result
            )
        )

        print(
            f"\nReport Saved: {pdf}"
        )

    elif option == "2":

        print(
            "\nExiting Toolkit..."
        )

        break

    else:

        print(
            "\nInvalid Option"
        )
