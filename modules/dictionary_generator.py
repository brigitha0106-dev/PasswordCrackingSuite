def leetspeak(word):
    replacements = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "5"
    }

    result = word.lower()

    for old, new in replacements.items():
        result = result.replace(old, new)

    return result


def generate_dictionary(name, dob, pet):

    name = name.lower()
    pet = pet.lower()

    words = set()

    base_words = [name, pet]

    for word in base_words:

        words.add(word)
        words.add(word.capitalize())
        words.add(word.upper())

        words.add(word + "123")
        words.add(word + "1234")
        words.add(word + dob)
        words.add(word + "2024")
        words.add(word + "2025")

        words.add(word + "@")
        words.add(word + "!")
        words.add(word + "#")

        words.add(leetspeak(word))

    words.add(name + pet)
    words.add(pet + name)

    words.add(name + dob)
    words.add(pet + dob)

    words.add(name + "@" + dob)
    words.add(pet + "@" + dob)

    words.add(name + "_" + pet)
    words.add(pet + "_" + name)

    return sorted(words)


if __name__ == "__main__":

    name = input("Enter Name: ")
    dob = input("Enter Birth Year: ")
    pet = input("Enter Pet Name: ")

    results = generate_dictionary(name, dob, pet)

    print("\nGenerated Password Candidates:\n")

    for word in results:
        print(word)

    print("\nSummary")
    print("--------")
    print("Total Candidates:", len(results))

    with open("sample_data/dictionary.txt", "w") as file:
        for word in results:
            file.write(word + "\n")

    print("\nDictionary saved to sample_data/dictionary.txt")
