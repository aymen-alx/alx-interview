#!/usr/bin/python3
""" cript that reads stdin line by line and computes metrics: """

import sys


def display_metrics(status_counts, total_size):
    """
    Display the computed metrics.
    """
    print("Total size:", total_size)
    for status_code, count in sorted(status_counts.items()):
        if count != 0:
            print(f"{status_code}: {count}")


def main():
    """
    Main function to process log data and compute metrics.
    """
    total_size = 0
    line_count = 0
    status_counts = {"200": 0, "301": 0, "400": 0, "401": 0,
                     "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            parsed_line = line.split()

            if len(parsed_line) >= 7:
                status_code = parsed_line[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1

                try:
                    file_size = int(parsed_line[-1])
                    total_size += file_size
                except ValueError:
                    pass

                line_count += 1

                if line_count == 10:
                    display_metrics(status_counts, total_size)
                    line_count = 0

    except KeyboardInterrupt:
        pass

    finally:
        display_metrics(status_counts, total_size)


if __name__ == "__main__":
    main()
