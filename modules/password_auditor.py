from modules.strength_checker import check_password_strength
from modules.entropy import calculate_entropy


class PasswordAuditor:

    COMMON_PASSWORDS = {
        "password",
        "password123",
        "admin",
        "admin123",
        "welcome",
        "welcome123",
        "123456",
        "qwerty"
    }

    @staticmethod
    def check_dictionary_file(password):

        try:

            with open(
                "sample_data/dictionary.txt",
                "r"
            ) as file:

                words = {
                    line.strip().lower()
                    for line in file
                }

                return (
                    password.lower()
                    in words
                )

        except FileNotFoundError:

            return False

    @staticmethod
    def audit(password):

        score, strength, recommendations = (
            check_password_strength(password)
        )

        entropy = calculate_entropy(password)

        common_match = (
            password.lower()
            in PasswordAuditor.COMMON_PASSWORDS
        )

        generated_match = (
            PasswordAuditor.check_dictionary_file(
                password
            )
        )

        dictionary_match = (
            common_match
            or generated_match
        )

        if common_match:

            risk = "CRITICAL"
            match_source = "Common Password List"

        elif generated_match:

            risk = "HIGH"
            match_source = "Generated Dictionary"

        elif entropy < 40:

            risk = "HIGH"
            match_source = "No Match"

        elif entropy < 60:

            risk = "MEDIUM"
            match_source = "No Match"

        else:

            risk = "LOW"
            match_source = "No Match"

        password_length = len(password)

        return {

            "password_length": password_length,

            "score": score,

            "strength": strength,

            "entropy": entropy,

            "dictionary_match": dictionary_match,

            "match_source": match_source,

            "risk": risk,

            "recommendations": recommendations

        }
