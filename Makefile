# Add to .PHONY at the top
.PHONY: all clean test run test_unary_add test_0n1n test_02n test_palindrome test_universal

PYTHON := python3
NAME := ft_turing
MAIN := $(NAME).py

all: run

run:
	$(PYTHON) $(MAIN)

test_0n1n:
	$(PYTHON) $(MAIN) machines/0n1n.json "0011"

test_02n:
	$(PYTHON) $(MAIN) machines/02n.json "000"

test_palindrome:
	$(PYTHON) $(MAIN) machines/palindrome.json "0110"

test_unary_add:
	$(PYTHON) $(MAIN) machines/unary_add.json "11.111"

test_unary_sub:
	$(PYTHON) $(MAIN) machines/unary_sub.json "1-1=1"

test_universal:
	$(PYTHON) $(MAIN) machines/universal.json "A^11.111|A11RAA.1RBB11RBB 1LCC1 LCH"

test: test_0n1n test_02n test_palindrome test_unary_add test_unary_sub test_universal
	$(PYTHON) $(MAIN) -h

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
