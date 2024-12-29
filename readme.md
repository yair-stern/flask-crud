# Expense Manager

## Overview
A simple CRUD app for managing expenses using Python, Flask, and JSON. HTML templates are rendered with Jinja for minimalistic, self-contained functionality.

## Features
- **Create**: Add expenses (description, amount, category).
- **Read**: View all expenses.
- **Update**: Edit expense details.
- **Delete**: Remove expenses.

## Requirements
- Python 3.7+
- Flask

## Installation
1. Clone the repository and navigate to the folder:
   ```bash
   git clone <repository_url>
   cd expense_manager
   ```
2. Install Flask:
   ```bash
   pip install flask
   ```
3. Create a JSON file:
   ```bash
   echo "[]" > expenses.json
   ```

## Usage
1. Run the app:
   ```bash
   python app.py
   ```
2. Open `http://127.0.0.1:5000/` in your browser.

## Structure
- **app.py**: Main file
- **expenses.json**: Database
- **templates/**:
  - **index.html**: List expenses
  - **add.html**: Add new expenses
  - **update.html**: Edit expenses

## Routes
- `/`: List expenses
- `/add`: Add expense (GET/POST)
- `/update/<int:id>`: Edit expense (GET/POST)
- `/delete/<int:id>`: Remove expense (POST)

## JSON Format
```json
{
    "id": 1,
    "description": "Groceries",
    "amount": 50.00,
    "category": "Food"
}
```

## Notes
- IDs are auto-incremented.
- Ensure `expenses.json` is writable.

---
This project demonstrates basic CRUD with Flask and JSON.

