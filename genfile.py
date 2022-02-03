import re
import sys


def main():
    i = 1
    while i < len(sys.argv):
        file_name = sys.argv[i]

        if i == len(sys.argv) - 1:
            print(f'Last file "{file_name}" is missing size')
            return

        try:
            generate_file(file_name, parse_size(sys.argv[i + 1], i + 1))
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(f'Failed to generate file "{file_name}": {e}')

        i = i + 2


def generate_file(name, byte_count):
    f = open(name, 'w')
    f.seek(byte_count - 1)
    f.write('\0')
    f.close()


def parse_size(size, arg_num):
    size_regex = r"^[0-9gGmMkK+]{1,}$"
    if not re.match(size_regex, size):
        raise Exception(f'argument {arg_num} "{size}" contains illegal characters, must match /{size_regex}/')

    byte_count = 0

    for part in size.split('+'):
        part_regex = r"^[0-9]{1,}(g|m|k){0,1}$"
        if not re.match(part_regex, part):
            raise Exception(f'argument {arg_num} contains invalid size component "{part}", must match /{part_regex}/')

        last_char_index = len(part) - 1
        last_char = part[last_char_index]

        if not re.match(r"^[gGmMkK]$", last_char):
            byte_count += int(part)
            continue

        unit = last_char.lower()
        value = int(part[0:last_char_index])

        if unit == 'g':
            byte_count += (value * 1024 * 1024 * 1024)
        elif unit == 'm':
            byte_count += (value * 1024 * 1024)
        elif unit == 'k':
            byte_count += (value * 1024)
        else:
            raise Exception(f'argument {arg_num} contains unknown size unit "{unit}"')

    return byte_count


if __name__ == '__main__':
    main()
