"""Problem 89: Generate a circular sequence Gray codes"""

def _convert_to_int(code):
    """Convert a list of 0/1 to unsigned int, left being less significant"""
    power = 1
    num = 0
    for b in code:
        num += b * power
        power <<= 1
    return num

def gray_code_sequence_generator(n):
    gray_code_sequence = []
    two_to_power = [2 ** i for i in range(n + 1)]
    gray_code = [0] * n
    gray_code_sequence.append(0)
    for i in range(1, 2 ** n):
        for j in range(n):
            if i % two_to_power[j + 1] == two_to_power[j]:
                gray_code[j] = 1 - gray_code[j]
        gray_code_sequence.append(_convert_to_int(gray_code))
    return gray_code_sequence

if __name__ == "__main__":
    print(gray_code_sequence_generator(4))