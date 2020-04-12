# CodeJam 2020 Qualification Round
# Nitzan Haim April 4, 2020

def parenthesize(s):
    res = ""
    opened = 0
    for i in range(0, len(s)):
        d = int(s[i])
        if d == opened:
           res += s[i]

        elif d > opened:
            res += "(" * (d-opened) + s[i]
            opened = d

        else:  # d < opened
            difference = opened - d
            res += ")" * difference + s[i]
            opened -= difference

    res += ")" * opened
    return res


output = ""
test_cases = int(input())
for t in range(test_cases):
    S = input()

    output += "Case #" + str(t+1) + ": " + parenthesize(S) + "\n"

print(output[:-1])
