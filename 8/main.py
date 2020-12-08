def read_code(current_index: int, instr: str) -> list:
    # returns [next_index, accu_amt, operation_type, operation_amt]
    operation, num = instr.split(' ')
    if operation == 'acc':
        return [current_index + 1, int(num), operation]
    elif operation == 'jmp':
        return [current_index + int(num), 0, operation, int(num)]
    else:
        return [current_index + 1, 0, operation, int(num)]


def go_forward(inputs: dict, position: int, history: list) -> list:
    history.append(position)
    next_position = inputs[position][0]
    if next_position in history or next_position >= len(inputs.values()):
        return history
    else:
        return go_forward(inputs, next_position, history)


def go_backward(inputs: dict, position: int, history: list) -> list:
    history.append(position)
    next_positions = [i for i, v in inputs.items() if v[0] == position]
    if len(next_positions) >= 1:
        for next_position in next_positions:
            if next_position not in history:
                history = go_backward(inputs, next_position, history)
    return history


with open('input', 'r') as f:
    inputs = {i: read_code(i, l) for i, l in enumerate(f)}
    forward_paths = go_forward(inputs, 0, [])
    print('part 1:', sum([v[1] for i, v in inputs.items() if i in forward_paths]))
    backward_paths = go_backward(inputs, len(inputs), [])
    for i, v in inputs.items():
        if i in forward_paths:
            if v[2] == 'nop' and (i + v[3]) in backward_paths:
                inputs[i] = [i + v[3], 0]
                break
            if v[2] == 'jmp' and (i + 1) in backward_paths:
                inputs[i] = [i + 1, 0]
                break
    forward_paths = go_forward(inputs, 0, [])
    print('part 2:', sum([v[1] for i, v in inputs.items() if i in forward_paths]))