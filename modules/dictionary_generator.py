def generate_dictionary(name, dob, pet):
    words = []

    name = name.lower()
    pet = pet.lower()

    words.extend([
        name,
        pet,
        name + dob,
        pet + dob,
        name + "123",
        pet + "123",
        name + "@" + dob,
        pet + "@" + dob,
        name + pet,
        pet + name,
        name.capitalize() + dob,
        pet.capitalize() + dob
    ])

    return sorted(set(words))


if __name__ == "__main__":
    name = input("Enter Name: ")
    dob = input("Enter Birth Year: ")
    pet = input("Enter Pet Name: ")

    results = generate_dictionary(name, dob, pet)

    print("\nGenerated Password Candidates:\n")

    for word in results:
        print(word)
