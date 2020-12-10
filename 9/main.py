def check_valid(sum: int, range: list) -> bool:
    for i, n in enumerate(range):
        if (sum - n) in [n for j, n in enumerate(range) if not j == i]:
            return True


def find_sum_range(sum: int, range: list) -> int:
    range_index, range_sum = 0, 0
    while range_sum < sum:
        range_sum += range[range_index]
        range_index += 1
    if range_sum == sum:
        return range_index


with open('input') as f:
    preamble_size = 25
    cypher = [int(l) for l in f]
    for i, n in enumerate(cypher):
        if not check_valid(n, cypher[(i-preamble_size):i]) and i >= preamble_size:
            end, invalid = i, n
            print('part 1:', invalid)
    for i in range(len(cypher[:end])):
        range_index = find_sum_range(invalid, cypher[i:end])
        if range_index:
            print('part 2:', min(cypher[i:i+range_index]) + max(cypher[i:i+range_index]))


