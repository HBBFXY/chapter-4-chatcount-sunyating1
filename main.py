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
print(f"{letter_count}")
print(f"{digit_count}")
print(f"{space_count}")
print(f"{other_count}")
