class HashExtractor:

    @staticmethod
    def extract(filepath):

        hashes = []

        with open(filepath, "r") as file:

            for line in file:

                line = line.strip()

                if line:
                    hashes.append(line)

        return hashes


if __name__ == "__main__":

    filepath = input(
        "Enter hash file path: "
    )

    hashes = HashExtractor.extract(
        filepath
    )

    print("\nExtracted Hashes")

    print("-" * 40)

    for hash_value in hashes:

        print(hash_value)

    print(
        f"\nTotal Hashes: {len(hashes)}"
    )
