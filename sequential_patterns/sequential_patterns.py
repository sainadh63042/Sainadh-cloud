def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def identify_pattern(sequence):
    if all(isinstance(item, int) for item in sequence):
        diff = sequence[1] - sequence[0]
        for i in range(1, len(sequence)):
            if sequence[i] != sequence[i - 1] + diff:
                return None
        return sequence[-1] + diff
    elif all(isinstance(item, str) for item in sequence):
        if all(item[:-1].isalpha() and item[-1].isdigit() for item in sequence):
            base = sequence[0][:-1]
            num = int(sequence[-1][-1])
            return f"{base}{num + 1}"
        elif all(len(item) == 1 and item.isalpha() for item in sequence):
            next_char = chr(ord(sequence[-1]) + 1)
            return next_char
    elif all(is_prime(item) for item in sequence):
        if len(sequence) > 1:
            diff = sequence[1] - sequence[0]
            for i in range(1, len(sequence)):
                if sequence[i] != sequence[i - 1] + diff:
                    return None
            return sequence[-1] + diff
        else:
            return sequence[0] + 2 if sequence[0] != 2 else 3


def main():
    while True:
        sequence_input = input(
            "Enter the sequence (comma-separated integers, strings, or prime numbers), or type 'stop' to exit: ")

        if sequence_input.lower() == "stop":
            exit()

        sequence_input = [item.strip() for item in sequence_input.split(',')]

        try:
            sequence_input = [int(item) for item in sequence_input]
        except ValueError:
            pass

        next_number = identify_pattern(sequence_input)
        if next_number is not None:
            print(f"Next number in sequence {sequence_input}: {next_number}")
        else:
            print("Pattern not identified.")


if __name__ == "__main__":
    main()
