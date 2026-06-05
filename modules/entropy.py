import math

def calculate_entropy(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26

    if any(c.isupper() for c in password):
        charset += 26

    if any(c.isdigit() for c in password):
        charset += 10

    if any(not c.isalnum() for c in password):
        charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)


if __name__ == "__main__":
    password = input("Enter Password: ")

    entropy = calculate_entropy(password)

    print(f"\nEntropy: {entropy} bits")

    if entropy < 40:
        print("Rating: Weak")
    elif entropy < 60:
        print("Rating: Medium")
    elif entropy < 80:
        print("Rating: Strong")
    else:
        print("Rating: Very Strong")
