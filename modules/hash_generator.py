import hashlib
from datetime import datetime


class HashGenerator:

    @staticmethod
    def generate_hashes(password):

        hashes = {
            "MD5": hashlib.md5(password.encode()).hexdigest(),
            "SHA1": hashlib.sha1(password.encode()).hexdigest(),
            "SHA256": hashlib.sha256(password.encode()).hexdigest(),
            "SHA512": hashlib.sha512(password.encode()).hexdigest()
        }

        return hashes


def save_hash_report(password, hashes):

    filename = "sample_data/generated_hashes.txt"

    with open(filename, "w") as file:

        file.write("PASSWORD HASH ANALYSIS REPORT\n")
        file.write("=" * 50 + "\n")
        file.write(f"Generated: {datetime.now()}\n\n")

        file.write(f"Original Password Length: {len(password)}\n\n")

        for algorithm, value in hashes.items():

            file.write(f"[{algorithm}]\n")
            file.write(f"Hash Length : {len(value)}\n")
            file.write(f"Hash Value  : {value}\n\n")

    return filename


if __name__ == "__main__":

    print("\nPASSWORD HASH GENERATOR")
    print("=" * 50)

    password = input("Enter Password: ")

    hashes = HashGenerator.generate_hashes(password)

    print("\nGenerated Hashes")
    print("-" * 50)

    for algorithm, value in hashes.items():

        print(f"\n{algorithm}")
        print(f"Length : {len(value)}")
        print(f"Hash   : {value}")

    report = save_hash_report(password, hashes)

    print("\nReport Saved:")
    print(report)
