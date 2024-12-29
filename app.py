from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "expenses.json"

def read_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def write_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@app.route("/")
def home():
    expenses = read_data()
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["POST"])
def add_expense():
    expenses = read_data()
    new_expense = {
        "id": len(expenses) + 1,
        "description": request.form["description"],
        "amount": float(request.form["amount"]),
        "category": request.form["category"]
    }
    expenses.append(new_expense)
    write_data(expenses)
    return redirect(url_for("home"))

@app.route("/delete/<int:expense_id>")
def delete_expense(expense_id):
    expenses = read_data()
    expenses = [expense for expense in expenses if expense["id"] != expense_id]
    write_data(expenses)
    return redirect(url_for("home"))

@app.route("/update/<int:expense_id>", methods=["GET", "POST"])
def update_expense(expense_id):
    expenses = read_data()
    expense = next((e for e in expenses if e["id"] == expense_id), None)
    if request.method == "POST":
        if expense:
            expense["description"] = request.form["description"]
            expense["amount"] = float(request.form["amount"])
            expense["category"] = request.form["category"]
            write_data(expenses)
        return redirect(url_for("home"))
    return render_template("update.html", expense=expense)

if __name__ == "__main__":
    app.run(debug=True)
