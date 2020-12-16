with open('input') as f:
    start = [int(l) for l in f.read().split(',')]

age = dict()
last_num, curr_num = None, None

for i in range(30000000):
    if i < len(start):
        curr_num = start[i]
    else:
        curr_num = i - 1 - age[last_num] if last_num in age.keys() else 0
        age[last_num] = i
    if last_num is not None:    
        age[last_num] = i - 1
    last_num = curr_num
    if i == 2019:
        p1_num = last_num
print('part 1:', p1_num)
print('part 2:', last_num)