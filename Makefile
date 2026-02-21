.PHONY: all clean fclean re test test_unary_add test_0n1n test_02n test_palindrome test_universal

PYTHON := python3
NAME := ft_turing
MAIN := $(NAME).py

all: $(NAME)

$(NAME): $(MAIN)
	@echo "#!/bin/bash" > $(NAME)
	@echo '$(PYTHON) $(MAIN) "$$@"' >> $(NAME)
	@chmod +x $(NAME)
	@echo "$(NAME) executable successfully created!"

clean:
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete

fclean: clean
	@rm -f $(NAME)
	@echo "$(NAME) removed."

re: fclean all

test_0n1n:
	@echo "--- 0n1n: valid 0011 (expect y) ---"
	$(PYTHON) $(MAIN) machines/0n1n.json "0011"
	@echo "--- 0n1n: valid 000111 (expect y) ---"
	$(PYTHON) $(MAIN) machines/0n1n.json "000111"
	@echo "--- 0n1n: valid 01 (expect y) ---"
	$(PYTHON) $(MAIN) machines/0n1n.json "01"
	@echo "--- 0n1n: invalid 001 (expect n) ---"
	$(PYTHON) $(MAIN) machines/0n1n.json "001"
	@echo "--- 0n1n: invalid 0111 (expect n) ---"
	$(PYTHON) $(MAIN) machines/0n1n.json "0111"
	@echo "--- 0n1n: invalid 1100 (expect n) ---"
	$(PYTHON) $(MAIN) machines/0n1n.json "1100"

test_02n:
	@echo "--- 02n: valid 00 (expect y) ---"
	$(PYTHON) $(MAIN) machines/02n.json "00"
	@echo "--- 02n: valid 0000 (expect y) ---"
	$(PYTHON) $(MAIN) machines/02n.json "0000"
	@echo "--- 02n: valid 000000 (expect y) ---"
	$(PYTHON) $(MAIN) machines/02n.json "000000"
	@echo "--- 02n: invalid 0 (expect n) ---"
	$(PYTHON) $(MAIN) machines/02n.json "0"
	@echo "--- 02n: invalid 000 (expect n) ---"
	$(PYTHON) $(MAIN) machines/02n.json "000"
	@echo "--- 02n: invalid 00000 (expect n) ---"
	$(PYTHON) $(MAIN) machines/02n.json "00000"

test_palindrome:
	@echo "--- palindrome: 0110 (expect y) ---"
	$(PYTHON) $(MAIN) machines/palindrome.json "0110"
	@echo "--- palindrome: 010 (expect y) ---"
	$(PYTHON) $(MAIN) machines/palindrome.json "010"
	@echo "--- palindrome: 1 (expect y) ---"
	$(PYTHON) $(MAIN) machines/palindrome.json "1"
	@echo "--- palindrome: 11 (expect y) ---"
	$(PYTHON) $(MAIN) machines/palindrome.json "11"
	@echo "--- palindrome: 100 (expect n) ---"
	$(PYTHON) $(MAIN) machines/palindrome.json "100"
	@echo "--- palindrome: 10 (expect n) ---"
	$(PYTHON) $(MAIN) machines/palindrome.json "10"
	@echo "--- palindrome: 01110 (expect y) ---"
	$(PYTHON) $(MAIN) machines/palindrome.json "01110"

test_unary_add:
	@echo "--- unary_add: 1.1 (expect 11) ---"
	$(PYTHON) $(MAIN) machines/unary_add.json "1.1"
	@echo "--- unary_add: 11.111 (expect 11111) ---"
	$(PYTHON) $(MAIN) machines/unary_add.json "11.111"
	@echo "--- unary_add: 111.11 (expect 11111) ---"
	$(PYTHON) $(MAIN) machines/unary_add.json "111.11"
	@echo "--- unary_add: 1111.1 (expect 11111) ---"
	$(PYTHON) $(MAIN) machines/unary_add.json "1111.1"

test_unary_sub:
	@echo "--- unary_sub: 1-1= (expect 0) ---"
	$(PYTHON) $(MAIN) machines/unary_sub.json "1-1="
	@echo "--- unary_sub: 111-11= (expect 1) ---"
	$(PYTHON) $(MAIN) machines/unary_sub.json "111-11="
	@echo "--- unary_sub: 11111-111= (expect 11) ---"
	$(PYTHON) $(MAIN) machines/unary_sub.json "11111-111="
	@echo "--- unary_sub: 1111-1= (expect 111) ---"
	$(PYTHON) $(MAIN) machines/unary_sub.json "1111-1="

test_universal:
	$(PYTHON) $(MAIN) machines/universal.json "A^11.111|A11RAA.1RBB11RBB 1LCC1 LCH"

test: test_unary_add test_unary_sub test_palindrome test_0n1n test_02n test_universal
	@echo "--- help ---"
	$(PYTHON) $(MAIN) -h
