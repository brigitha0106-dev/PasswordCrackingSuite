from datetime import datetime


class HashIdentifier:

    HASH_TYPES = {
        32: ["MD5", "NTLM"],
        40: ["SHA1"],
        64: ["SHA256"],
        128: ["SHA512"]
    }

    RISK_LEVELS = {
        "MD5": "HIGH",
        "NTLM": "HIGH",
        "SHA1": "MEDIUM",
        "SHA256": "LOW",
        "SHA512": "LOW"
    }

    @staticmethod
    def identify(hash_value):

        length = len(hash_value)

        possible_algorithms = HashIdentifier.HASH_TYPES.get(
            length,
            ["Unknown"]
        )

        return {
            "hash": hash_value,
            "length": length,
            "algorithms": possible_algorithms
        }


def generate_report(result):

    filename = "sample_data/hash_analysis_report.txt"

    with open(filename, "w") as file:

        file.write("HASH ANALYSIS REPORT\n")
        file.write("=" * 50 + "\n")
        file.write(f"Generated: {datetime.now()}\n\n")

        file.write(f"Hash Value : {result['hash']}\n")
        file.write(f"Length     : {result['length']}\n\n")

        file.write("Possible Algorithms:\n")

        for algo in result["algorithms"]:

            file.write(f"- {algo}\n")

            if algo != "Unknown":
                file.write(
                    f"  Risk Level: "
                    f"{HashIdentifier.RISK_LEVELS.get(algo)}\n"
                )

        file.write("\nRecommendations:\n")

        if "MD5" in result["algorithms"] or \
           "NTLM" in result["algorithms"]:

            file.write(
                "- Upgrade to SHA256 or SHA512\n"
            )

        elif "SHA1" in result["algorithms"]:

            file.write(
                "- SHA1 is deprecated for security-critical use\n"
            )

        else:

            file.write(
                "- Algorithm appears reasonably secure\n"
            )

    return filename


if __name__ == "__main__":

    print("\nHASH IDENTIFIER")
    print("=" * 50)

    hash_value = input("Enter Hash: ").strip()

    result = HashIdentifier.identify(hash_value)

    print("\nHash Analysis")
    print("-" * 50)

    print(f"Length: {result['length']}")

    print("\nPossible Algorithms:")

    for algo in result["algorithms"]:

        print(f"- {algo}")

        if algo != "Unknown":

            print(
                f"  Risk Level: "
                f"{HashIdentifier.RISK_LEVELS.get(algo)}"
            )

    report = generate_report(result)

    print("\nReport Saved:")
    print(report)
