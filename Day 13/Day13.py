fname = "day13.txt"

with open(fname) as f:
    content = [x.strip("\n").split(": ") for x in f.readlines()]

data = list()

for line in content:
    data.append([int(line[0]), int(line[1])])

severity = sum(d[0] * d[1] for d in data if d[0] % ((d[1] - 1) * 2) == 0)

delay = 0

while True:
    for d in data:
            s = (delay + d[0]) % ((d[1] - 1) * 2)
            if s == 0:
                break
    else:
        break
    delay += 1

print(severity)
print(delay)
