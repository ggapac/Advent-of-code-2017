fname = "day15.txt"

with open(fname) as f:
    values = [x.strip("\n").split(" ")[4] for x in f.readlines()]


def next_val(val, m, k):
    while True:
        val = (val * m) % 2147483647
        if val % k == 0:
            return val


def run(num, values, k_a, k_b):
    n = 0
    a = 16807
    b = 48271

    for i in range(num):
        values[0] = next_val(int(values[0]), a, k_a)
        values[1] = next_val(int(values[1]), b, k_b)
        if '{:032b}'.format(values[0])[16:] == '{:032b}'.format(values[1])[16:]:
            n += 1

    return n

print(run(40000000, values[:], 1, 1))
print(run(5000000, values[:], 4, 8))
