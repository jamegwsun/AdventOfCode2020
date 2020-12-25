with open('input') as f:
    pub_card, pub_door = (int(k) for k in f.read().split('\n'))

s_num = 7
md = 20201227
loop_card, loop_door = 0, 0
val_card, val_door = 1, 1
while True:
    val_card *= s_num
    val_card %= md
    loop_card += 1
    if val_card == pub_card:
        break

while True:
    val_door *= s_num
    val_door %= md
    loop_door += 1
    if val_door == pub_door:
        break

key = 1
for _ in range(loop_card):
    key *= val_door
    key %= md

print(key)