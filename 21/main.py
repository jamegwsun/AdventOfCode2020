allergens = {}
menu, safe_ingredients = [], []
sketchy_ingredients, solved_ingredients = set(), set()

with open('input') as f:
    f = f.readlines()

for l in f:
    s = l.strip(')\n').split('(contains')
    als = {k:set(s[0].strip().split(' ')) for k in s[1].replace(' ', '').split(',')}
    menu.append((s[1].replace(' ', '').split(','), set(s[0].strip().split(' '))))
    for a, i in als.items():
        if a in allergens.keys():
            allergens[a] &= i
        else:
            allergens[a] = i

for i in allergens.values():
    sketchy_ingredients |= i

for als, ings in menu:
    safe_ingredients += [ing for ing in ings if ing not in sketchy_ingredients]

print('part 1:', len(safe_ingredients))

finish = None
while not finish:
    finish = True
    for a, i in allergens.items():
        if isinstance(i, str):
            pass
        elif len(i) == 1:
            solved_ingredients |= i
            allergens[a] = list(i)[0]
        else:
            finish = False
            allergens[a] -= solved_ingredients

sorted_allergens = {a: allergens[a] for a in sorted(allergens.keys())}
print('part 2:', ','.join(sorted_allergens.values()))