line = input()
letter_count = 0
digit_count = 0
space_count = 0
other_count = 0
for c in line:
    if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
        letter_count += 1
    elif c.isdigit():
        digit_count += 1
    elif c.isspace():
        space_count += 1
    else:
        other_count += 1
print(f"英文字符:{letter_count}\n数字:{digit_count}\n空格:{space_count}\n其他字符:{other_count}")
