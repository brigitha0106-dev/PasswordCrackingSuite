import math
from datetime import datetime


class BruteForceSimulator:

    GUESS_RATES = {
        "Basic CPU (1K/sec)": 1_000,
        "Modern CPU (1M/sec)": 1_000_000,
        "GPU Cluster (1B/sec)": 1_000_000_000
    }

    @staticmethod
    def calculate_keyspace(length, charset_size):

        return charset_size ** length

    @staticmethod
    def estimate_time(combinations, guesses_per_second):

        seconds = combinations / guesses_per_second

        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24
        years = days / 365

        return {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours,
            "days": days,
            "years": years
        }


def save_report(length, charset, combinations, results):

    filename = "sample_data/bruteforce_report.txt"

    with open(filename, "w") as file:

        file.write("BRUTE FORCE SIMULATION REPORT\n")
        file.write("=" * 60 + "\n")
        file.write(f"Generated: {datetime.now()}\n\n")

        file.write(f"Password Length : {length}\n")
        file.write(f"Character Set   : {charset}\n")
        file.write(f"Total Keyspace  : {combinations:,}\n\n")

        for machine, data in results.items():

            file.write(f"{machine}\n")
            file.write("-" * 40 + "\n")

            file.write(
                f"Years : {data['years']:.2f}\n"
            )

            file.write(
                f"Days  : {data['days']:.2f}\n\n"
            )

    return filename


if __name__ == "__main__":

    print("\nBRUTE FORCE SIMULATOR")
    print("=" * 60)

    length = int(input("Password Length: "))
    charset = int(input("Character Set Size: "))

    combinations = (
        BruteForceSimulator.calculate_keyspace(
            length,
            charset
        )
    )

    print("\nTotal Search Space")
    print("-" * 40)

    print(f"{combinations:,}")

    results = {}

    print("\nEstimated Crack Times")
    print("-" * 40)

    for machine, rate in BruteForceSimulator.GUESS_RATES.items():

        estimate = (
            BruteForceSimulator.estimate_time(
                combinations,
                rate
            )
        )

        results[machine] = estimate

        print(f"\n{machine}")

        print(
            f"Years: "
            f"{estimate['years']:.2f}"
        )

        print(
            f"Days : "
            f"{estimate['days']:.2f}"
        )

    report = save_report(
        length,
        charset,
        combinations,
        results
    )

    print("\nReport Saved:")
    print(report)
