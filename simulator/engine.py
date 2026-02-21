def step(machine, tape, head, state):
    """
    Calculates the next single state of the machine.
    Returns: (new_tape, new_head, new_state) or None if blocked.
    """
    read_char = tape[head]

    if state not in machine['transitions']:
        return None
        
    rule = next((t for t in machine['transitions'][state] if t['read'] == read_char), None)
    
    if not rule:
        return None

    new_char = rule['write']
    tape_written = tape[:head] + [new_char] + tape[head+1:]

    # Move Head
    direction = rule['action']
    new_head = head + 1 if direction == 'RIGHT' else head - 1

    # Expand Tape
    blank = machine['blank']
    
    if new_head < 0:
        return ([blank] + tape_written, 0, rule['to_state'])
    elif new_head >= len(tape_written):
        return (tape_written + [blank], new_head, rule['to_state'])
    else:
        return (tape_written, new_head, rule['to_state'])

def format_tape_state(tape, head, state, rule=None):
    """
    Returns the tape line with head marker and optional transition.
    Final state:  [11<1>1=..] (state)
    Active step:  [11<1>1=..] (state, read) -> (to_state, write, action)
    """
    formatted_tape = "".join(
        f"<{char}>" if i == head else char
        for i, char in enumerate(tape)
    )
    if rule:
        return (f"[{formatted_tape}] ({state}, {rule['read']}) -> "
                f"({rule['to_state']}, {rule['write']}, {rule['action']})")
    return f"[{formatted_tape}] ({state})"

def run_machine(machine, tape, head, state, step_count=0):
    """
    Recursive driver that runs the machine until HALT or BLOCK.
    Returns (lines, tape, step_count) on halt, (lines, None, step_count) on block.
    All output lines are collected and returned — no side effects.
    """
    if state in machine['finals']:
        return ([format_tape_state(tape, head, state)], tape, step_count)

    read_char = tape[head]
    rule = next(
        (t for t in machine['transitions'].get(state, []) if t['read'] == read_char),
        None
    )

    line = format_tape_state(tape, head, state, rule)

    if rule is None:
        return ([line, "Error: Machine blocked (undefined transition)."], None, step_count)

    new_tape, new_head, new_state = step(machine, tape, head, state)
    rest_lines, result_tape, final_count = run_machine(machine, new_tape, new_head, new_state, step_count + 1)
    return ([line] + rest_lines, result_tape, final_count)