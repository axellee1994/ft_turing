.PHONY: all clean test run

PYTHON := python3
NAME := ft_turing
MAIN := $(NAME).py

all: run

run:
	$(PYTHON) $(MAIN)

test_unary_sub:
	$(PYTHON) $(MAIN) -h
	$(PYTHON) $(MAIN) machines/unary_sub.json "1-1=1" 2>&1 | head -20 || true

test_0n1n:
	$(PYTHON) $(MAIN) -h
	$(PYTHON) $(MAIN) machines/0n1n.json "0011" 2>&1 | head -20 || true

test_02n:
	$(PYTHON) $(MAIN) -h
	$(PYTHON) $(MAIN) machines/02n.json "000" 2>&1 | head -20 || true

test_palindrome:
	$(PYTHON) $(MAIN) -h
	$(PYTHON) $(MAIN) machines/palindrome.json "0110" 2>&1 | head -20 || true

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
