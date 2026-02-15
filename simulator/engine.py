def step(machine, tape, head, state):
    """
    Calculates the next single state of the machine.
    Returns: (new_tape, new_head, new_state) or None if blocked.
    """
    read_char = tape[head]

    # Search transitions[state] for a rule where 'read' matches read_char
    if state not in machine['transitions']:
        return None
        
    rule = next((t for t in machine['transitions'][state] if t['read'] == read_char), None)
    
    if not rule:
        return None

    # Create new list with the new char
    new_char = rule['write']
    tape_written = tape[:head] + [new_char] + tape[head+1:]

    # Move Head
    direction = rule['action']
    new_head = head + 1 if direction == 'RIGHT' else head - 1

    # Expand Tape (Infinite Tape Logic)
    blank = machine['blank']
    
    if new_head < 0:
        return ([blank] + tape_written, 0, rule['to_state'])
    elif new_head >= len(tape_written):
        return (tape_written + [blank], new_head, rule['to_state'])
    else:
        return (tape_written, new_head, rule['to_state'])

def print_tape_state(tape, head, state):
    """
    Prints the tape with the head surrounding the current character.
    Example: [11<1>1=..] (state)
    """
    formatted_tape = "".join(
        f"<{char}>" if i == head else char 
        for i, char in enumerate(tape)
    )
    
    # Print the final string
    print(f"[{formatted_tape}] ({state})")

def run_machine(machine, tape, head, state):
    """
    Recursive driver that runs the machine until HALT or BLOCK.
    """
    # Print current state (Required by subject)
    print_tape_state(tape, head, state) # We need to define this later

    # Check if we are in a FINAL state 
    if state in machine['finals']:
        return tape

    # Calculate next step
    result = step(machine, tape, head, state)

    # Check for blocking (Undefined transition)
    if result is None:
        print("Error: Machine blocked (undefined transition).")
        return None

    new_tape, new_head, new_state = result
    return run_machine(machine, new_tape, new_head, new_state)