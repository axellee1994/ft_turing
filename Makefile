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
	$(PYTHON) $(MAIN) machines/0n1n.json "0011"
	$(PYTHON) $(MAIN) machines/0n1n.json "000111"
	$(PYTHON) $(MAIN) machines/0n1n.json "01"

test_02n:
	$(PYTHON) $(MAIN) machines/02n.json "00"
	$(PYTHON) $(MAIN) machines/02n.json "0000"
	$(PYTHON) $(MAIN) machines/02n.json "000000"

test_palindrome:
	$(PYTHON) $(MAIN) machines/palindrome.json "0110"
	$(PYTHON) $(MAIN) machines/palindrome.json "010"
	$(PYTHON) $(MAIN) machines/palindrome.json "1"
	$(PYTHON) $(MAIN) machines/palindrome.json "11"
	$(PYTHON) $(MAIN) machines/palindrome.json "100"
	$(PYTHON) $(MAIN) machines/palindrome.json "10"
	$(PYTHON) $(MAIN) machines/palindrome.json "01110"

test_unary_add:
	$(PYTHON) $(MAIN) machines/unary_add.json "1.1"
	$(PYTHON) $(MAIN) machines/unary_add.json "11.111"
	$(PYTHON) $(MAIN) machines/unary_add.json "111.11"
	$(PYTHON) $(MAIN) machines/unary_add.json "1111.1"

test_unary_sub:
	$(PYTHON) $(MAIN) machines/unary_sub.json "1-1="
	$(PYTHON) $(MAIN) machines/unary_sub.json "111-11="
	$(PYTHON) $(MAIN) machines/unary_sub.json "11111-111="
	$(PYTHON) $(MAIN) machines/unary_sub.json "1111-1="

test_universal:
	$(PYTHON) $(MAIN) machines/universal.json "A^11.111|A11RAA.1RBB11RBB  LCC1 LH"

test: test_unary_add test_unary_sub test_palindrome test_0n1n test_02n test_universal
	$(PYTHON) $(MAIN) -h
