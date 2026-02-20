def validate_machine(data):
    required_keys = ['name', 'alphabet', 'blank', 'states', 'initial', 'finals', 'transitions']
    if not isinstance(data,dict) or not all(key in data for key in required_keys):
        return False
    
    set_states = set(data['states'])
    set_alphabet = set(data['alphabet'])
    valid_actions = {'LEFT', 'RIGHT'}
    required_transition_keys = {'read', 'write', 'to_state', 'action'}

    if not isinstance(data["transitions"], dict):
        return False

    checks = [
        # Alphabet characters are single characters
        all(len(char) == 1 for char in data['alphabet']),

        # Blank symbol is part of the alphabet
        data['blank'] in set_alphabet,

        # Initial state is part of the states
        data['initial'] in set_states,

        # Final states are a sub-list of states
        all(state in set_states for state in data['finals']),

        # 5. Transitions logic check
        all(
            # Key must be a valid state 
            state in set_states and isinstance(rules, list) and
            # Each rule must have the required keys
            all(
                isinstance(trans, dict) and required_transition_keys.issubset(trans.keys()) and
                trans['read'] in set_alphabet and
                trans['write'] in set_alphabet and
                trans['to_state'] in set_states and
                trans['action'] in valid_actions
                for trans in rules
            )
            for state, rules in data['transitions'].items()
        )
    ]
    
    return all(checks)