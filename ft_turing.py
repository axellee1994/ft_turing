import sys
import json
from typing import Optional
from simulator.parser import validate_machine
from simulator.engine import run_machine, MAX_STEPS

USAGE = "\n".join(
    [
        "usage: ft_turing [-h] jsonfile input",
        "",
        "positional arguments:",
        "  jsonfile              json description of the machine",
        "",
        "  input                 input of the machine",
        "",
        "optional arguments:",
        "  -h, --help            show this help message and exit",
    ]
)

SEPARATOR = "*" * 61


def load_machine(path: str) -> tuple[Optional[dict], Optional[str]]:
    """Pure loader: returns (machine_dict, None) on success, (None, error_msg) on failure."""
    try:
        with open(path, "r") as f:
            return (json.load(f), None)
    except FileNotFoundError:
        return (None, f"File '{path}' not found.")
    except PermissionError:
        return (None, f"Permission denied for file '{path}'.")
    except json.JSONDecodeError as e:
        return (None, f"Invalid JSON file - {e}")


def format_transition(state: str, t: dict) -> str:
    return f"({state}, {t['read']}) -> ({t['to_state']}, {t['write']}, {t['action']})"


def format_header(machine: dict) -> str:
    """Pure function: builds the header block as a single string."""
    transition_lines = "\n".join(
        format_transition(state, t)
        for state, rules in machine["transitions"].items()
        for t in rules
    )
    return "\n".join(
        [
            SEPARATOR,
            f"*{machine['name']:^59}*",
            SEPARATOR,
            f"Alphabet: [ {', '.join(machine['alphabet'])} ]",
            f"States: [ {', '.join(machine['states'])} ]",
            f"Initial: {machine['initial']}",
            f"Finals: [ {', '.join(machine['finals'])} ]",
            transition_lines,
            SEPARATOR,
        ]
    )


def input_error(machine: dict, input_str: str) -> Optional[str]:
    """Pure function: returns an error message if the input is invalid, else None."""
    return (
        "Input string cannot be empty."
        if not input_str
        else "Input string cannot contain the blank character."
        if machine["blank"] in input_str
        else "Input string contains characters not in the alphabet."
        if not all(c in machine["alphabet"] for c in input_str)
        else None
    )


def simulate(machine: dict, input_str: str) -> tuple[list[str], int]:
    """Pure function: runs the machine and returns (output_lines, exit_code)."""
    tape = list(input_str)
    lines, result_tape, total_steps = run_machine(
        machine, tape, 0, machine["initial"]
    )
    halt_line = (
        [f"Machine halted after {total_steps} steps.", SEPARATOR]
        if result_tape is not None
        else [SEPARATOR]
    )
    return ([format_header(machine)] + lines + halt_line, 0 if result_tape is not None else 1)


def run(args: list[str]) -> tuple[list[str], int]:
    """Pure function: maps CLI args to (output_lines, exit_code). No side effects."""
    if len(args) == 1 and args[0] in ("-h", "--help"):
        return ([USAGE], 0)
    if len(args) != 2:
        return ([USAGE], 1)

    json_path, input_str = args[0], args[1]

    machine, load_err = load_machine(json_path)
    if load_err:
        return ([f"Error: {load_err}"], 1)

    validation_err = validate_machine(machine)
    if validation_err:
        return ([f"Error: {validation_err}"], 1)

    err = input_error(machine, input_str)
    if err:
        return ([f"Error: {err}"], 1)

    return simulate(machine, input_str)


def main():
    sys.setrecursionlimit(MAX_STEPS + 1000)
    lines, code = run(sys.argv[1:])
    print("\n".join(lines))
    sys.exit(code)


if __name__ == "__main__":
    main()
