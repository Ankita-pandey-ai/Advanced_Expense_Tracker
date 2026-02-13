import matplotlib.pyplot as plt
import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
    except FileExistsError:
        pass


def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!\n")


def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) <= 1:
            print("No expenses found.\n")
            return

        print("\nDate        Amount    Category    Description")
        print("-" * 50)

        for row in rows[1:]:  # skip header
            date, amount, category, description = row
            print(f"{date:<12}{amount:<10}{category:<12}{description}")

        print()

def show_total():
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            total += float(row[1])

    print(f"\nTotal Spending: {total}\n")

def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            category = row[2]
            amount = float(row[1])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    print("\nCategory Summary")
    print("-" * 30)
    for category, total in summary.items():
        print(f"{category:<15}{total}")

    print()

def monthly_summary():
    month_input = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            date = row[0]
            amount = float(row[1])

            if date.startswith(month_input):
                total += amount

    print(f"\nTotal spending for {month_input}: {total}\n")

def category_chart():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[2]
            amount = float(row[1])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    if not summary:
        print("No data to display.")
        return

    categories = list(summary.keys())
    amounts = list(summary.values())

    plt.figure(figsize=(6,6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution by Category")
    plt.show()


def main():
    initialize_file()

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spending")
        print("4. Category Summary")
        print("5. Monthly Summary")
        print("6. Show Category Chart")
        print("7. Exit")


        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            category_chart()
        elif choice == "7":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
