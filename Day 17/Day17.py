step = 356


def spinlock(num, insert):
    buffer = [0]
    pos = 0
    after0 = 0

    for i in range(1, num):
        pos = (pos + step) % i + 1
        if pos == 1 and not insert:
            after0 = i
        if insert:
            buffer.insert(pos, i)

    return buffer[pos + 1] if insert else after0


print(spinlock(2018, True))
print(spinlock(50000001, False))
