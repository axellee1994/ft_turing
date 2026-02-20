# ft_turing

A functional implementation of a single infinite tape Turing machine in Python.
This project is part of the 42 curriculum.

## Description

The goal of this project is to simulate a Turing machine based on a JSON configuration file. The implementation respects the functional programming paradigm, preferring recursion and iterators over imperative loops.

The program reads a machine description from a JSON file and an input string, then simulates the machine execution step by step, displaying the state of the tape and the head position at each transition.

## Features

- **Functional Architecture**: Built using recursion and functional constructs.
- **JSON Configuration**: Machines are defined in easy-to-read JSON files.
- **Infinite Tape**: Simulation of a single infinite tape (extends dynamically).
- **Stepped Output**: Detailed visualization of the machine state at every step.

## Installation

Clone the repository:

```bash
git clone https://github.com/StartInB/ft_turing.git
cd ft_turing
```

No external dependencies are required. The project runs with standard Python 3.

## Usage

Run the simulator with a machine description and an input string:

```bash
# General syntax
python3 ft_turing.py [-h] jsonfile input
```

### Arguments

- `jsonfile`: Path to the JSON file describing the machine.
- `input`: The initial input string for the tape.
- `-h, --help`: Show help message.

### Example

To run the unary addition machine:

```bash
python3 ft_turing.py machines/unary_add.json "111.11"
```

## Included Machines

The `machines/` directory contains several example Turing machine configurations:

- **`unary_add.json`**: Performs unary addition (e.g., `11.111` becomes `11111`).
- **`unary_sub.json`**: Performs unary subtraction (e.g., `11-1=` becomes `1`).
- **`palindrome.json`**: Decides if the input is a palindrome (writes `y` or `n`).
- **`0n1n.json`**: Decides the language $0^n1^n$ (writes `y` or `n`).
- **`02n.json`**: Decides the language $0^{2n}$ (writes `y` or `n`).
- **`universal.json`**: A Universal Turing Machine capable of simulating other machines.

## Testing

A `Makefile` is provided for running tests on the included machines.

```bash
make run              # Runs default command
make test_unary_add   # Tests unary addition
make test_unary_sub   # Tests unary subtraction
make test_palindrome  # Tests palindrome machine
make test_0n1n        # Tests 0n1n machine
make test_02n         # Tests 02n machine
make test_universal   # Tests universal machine
```

To cleanup compiled python files:

```bash
make clean
```

## Machine Definition Format

Machines are defined in JSON with the following structure:

```json
{
    "name": "unary_add",
    "alphabet": [ "1", ".", "y", "n" ],
    "blank": ".",
    "states": [ "scanright", "addone", "HALT" ],
    "initial": "scanright",
    "finals": [ "HALT" ],
    "transitions": {
        "scanright": [
            { "read": "1", "to_state": "scanright", "write": "1", "action": "RIGHT" },
            { "read": ".", "to_state": "addone", "write": "1", "action": "RIGHT" }
        ]
    }
}
```
