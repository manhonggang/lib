import itertools
items = [1, 2, 3]

for item in itertools.permutations(items):
    print(item)

for item in itertools.combinations_with_replacement(items, 2):
    print(item)

ab = ['a', 'b']
cd = ['1', '2', '3']
for item in itertools.product(ab, cd):
    print(item)