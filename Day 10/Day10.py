file = open("day10.txt", "r")
inpt = file.read()

elements = list(range(256))


def get_index(ix):
    return ix - len(elements) if ix >= len(elements) else ix


def get_indices(curr_i, length):
    indices = list(range(curr_i, curr_i + length))
    indices = [ix % len(elements) if ix >= len(elements) else ix for ix in indices]
    return indices


def translate_input(inp):
    inp = [ord(char) for char in inp]
    inp.extend([17, 31, 73, 47, 23])
    return inp


def do_round(inp, curr_i, skip, els):
    i = 0

    while i < len(inp):
        length = int(inp[i])
        indices = get_indices(curr_i, length)
        list_tmp = [els[ix] for ix in indices]
        for ix, val in enumerate(indices):
            els[val] = list_tmp[::-1][ix]
        curr_i = get_index(curr_i + length + skip)
        i += 1
        skip += 1

    return curr_i, skip, els


def problem1(inp, els):
    curr_i = 0
    skip = 0

    inp = inp.split(",")

    curr_i, skip, els = do_round(inp, curr_i, skip, els)

    return els[0] * els[1]


def problem2(inp, els):
    inp = translate_input(inp)
    curr_i = 0
    skip = 0

    rounds = 0
    while rounds < 64:
        curr_i, skip, els = do_round(inp, curr_i, skip, els)
        rounds += 1

    block = 0
    knot_dash = ""

    while block < len(els):
        indices = list(range(block, 16 + block))
        xor = 0
        for ix in indices:
            xor ^= els[ix]
        knot_dash += hex(xor)[2:4] if len(hex(xor)) == 4 else "0" + hex(xor)[2:3]
        block += 16

    return knot_dash


print(problem1(inpt, elements))
print(problem2(inpt, elements))
