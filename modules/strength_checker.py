import re

def check_password_strength(password):
    score = 0
    recommendations = []

    if len(password) >= 12:
        score += 25
    else:
        recommendations.append("Use at least 12 characters")

    if re.search(r"[A-Z]", password):
        score += 20
    else:
        recommendations.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 20
    else:
        recommendations.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 15
    else:
        recommendations.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        recommendations.append("Add special characters")

    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    elif score < 90:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength, recommendations


if __name__ == "__main__":
    password = input("Enter Password: ")

    score, strength, recommendations = check_password_strength(password)

    print("\nPassword Analysis")
    print("-----------------")
    print("Score:", score, "/100")
    print("Strength:", strength)

    if recommendations:
        print("\nRecommendations:")
        for r in recommendations:
            print("-", r)
