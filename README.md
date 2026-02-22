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

The `machines/` directory contains several example Turing machine configurations. Here is how each machine operates:

### `unary_add.json`
- **Goal**: Performs unary addition (e.g., `111.11` becomes `11111`).
- **Operation**: The machine scans the tape from left to right until it finds the `.` separator. It replaces the `.` with a `1` (effectively joining the two unary numbers). It then continues to the right end of the string and erases the last `1` (replacing it with a blank) to ensure the final count is exactly the sum of the two inputs.

### `unary_sub.json`
- **Goal**: Performs unary subtraction (e.g., `111-11=` becomes `1`).
- **Operation**: The machine scans right to find the `=` sign. It then moves left to find the last `1` of the subtrahend (right side of `-`) and marks it. It continues moving left past the `-` to find the last `1` of the minuend (left side of `-`) and erases it. This one-to-one cancellation repeats until the subtrahend is fully erased, leaving the result on the left.

### `palindrome.json`
- **Goal**: Decides if a binary string is a palindrome (writes `y` for yes, `n` for no).
- **Operation**: The machine reads the first character (`0` or `1`), erases it, and remembers it using its internal state. It then scans all the way to the right end of the string to check if the last character matches the remembered first character. If it matches, it erases it and scans all the way back to the left to repeat the process. If it finds a mismatch, it halts and writes `n`. If it successfully pairs all characters (or leaves at most one middle character), it halts and writes `y`.

### `0n1n.json`
- **Goal**: Decides the language $0^n1^n$ (a sequence of `0`s followed by an equal number of `1`s).
- **Operation**: The machine reads the first `0`, erases it, and scans all the way to the right end of the string. It checks if the last character is a `1`, erases it, and then scans all the way back to the left to find the next `0`. This outside-in matching continues until the string is empty (accepts with `y`). If it encounters characters out of order or an unequal number of `0`s and `1`s, it rejects and writes `n`.

### `02n.json`
- **Goal**: Decides the language $0^{2n}$ (checks if the string has an even number of `0`s).
- **Operation**: The machine simply scans the string from left to right, alternating between two states: `is_even` and `is_odd`. For every `0` it reads, it flips its state. When it reaches the end of the string (a blank character), it writes `y` if it is in the `is_even` state, and `n` if it is in the `is_odd` state.

### `universal.json`
- **Goal**: A Universal Turing Machine (UTM) capable of simulating any other Turing machine encoded on its tape.
- **Operation**: The tape contains an encoded description of a target machine's states and transitions, followed by the target machine's input string. The UTM reads its current simulated state, scans the encoded rules to find the matching transition for the current simulated tape symbol, updates the simulated tape, moves the simulated head, and updates its simulated state. This fetch-decode-execute cycle repeats until the simulated machine reaches a halt state.

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
