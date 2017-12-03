from math import sqrt

number = 277678


"""
PROBLEM 1:
We find the smallest spiral with an odd square S in the bottom right corner that contains our number.
We get a square of numbers, its side length is sqrt(S) and our input is one of the margin values.
Manhattan distance = number of steps from access port to margin values
											+
					 minimum number of steps from the middle value of square side to our input

PROBLEM 2:
The solution can be found on https://oeis.org/A141481.
"""


def nearest_square(num):
    return round(sqrt(num))**2


def odd_corner(num):
    corner = nearest_square(num)
    side_length = sqrt(corner) if corner >= number else sqrt(corner) + 1
    side_length = side_length if (side_length % 2) != 0 else side_length + 1
    return int(side_length ** 2)


def get_side_values(corner):
    side_length = int(sqrt(corner))
    n = 4 + 4 * (side_length - 2)
    return list(range(corner - n + 1, corner + 1))


corner = odd_corner(number)
side_values = get_side_values(corner)
l_to_side = int(sqrt(corner) / 2)

shortest_path_vals = [side_values[i] for i in [j * 2 * l_to_side + l_to_side - 1 for j in range(0, 4)]]

diff = [abs(val - number) for val in shortest_path_vals]

manhattan_distance = l_to_side + min(diff)
print(manhattan_distance)