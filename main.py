line = input()
letter_count = 0
digit_count = 0
space_count = 0
other_count = 0
for c in line:
    if c.isalpha():
        letter_count += 1
    elif c.isdigit():
        digit_count += 1
    elif c.isspace():
        space_count += 1
    else:
        other_count += 1
print(f"英文字符:{letter_count}")
print(f"数字:{digit_count}")
print(f"空格:{space_count}")
print(f"其他字符:{other_count}")
