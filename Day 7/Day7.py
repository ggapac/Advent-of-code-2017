from collections import Counter

fname = "day7.txt"

with open(fname) as f:
    content = [x.strip("\n") for x in f.readlines()]


def problem1():
    inpt = [x for x in content if "->" in x]

    bottoms = list()
    discs = list()

    for x in inpt:
        tmp = x.split("->")
        bottoms.append(tmp[0].split()[0])
        tmp_discs = [disc.split() for disc in tmp[1].split(",")]
        discs.append(sum(tmp_discs, []))

    discs = sum(discs, [])

    bottom = set(bottoms) - set(discs)

    return list(bottom)


def extract_data():
    relationship = dict()
    values = dict()

    for x in content:
        if "->" in x:
            tmp = x.split("->")
            relationship[tmp[0].split()[0]] = sum([disc.split() for disc in tmp[1].split(",")], [])
            lala = tmp[0].split()[1]
            values[tmp[0].split()[0]] = int(lala[1:-1])
        else:
            tmp = x.split(" ")
            lala = tmp[1].split()[0]
            relationship[tmp[0].split()[0]] = []
            values[tmp[0]] = int(lala[1:-1])

    return relationship, values


def get_weight(x, relationship, values):
    return values[x] + sum(get_weight(disc, relationship, values) for disc in relationship[x])


def subtower_weight(x, relationship, values):
    weights = list()
    discs = relationship[x]
    for disc in discs:
        weights.append(get_weight(disc, relationship, values))
    return discs, weights


def get_change_value(count, weights, values, discs):
    for k, v in count.items():
        if v == 1:
            intruder = k
        else:
            rest = k

    ix = weights.index(intruder)

    change = intruder - rest if intruder < rest else rest - intruder
    return values[discs[ix]] + change


def problem2():
    relationship, values = extract_data()

    changes = list()
    check = problem1()

    i = 0

    while i < len(check):
        key = check[i]
        if relationship[key] != [] or len(relationship[key]) != 1:
            discs, weights = subtower_weight(key, relationship, values)
            check.extend(discs)
            count = Counter(weights)

            if len(count) > 1:
                changes.append(get_change_value(count, weights, values, discs))
        i += 1

    return changes[len(changes) - 1]

print(problem1())
print(problem2())
