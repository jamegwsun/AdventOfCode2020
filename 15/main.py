# with open('input') as f:
#     start = [int(l) for l in f.split('')]  # fix this

start = [14,3,1,0,9,5]
age = dict()
last_num, curr_num = None, None

for i in range(30000000):
    if i < len(start):
        curr_num = start[i]
    else:
        curr_num =  i - 1 - age[last_num] if last_num in age.keys() else 0
        age[last_num] = i
    if last_num is not None:    
        age[last_num] = i - 1
    last_num = curr_num
    if i % 100 == 0:
        print(i)
print(last_num)