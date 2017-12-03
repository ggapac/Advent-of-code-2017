import itertools

fname = "day2.txt"


def tonumbers(line):
	# Split input to rows, parse and sort the integers
    return sorted(list(map(int, line.split())))


with open(fname) as f:
    content = f.readlines()

content = [tonumbers(x.strip('\n')) for x in content]

problem1 = sum(max(line) - min(line) for line in content)
problem2 = sum(b/a for line in content for a, b in itertools.combinations(line, 2) if b % a == 0)

print(problem1)
print(problem2)
