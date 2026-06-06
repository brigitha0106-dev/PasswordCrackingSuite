from datetime import datetime


class ShadowParser:

    ALGORITHMS = {
        "$1$": "MD5",
        "$5$": "SHA256",
        "$6$": "SHA512"
    }

    @staticmethod
    def identify_algorithm(hash_field):

        for identifier, algorithm in ShadowParser.ALGORITHMS.items():

            if hash_field.startswith(identifier):
                return algorithm

        return "Unknown"


def parse_shadow_file(filepath):

    entries = []

    with open(filepath, "r") as file:

        for line in file:

            parts = line.strip().split(":")

            username = parts[0]
            password_hash = parts[1]

            algorithm = (
                ShadowParser.identify_algorithm(
                    password_hash
                )
            )

            entries.append({
                "username": username,
                "algorithm": algorithm,
                "hash": password_hash
            })

    return entries


def save_report(entries):

    filename = "sample_data/shadow_analysis_report.txt"

    with open(filename, "w") as file:

        file.write("SHADOW FILE ANALYSIS REPORT\n")
        file.write("=" * 60 + "\n")
        file.write(f"Generated: {datetime.now()}\n\n")

        for entry in entries:

            file.write(
                f"User      : {entry['username']}\n"
            )

            file.write(
                f"Algorithm : {entry['algorithm']}\n"
            )

            file.write(
                f"Hash      : {entry['hash'][:30]}...\n"
            )

            file.write("-" * 40 + "\n")

    return filename


if __name__ == "__main__":

    print("\nLINUX SHADOW FILE PARSER")
    print("=" * 60)

    filepath = "sample_data/sample_shadow.txt"

    entries = parse_shadow_file(filepath)

    print("\nAnalysis Results")
    print("-" * 40)

    for entry in entries:

        print(
            f"{entry['username']} "
            f"→ {entry['algorithm']}"
        )

    report = save_report(entries)

    print("\nReport Saved:")
    print(report)
