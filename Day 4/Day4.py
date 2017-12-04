"""
We convert our passphrase list to a set. If number of elements in the set is
the same as number of elements in the list, we know that the passphrase is valid.
(A set contains only unique elements.)

For problem 2 we just need to make sure the letters in the words are ordered.
"""

fname = "day4.txt"

with open(fname) as f:
    content = f.readlines()

content = [[''.join(sorted(el)) for el in x.strip('\n').split()] for x in content]

s = sum(1 for phrase in content if len(set(phrase)) == len(phrase))
print(s)
