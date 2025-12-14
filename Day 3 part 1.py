def max_joltage_for_bank(bank: str) -> int:
    digits = list(map(int, bank))
    best = 0


    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            value = digits[i] * 10 + digits[j]
            if value > best:
                best = value
    return best


def total_output_joltage(input_text: str) -> int:
    total = 0
    for line in input_text.strip().splitlines():
        total += max_joltage_for_bank(line.strip())
    return total


input_data = """987654321111111
811111111111119
234234234234278
818181911112111"""

print(total_output_joltage(input_data))
