def count_char(str):
    char_count = {}
    for i in str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count
a = count_char("ducphuc")
print(a)