def max_joltage_for_bank(bank: str, k: int = 12) -> int:
    digits = bank.strip()
    n = len(digits)

    result = []
    start = 0

    for i in range(k):
        remaining = k - i
        end = n - remaining
        max_digit = '0'
        max_index = start

        for j in range(start, end + 1):
            if digits[j] > max_digit:
                max_digit = digits[j]
                max_index = j
                if max_digit == '9':
                    break

        result.append(max_digit)
        start = max_index + 1

    return int("".join(result))


def total_output_joltage(input_text: str) -> int:
    total = 0

    for line in input_text.strip().splitlines():
        total += max_joltage_for_bank(line, 12)
    return total

input_data = """987654321111111
811111111111119
234234234234278
818181911112111"""

print(total_output_joltage(input_data))
