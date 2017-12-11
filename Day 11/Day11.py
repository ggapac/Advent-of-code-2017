file = open("day11.txt", "r")
inpt = file.read().split(",")

x = 0
y = 0
z = 0


def cube_distance():
    return (abs(0 - x) + abs(0 - y) + abs(0 - z)) / 2

max_dist = 0

for direction in inpt:
    if direction == "ne":
        x += 1
        z -= 1
    elif direction == "n":
        y += 1
        z -= 1
    elif direction == "nw":
        x -= 1
        y += 1
    elif direction == "sw":
        x -= 1
        z += 1
    elif direction == "s":
        y -= 1
        z += 1
    else:
        x += 1
        y -= 1

    tmp_dist = cube_distance()
    if tmp_dist > max_dist:
        max_dist = tmp_dist

print(cube_distance())
print(max_dist)
