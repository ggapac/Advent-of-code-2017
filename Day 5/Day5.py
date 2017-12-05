fname = "day5.txt"

with open(fname) as f:
    content = f.readlines()

content = [int(x.strip('\n')) for x in content]


pos = 0
steps = 0

while 0 <= pos < len(content):
    new_pos = pos + content[pos]
    content[pos] += 1 if content[pos] < 3 else - 1
    steps += 1
    pos = new_pos

print(steps)
