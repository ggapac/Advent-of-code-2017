file = open("day9.txt", "r")
inpt = file.read()

n_group = 0
n_garb = 0
group_start = 0
garb = False

i = 0

while i < len(inpt):
    if inpt[i] == "!":
        i += 2
        continue

    if inpt[i] == "{" and garb is False:
        group_start += 1
    elif inpt[i] == "}" and garb is False:
        n_group += group_start
        group_start -= 1
    elif inpt[i] == "<":
        garb = True
    elif inpt[i] == ">":
        garb = False
        n_garb -= 1

    if garb is True:
        n_garb += 1

    i += 1

print(n_group)
print(n_garb)
