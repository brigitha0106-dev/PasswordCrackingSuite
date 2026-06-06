from strength_checker import check_password_strength
from entropy import calculate_entropy


class PasswordAuditor:

    COMMON_PASSWORDS = {
        "password",
        "password123",
        "admin",
        "admin123",
        "welcome",
        "123456",
        "qwerty"
    }

    @staticmethod
    def audit(password):

        score, strength, recommendations = (
            check_password_strength(password)
        )

        entropy = calculate_entropy(
            password
        )

        dictionary_match = (
            password.lower()
            in PasswordAuditor.COMMON_PASSWORDS
        )

        if dictionary_match:
            risk = "HIGH"

        elif entropy < 50:
            risk = "MEDIUM"

        else:
            risk = "LOW"

        return {

            "score": score,

            "strength": strength,

            "entropy": entropy,

            "dictionary_match":
                dictionary_match,

            "risk": risk,

            "recommendations":
                recommendations
        }
