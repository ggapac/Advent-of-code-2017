file = open("day14.txt", "r")
inpt = file.read()

elements = list(range(256))


def translate_input(inp):
    inp = [ord(char) for char in inp]
    inp.extend([17, 31, 73, 47, 23])
    return inp


def get_index(ix):
    return ix - len(elements) if ix >= len(elements) else ix


def get_indices(curr_i, length):
    indices = list(range(curr_i, curr_i + length))
    indices = [ix % len(elements) if ix >= len(elements) else ix for ix in indices]
    return indices


def do_round(inp, curr_i, skip, els):
    j = 0

    while j < len(inp):
        length = int(inp[j])
        indices = get_indices(curr_i, length)
        list_tmp = [els[ix] for ix in indices]
        for ix, val in enumerate(indices):
            els[val] = list_tmp[::-1][ix]
        curr_i = get_index(curr_i + length + skip)
        j += 1
        skip += 1

    return curr_i, skip, els


def knot_hash_binary(inp, els):
    inp = translate_input(inp)
    curr_i = 0
    skip = 0

    rounds = 0
    while rounds < 64:
        curr_i, skip, els = do_round(inp, curr_i, skip, els)
        rounds += 1

    block = 0
    res = ""

    while block < len(els):
        indices = list(range(block, 16 + block))
        xor = 0
        for ix in indices:
            xor ^= els[ix]
        res += hex(xor)[2:4] if len(hex(xor)) == 4 else "0" + hex(xor)[2:3]
        block += 16

    return '{:0128b}'.format(int(res, 16))


def floodfill(rows, i, j, ix):
    if rows[i][j] == "1":
        rows[i][j] = ix
        if i > 0:
            floodfill(rows, i - 1, j, ix)
        if i < 127:
            floodfill(rows, i + 1, j, ix)
        if j > 0:
            floodfill(rows, i, j - 1, ix)
        if j < 127:
            floodfill(rows, i, j + 1, ix)


# Problem 1
n = 0
rows = list()

for i in range(128):
    v = knot_hash_binary(inpt + "-" + str(i), list(range(256)))
    rows.append(list(v))
    n += v.count("1")

print(n)

# Problem 2
ix = 0

for x in range(128):
    for y in range(128):
        if rows[x][y] == "1":
            floodfill(rows, x, y, ix)
            ix += 1

print(ix)
