# AI-Based Password Generator

A beginner-friendly Python password generator project. It creates strong,
random passwords using uppercase letters, lowercase letters, numbers, and
special characters.

> **Technical note:** This starter version uses Python's `secrets` module
> for secure randomness. It is a rule-based password generator, not a
> machine-learning model. The project title can be changed to
> **Secure Password Generator** for a more technically accurate description.

## Features

- Choose a password length from 8 to 64 characters.
- Choose which character types to include.
- Ensures at least one character from each selected type.
- Uses Python's `secrets` module instead of the ordinary `random` module.
- No external packages required.

## Requirements

- Python 3.8 or newer

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Files

- `main.py` — password generator program
- `requirements.txt` — external dependencies (none required)

## Learning concepts

- Functions
- User input and output
- Conditional statements
- Strings and character groups
- Exception handling
- Python's `secrets` module

## Responsible use

Use unique passwords for your accounts and store them in a reputable
password manager. Never publish real passwords, API keys, or private
credentials in this repository.
