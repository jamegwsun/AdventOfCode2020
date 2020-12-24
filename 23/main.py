def solve_cups(cups: dict, current: int, moves: int) -> dict:
    max = len(cups)
    for _ in range(moves):
        picked = (cups[current], cups[cups[current]], cups[cups[cups[current]]])
        first_picked, _, last_picked = picked
        dest = current - 1 if current - 1 > 0 else max
        while dest in picked:
            dest = dest - 1 if dest > 1 else max
        cups[current] = cups[last_picked]
        cups[last_picked] = cups[dest]
        cups[dest] = first_picked
        current = cups[current]
    return cups


def link_cups(cups_input: list) -> dict:
    cups = {cups_input[i]: cups_input[i + 1] for i in range(len(cups_input[:-1]))}  # cup: next cup
    cups[cups_input[-1]] = cups_input[0]
    return cups


cups_input = [int(c) for c in open('input').read()]
cups = link_cups(cups_input)
cups = solve_cups(cups, cups_input[0], 100)
p1 = [1]
for _ in range(8):
    p1.append(cups[p1[-1]])
print('part 1:', ''.join([str(c) for c in p1[1:]]))

cups_input += [i for i in range(10, 1000001)]
cups = link_cups(cups_input)
cups = solve_cups(cups, cups_input[0], 10000000)
print('part 2:', cups[1] * cups[cups[1]])
