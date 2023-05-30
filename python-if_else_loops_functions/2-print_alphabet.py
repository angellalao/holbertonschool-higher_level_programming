#!/usr/bin/python3
start = ord('a')
end = ord('z') + 1
for ascii_val in range(start, end):
    character = chr(ascii_val)
    print(character, end='')
