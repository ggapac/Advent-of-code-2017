file = open("day1.txt", "r")
inpt = file.read()


def walk(s, k = 2):
    for i in range(len(s) - (k - 1)):
        yield (s[i:i + k])


def problem1(inpt):
    z = list(walk(inpt))
    z.append(inpt[0] + inpt[len(inpt) - 1])

    return sum(int(pair) / 11 for pair in z if int(pair) % 11 == 0)


def get_ix(inpt, ix):
    return ix - len(inpt) if len(inpt) <= ix else ix


def problem2(inpt):
    s = 0
    half = len(inpt) / 2

    for i in range(0, len(inpt)):
        ix = int(i + half)
        ix = get_ix(inpt, ix)
        tmp = inpt[i] + inpt[ix]

        s += int(tmp) / 11 if int(tmp) % 11 == 0 else 0

    return s


print(problem2(inpt))
