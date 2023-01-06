def reverse_string(s):
    s = list(s)

    # Use two pointers to reverse the string in place
    for i in range(len(s) // 2):
        s[i] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = s[i]

    s = "".join(s)
    return s


print(reverse_string('coderbyte'))
