file = open("day16.txt", "r")
inpt = file.read().split(",")

programs = list("abcdefghijklmnop")


def swap(i, j, pr):
    pr[i], pr[j] = pr[j], pr[i]
    return pr


def dance(pr):
    for move in inpt:
        if move[0] == "s":
            pr = pr[-int(move[1:]):] + pr[:-int(move[1:])]
        elif move[0] == "x":
            places = move[1:].split("/")
            pr = swap(int(places[0]), int(places[1]), pr)
        else:
            pr = swap(pr.index(move[1]), pr.index(move[3]), pr)
    return pr


def problem1(pr):
    pr = dance(pr)
    return ''.join(pr)


def problem2(pr):
    seen = list()

    for _ in range(1000000000):
        s = "".join(pr)
        if s in seen:
            return ''.join(seen[1000000000 % len(seen)])
        seen.append(s)
        pr = dance(pr)

    return ''.join(pr)

print(problem1(programs))
print(problem2(programs))
