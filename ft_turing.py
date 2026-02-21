import sys
import json
from simulator.parser import validate_machine
from simulator.engine import run_machine

sys.setrecursionlimit(100000)

USAGE = "\n".join([
    "usage: ft_turing [-h] jsonfile input",
    "",
    "positional arguments:",
    "  jsonfile              json description of the machine",
    "",
    "  input                 input of the machine",
    "",
    "optional arguments:",
    "  -h, --help            show this help message and exit",
])

SEPARATOR = "*" * 61


def load_machine(path):
    """Returns parsed machine dict, or raises SystemExit on error."""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for file '{path}'.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON file - {e}")
        sys.exit(1)


def format_transition(state, t):
    return f"({state}, {t['read']}) -> ({t['to_state']}, {t['write']}, {t['action']})"


def format_header(machine):
    """Pure function: builds the header block as a single string."""
    transition_lines = "\n".join(
        format_transition(state, t)
        for state, rules in machine['transitions'].items()
        for t in rules
    )
    return "\n".join([
        SEPARATOR,
        f"*{machine['name']:^59}*",
        SEPARATOR,
        f"Alphabet: [ {', '.join(machine['alphabet'])} ]",
        f"States: [ {', '.join(machine['states'])} ]",
        f"Initial: {machine['initial']}",
        f"Finals: [ {', '.join(machine['finals'])} ]",
        transition_lines,
        SEPARATOR,
    ])


def main():
    args = sys.argv[1:]

    if len(args) == 1 and args[0] in ("-h", "--help"):
        print(USAGE)
        sys.exit(0)

    if len(args) != 2:
        print(USAGE)
        sys.exit(1)

    json_path, input_str = args[0], args[1]

    machine = load_machine(json_path)

    if not validate_machine(machine):
        print("Error: Invalid Turing machine definition.")
        sys.exit(1)

    if machine["blank"] in input_str:
        print("Error: Input string cannot contain the blank character.")
        sys.exit(1)

    if not all(c in machine["alphabet"] for c in input_str):
        print("Error: Input string contains characters not in the alphabet.")
        sys.exit(1)

    tape = list(input_str) if input_str else [machine["blank"]]

    print(format_header(machine))

    try:
        lines, result_tape, total_steps = run_machine(machine, tape, 0, machine["initial"])
        print("\n".join(lines))
        if result_tape is not None:
            print(f"Machine halted after {total_steps} steps.")
    except RecursionError:
        print("Error: Maximum recursion depth exceeded. Possible infinite loop.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Execution interrupted by user.")
        sys.exit(1)


if __name__ == "__main__":
    main()
