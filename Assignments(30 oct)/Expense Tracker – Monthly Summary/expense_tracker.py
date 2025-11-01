import os

def read_expenses(filename):
    records = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                parts = line.strip().split(',')
                if len(parts) != 3:
                    print(f"Warning: Malformed line {line_num} skipped (expected 3 fields, got {len(parts)})")
                    continue
                date, category, amount_str = parts
                try:
                    amount = float(amount_str)
                except ValueError:
                    print(f"Warning: Non-numeric amount on line {line_num} skipped")
                    continue
                records.append((date, category, amount))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the file name and try again.")
    return records

def calculate_summary(records):
    total_expense = 0
    category_expense = {}
    day_expense = {}
    for date, category, amount in records:
        total_expense += amount
        category_expense[category] = category_expense.get(category, 0) + amount
        day_expense[date] = day_expense.get(date, 0) + amount
    if day_expense:
        highest_day = max(day_expense, key=day_expense.get)
        highest_amount = day_expense[highest_day]
    else:
        highest_day = None
        highest_amount = 0
    summary = {
        'total_expense': total_expense,
        'category_expense': category_expense,
        'highest_day': highest_day,
        'highest_amount': highest_amount
    }
    return summary

def write_summary(summary, filename):
    if not summary or 'total_expense' not in summary:
        print("No summary data to write.")
        return

    month_year = "October 2025"  # static for this data
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"================= Expense Summary ({month_year}) =================\n")
            file.write(f"Total Monthly Expense: ₹{int(summary['total_expense']) if summary['total_expense'].is_integer() else summary['total_expense']}\n\n")
            file.write("Category-wise Breakdown:\n")
            for cat, amt in summary['category_expense'].items():
                file.write(f"{cat.ljust(14)}: ₹{int(amt) if amt.is_integer() else amt}\n")
            if summary['highest_day']:
                date = summary['highest_day']
                amount = int(summary['highest_amount']) if summary['highest_amount'].is_integer() else summary['highest_amount']
                file.write(f"\nHighest Spending Day: {date} (₹{amount})\n")
            file.write("Result updated.\n")
            file.write("=================================================================\n")
    except Exception as e:
        print(f"Error writing summary: {e}")

if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    input_file = r"c:/Users/DELL/Desktop/vs_code/Expense Tracker – Monthly Summary/expenses.csv"
    output_file = "monthly_summary.txt"

    records = read_expenses(input_file)
    if records:
        summary = calculate_summary(records)
        write_summary(summary, output_file)
        print(f"Report written to {output_file}")
    else:
        print("No expense records found.")
