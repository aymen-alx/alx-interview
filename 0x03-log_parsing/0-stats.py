#!/usr/bin/python3
""" cript that reads stdin line by line and computes metrics: """

import sys


def display_metrics(codes, file_size):
    """
    Display the computed metrics.
    """
    print("File size:", file_size)
    for k, v in sorted(codes.items()):
        if v != 0:
            print(f"{k}: {v}")


def main():
    """
    Main function to process log data and compute metrics.
    """
    file_size = 0
    count_lines = 0
    codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
             "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            parsed_line = line.split()

            if len(parsed_line) >= 7:
                status_code = parsed_line[-2]
                if status_code in codes:
                    codes[status_code] += 1

                try:
                    file_size += int(parsed_line[-1])
                except ValueError:
                    pass

                count_lines += 1

                if count_lines == 10:
                    display_metrics(codes, file_size)
                    count_lines = 0

    except KeyboardInterrupt:
        pass

    finally:
        display_metrics(codes, file_size)


if __name__ == "__main__":
    main()
