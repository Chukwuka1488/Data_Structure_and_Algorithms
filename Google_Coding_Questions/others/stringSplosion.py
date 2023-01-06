def string_splosion(s):
    a = []
    for i in range(len(s)):
        a.append(s[:i+1])

    return "".join(a)


print(string_splosion('Code'))
