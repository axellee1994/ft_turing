from typing import Optional


def validate_machine(data: dict) -> Optional[str]:
    """
    Returns None if the machine description is valid,
    or a descriptive error message string if it is not.
    """
    required_keys = ['name', 'alphabet', 'blank', 'states', 'initial', 'finals', 'transitions']

    if not isinstance(data, dict):
        return "Machine description must be a JSON object."

    missing = [k for k in required_keys if k not in data]
    if missing:
        return f"Missing required field(s): {', '.join(missing)}."

    if not isinstance(data['alphabet'], list) or not all(isinstance(c, str) and len(c) == 1 for c in data['alphabet']):
        return "Field 'alphabet' must be a list of single-character strings."

    if not isinstance(data['states'], list) or not all(isinstance(s, str) for s in data['states']):
        return "Field 'states' must be a list of strings."

    if not isinstance(data['blank'], str) or data['blank'] not in set(data['alphabet']):
        return f"Field 'blank' must be a single character present in the alphabet."

    if data['initial'] not in set(data['states']):
        return f"Field 'initial' ('{data['initial']}') is not in 'states'."

    if not isinstance(data['finals'], list) or not all(s in set(data['states']) for s in data['finals']):
        invalid = [s for s in data.get('finals', []) if s not in set(data['states'])]
        return f"Field 'finals' contains state(s) not in 'states': {invalid}."

    if not isinstance(data['transitions'], dict):
        return "Field 'transitions' must be a JSON object."

    set_states = set(data['states'])
    set_alphabet = set(data['alphabet'])
    valid_actions = {'LEFT', 'RIGHT'}
    required_transition_keys = {'read', 'write', 'to_state', 'action'}

    for state, rules in data['transitions'].items():
        if state not in set_states:
            return f"Transition key '{state}' is not a defined state."
        if not isinstance(rules, list):
            return f"Transitions for state '{state}' must be a list."
        for trans in rules:
            if not isinstance(trans, dict) or not required_transition_keys.issubset(trans.keys()):
                return f"A transition in state '{state}' is missing required key(s)."
            if trans['read'] not in set_alphabet:
                return f"Transition in '{state}': read symbol '{trans['read']}' not in alphabet."
            if trans['write'] not in set_alphabet:
                return f"Transition in '{state}': write symbol '{trans['write']}' not in alphabet."
            if trans['to_state'] not in set_states:
                return f"Transition in '{state}': to_state '{trans['to_state']}' not in states."
            if trans['action'] not in valid_actions:
                return f"Transition in '{state}': action '{trans['action']}' must be LEFT or RIGHT."

    return None