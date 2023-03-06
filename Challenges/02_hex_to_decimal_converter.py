hex_numbers_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}


def hex_to_decimal(hex_number):
    for character in hex_number:
        if character not in hex_numbers_dict:
            return None
    if type(hex_number) is str:
        decimal_number = 0
        digit_count = len(hex_number)
        string_position = -1
        for power in range(digit_count):
            decimal_number += hex_numbers_dict.get(hex_number[string_position]) * (16 ** power)
            string_position -= 1
    print(f'Decimal equivalent of {hex_number} is {decimal_number}')


hex_to_decimal('E3BFF')
