#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    reg_num = []
    for letter in roman_string:
        if letter in rom_num.keys():
            reg_num.append(rom_num.get(letter))
        x = 0
        for num in range(len(reg_num) - 1):
            if reg_num[x] < reg_num[x + 1]:
                reg_num[x+1] = reg_num[x+1] - reg_num[x]
                del reg_num[x]
    return sum(reg_num)
