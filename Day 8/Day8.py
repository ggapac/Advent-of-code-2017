fname = "day8.txt"

with open(fname) as f:
    content = [x.strip("\n").split(" ") for x in f.readlines()]

registers = dict()
which_reg = list()
vals = list()
condition_reg = list()
condition = list()

for line in content:
    registers[line[0]] = 0
    which_reg.append(line[0])
    vals.append(int(line[2])) if line[1] == "inc" else vals.append(-int(line[2]))
    condition_reg.append(line[4])
    condition.append(line[5] + line[6])

curr_max = 0

for i in range(1, len(which_reg)):
    if eval(str(registers[condition_reg[i]]) + condition[i]):
        registers[which_reg[i]] += vals[i]
        if registers[which_reg[i]] > curr_max:
            curr_max = registers[which_reg[i]]


print(max(registers.values()))
print(curr_max)
