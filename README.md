# ft_turing

**Summary:** This project is a functional implementation of a single infinite tape Turing machine.

**Version:** 3.2

## Table of Contents

- [Forewords](#forewords)
- [Introduction](#introduction)
- [Objectives](#objectives)
- [Generic Rules](#generic-rules)
- [Mandatory Part](#mandatory-part)
- [Submission and Peer-Evaluation](#submission-and-peer-evaluation)

---

## Forewords

Alan Mathison Turing was a British pioneering computer scientist and mathematician who provided a formalisation of the concepts of algorithm and computation with the Turing machine.He is widely considered the father of theoretical computer science and artificial intelligence.

---

## Introduction

The Turing machine is a mathematical model that is fairly easy to understand and implement.This project involves creating a functional implementation of such a machine with a single infinite tape.

---

## Objectives

The goal is to write a program capable of simulating a Turing machine from a machine description provided in JSON.The project must be written respecting the functional paradigm. Iterators like `map`, `fold`, or `filter` are preferred over imperative loops.

---

## Generic Rules

- You are free to use any language and its basic libraries.
- Libraries that "do all the work for you" are forbidden.
- You must not rely on imperative style; use constants and anonymous functions. 
- If using OCaml, a Makefile must be provided to handle compilation and OPAM dependencies.

---

## Mandatory Part

### The Simulator
The program must simulate a Turing machine based on a JSON parameter.
- **Usage:** `./ft_turing [-h] jsonfile input`
- **Output:** The program must display the state of the tape and the head position at each transition.
- **Robustness:** The program must detect and reject invalid descriptions and never crash.

### Machine Descriptions
You must provide 5 JSON machine descriptions:
1. **Unary addition.**
2. **Palindrome decider** (writes 'y' or 'n' on the tape).
3. **$0^n1^n$ language decider** (writes 'y' or 'n' on the tape).
4. **$0^{2n}$ language decider** (writes 'y' or 'n' on the tape).
5. **Universal machine:** A machine that runs the first machine (unary addition).

---

## Submission and Peer-Evaluation

Turn in your assignment in your Git repository.Only the work inside the repository will be evaluated during the defense.Ensure your folders and files are correctly named.