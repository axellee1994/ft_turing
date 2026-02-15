import sys
import json
from simulator.parser import validate_machine
from simulator.engine import run_machine


def print_usage():
    print("usage: ft_turing [-h] jsonfile input")
    print()
    print("positional arguments:")
    print("    jsonfile     json description of the machine")
    print()
    print("    input        input of the machine")
    print()
    print("optional arguments:")
    print("    -h --help    show this help message and exit")


def main():
    # Just argument handlers
    args = sys.argv[1:]

    if len(args) != 2:
        if len(args) > 0 and args[0] in ["-h", "--help"]:
            print_usage()
            sys.exit(0)
        print_usage()
        sys.exit(1)

    json_path = args[0]
    input_str = args[1]

    # To load the JSON file
    try:
        with open(json_path, "r") as f:
            machine_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{json_path}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for file '{json_path}'.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON file - {e}")
        sys.exit(1)

    # Validating the machine data
    if not validate_machine(machine_data):
        print("Error: Invalid Turing machine definition.")
        sys.exit(1)

    # Now to check input vs alphabet. Blank character not allowed here
    if machine_data["blank"] in input_str:
        print("Error: Input string cannot contain the blank character.")
        sys.exit(1)

    # Make sure whatever characters we are inputting are in the alphabet
    if not all(char in machine_data["alphabet"] for char in input_str):
        print("Error: Input string contains characters not in the alphabet.")
        sys.exit(1)

    tape = list(input_str) if input_str else [machine_data["blank"]]
    print("*" * 20)
    print(f"Running {machine_data['name']}")
    print("*" * 20)

    # Run the machhine
    try:
        run_machine(machine_data, tape, 0, machine_data["initial"])
    except RecursionError:
        print("Error: Maximum recursion depth exceeded. Possible infinite loop.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Execution interrupted by user.")
        sys.exit(1)


if __name__ == "__main__":
    main()
