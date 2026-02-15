.PHONY: all clean test run

PYTHON := python3
NAME := ft_turing
MAIN := $(NAME).py

all: run

run:
	$(PYTHON) $(MAIN)

test:
	$(PYTHON) $(MAIN) -h
	$(PYTHON) $(MAIN) machines/unary_sub.json "1-1=1" 2>&1 | head -20 || true

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
