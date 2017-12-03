file = open("day1.txt", "r")
inpt = file.read()


def walk(s, k = 2):
    # Get pairs of input numbers
    for i in range(len(s) - (k - 1)):
        yield (s[i:i + k])


def problem1(inpt):
    z = list(walk(inpt))
    z.append(inpt[0] + inpt[len(inpt) - 1])

    # If pair of digits is divisible by 11, add its quotient to our sum
    return sum(int(pair) / 11 for pair in z if int(pair) % 11 == 0)


def get_ix(inpt, ix):
    # Circular list, get the correct index
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


print(problem1(inpt))
print(problem2(inpt))
