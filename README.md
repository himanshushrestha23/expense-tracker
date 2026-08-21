# Expense Tracker

## Description

A simple command-line application built in Python to manage personal expenses. The application allows users to add, view, update, delete, and calculate the total of expenses through a menu-driven interface. Expense information is stored using Python dictionaries and saved to a text file so expenses persist after closing the program.

## Features

* Add a new expense.
* View all expenses.
* Update an existing expense.
* Delete an expense.
* Calculate total expenses.
* Validate user input.
* Load saved expenses when the program starts.
* Save expenses to a file when the program exits.

## Technologies Used

* Python 3
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* File handling
* Exception handling

## How to Run

1. Clone this repository.
2. Open the project folder.
3. Run:

```bash
python expense_tracker.py
```

The program will create `expenses.txt` when expenses are saved for the first time.

## How It Works

Each expense is stored as a dictionary containing its description, amount, and category.

```python
{"description": "Lunch", "amount": 300, "category": "Food"}
```

These dictionaries are stored inside a list called `expenses`.

The program uses a menu-driven interface to let the user add, view, update, delete, and calculate expenses.

## File Storage

Expenses are stored in `expenses.txt` using the following format:

```text
Lunch:300:Food
Bus:50:Transport
Movie:500:Entertainment
```

When the program starts, it reads the file and converts each line into an expense dictionary.

When the user exits, the current expenses are written back to the file.

## What I Learned

* Using lists and dictionaries to manage structured data.
* Organizing a program into functions.
* Building menu-driven command-line applications.
* Validating and handling user input.
* Managing and updating data stored in a list.
* Reading and writing data using text files.
* Converting file data into dictionary data and vice versa.

## Future Improvements

* Add expense dates.
* Filter expenses by category.
* Add monthly expense summaries.
* Improve input validation for descriptions and categories.
