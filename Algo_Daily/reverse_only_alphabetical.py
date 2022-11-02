import re


# reverse the array function
def reverse_array(arr):
    return arr[::-1]


def reverse_only_alpha(s):
    s = list(s)
    new_s = ""
    # check for only alphabets
    r = re.compile("[a-zA-Z]")

    alp_char = [char for char in s if r.match(char)]
    # reverse the alpha arrays
    reversed_alpha = reverse_array(alp_char)

    idx_ra = 0
    for i in range(len(s)):
        if r.match(s[i]):
            new_s += reversed_alpha[idx_ra]
            idx_ra += 1
        else:
            new_s += s[i]

    return new_s


if __name__ == "__main__":
    print(reverse_only_alpha('sea!$hells3'))
