fname = "day6.txt"

file = open(fname, "r")
blocks = file.read().split("\t")
blocks = [int(x) for x in blocks]

seen = list()
steps = 0


def distribute(ix, val, blocks):
    blocks[ix] = 0

    while val > 0:
        ix = ix + 1 if ix + 1 < len(blocks) else 0
        blocks[ix] += 1
        val -= 1

    return blocks


while blocks not in seen:
    seen.append(blocks[:])
    ix = blocks.index(max(blocks))
    max_val = blocks[ix]
    blocks = distribute(ix, max_val, blocks)
    steps += 1

first_occ = seen.index(blocks)

print(steps)
print(len(seen) - int(first_occ))
