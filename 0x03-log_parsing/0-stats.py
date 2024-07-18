#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning.
"""

import sys

size = 0
status_codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
count = 0


def print_status_code():
    """Prints statistics since the beginning of each
    10 lines or on interrupt."""
    print("File size:", size)
    for key in sorted(status_codes):
        print(key + ":", status_codes[key])


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            count += 1
            elements = line.split()

            # Check if the line has at least 2 elems for stat code &file size
            if len(elements) < 2:
                continue

            try:
                size += int(elements[-1])
            except (IndexError, ValueError):
                continue

            try:
                status_code = elements[-2]
                if status_code in valid_codes:
                    if status_code not in status_codes:
                        status_codes[status_code] = 1
                    else:
                        status_codes[status_code] += 1
            except IndexError:
                continue

            if count == 10:
                print_status_code()
                count = 0

        print_status_code()

    except KeyboardInterrupt:
        print_status_code()
        sys.exit(0)
