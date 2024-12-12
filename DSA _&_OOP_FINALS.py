import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime


class ExpenseTrackerUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")
        self.master.configure(bg="#1E1E1E")

        self.expenses = []

        self.title_label = tk.Label(
            master,
            text="💵 Expense Tracker 💵",
            bg="#1E1E1E",
            fg="#FFD700",
            font=("Arial", 20, "bold")
        )
        self.title_label.pack(pady=10)

        self.date_label = tk.Label(
            master,
            text="Select Date:",
            bg="#1E1E1E",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.date_label.pack(pady=5)

        date_frame = tk.Frame(master, bg="#1E1E1E")
        date_frame.pack(pady=5)

        current_year = datetime.now().year
        self.year_var = tk.IntVar(value=current_year)
        self.year_dropdown = ttk.Combobox(
            date_frame,
            textvariable=self.year_var,
            values=[current_year - i for i in range(10)],
            width=5,
            state="readonly"
        )
        self.year_dropdown.pack(side="left", padx=5)

        self.month_var = tk.IntVar(value=datetime.now().month)
        self.month_dropdown = ttk.Combobox(
            date_frame,
            textvariable=self.month_var,
            values=list(range(1, 13)),
            width=5,
            state="readonly"
        )
        self.month_dropdown.pack(side="left", padx=5)

        self.day_var = tk.IntVar(value=datetime.now().day)
        self.day_dropdown = ttk.Combobox(
            date_frame,
            textvariable=self.day_var,
            values=list(range(1, 32)),
            width=5,
            state="readonly"
        )
        self.day_dropdown.pack(side="left", padx=5)

        self.category_label = tk.Label(
            master,
            text="Category:",
            bg="#1E1E1E",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.category_label.pack(pady=5)
        self.category_entry = tk.Entry(
            master,
            bg="#2E2E2E",
            fg="white",
            font=("Arial", 14),
            width=30,
            bd=3,
            relief="groove",
        )
        self.category_entry.pack(pady=5)

        self.amount_label = tk.Label(
            master,
            text="Amount:",
            bg="#1E1E1E",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(
            master,
            bg="#2E2E2E",
            fg="white",
            font=("Arial", 14),
            width=30,
            bd=3,
            relief="groove",
        )
        self.amount_entry.pack(pady=5)

        self.description_label = tk.Label(
            master,
            text="Description:",
            bg="#1E1E1E",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.description_label.pack(pady=5)
        self.description_entry = tk.Entry(
            master,
            bg="#2E2E2E",
            fg="white",
            font=("Arial", 14),
            width=30,
            bd=3,
            relief="groove",
        )
        self.description_entry.pack(pady=5)

        button_frame = tk.Frame(master, bg="#1E1E1E")
        button_frame.pack(pady=20)

        self.add_button = tk.Button(
            button_frame,
            text="Add Expense ➕",
            command=self.add_expense,
            bg="#32CD32",
            fg="black",
            font=("Arial", 10, "bold"),
            width=15,
            relief="raised",
            bd=3,
        )
        self.add_button.grid(row=0, column=0, padx=5)

        self.update_button = tk.Button(
            button_frame,
            text="Update Expense ✏️",
            command=self.update_expense,
            bg="#FFA500",
            fg="black",
            font=("Arial", 10, "bold"),
            width=15,
            relief="raised",
            bd=3,
        )
        self.update_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(
            button_frame,
            text="Delete Expense ❌",
            command=self.delete_expense,
            bg="#FF4500",
            fg="black",
            font=("Arial", 10, "bold"),
            width=15,
            relief="raised",
            bd=3,
        )
        self.delete_button.grid(row=0, column=2, padx=5)

        self.search_button = tk.Button(
            button_frame,
            text="Search by Category 🔍",
            command=self.search_by_category,
            bg="#1E90FF",
            fg="black",
            font=("Arial", 10, "bold"),
            width=20,
            relief="raised",
            bd=3,
        )
        self.search_button.grid(row=0, column=3, padx=5)

        self.summary_button = tk.Button(
            button_frame,
            text="Generate Summary 📊",
            command=self.generate_summary,
            bg="#FFD700",
            fg="black",
            font=("Arial", 10, "bold"),
            width=20,
            relief="raised",
            bd=3,
        )
        self.summary_button.grid(row=1, column=0, columnspan=4, pady=10)

        self.expenses_label = tk.Label(
            master,
            text="📜 Expense List 📜",
            bg="#1E1E1E",
            fg="#87CEEB",
            font=("Arial", 14, "bold")
        )
        self.expenses_label.pack(pady=10)

        self.expenses_text = tk.Text(
            master,
            height=15,
            width=80,
            bg="#2E2E2E",
            fg="white",
            font=("Arial", 12),
            bd=3,
            relief="groove",
        )
        self.expenses_text.pack(pady=5)

        self.footer = tk.Label(
            master,
            text="💡 Designed by JKL Productions",
            bg="#1E1E1E",
            fg="#FFD700",
            font=("Arial", 10, "italic")
        )
        self.footer.pack(side="bottom", pady=10)

    def add_expense(self):
        """Add a new expense to the list."""
        year = self.year_var.get()
        month = self.month_var.get()
        day = self.day_var.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        description = self.description_entry.get()

        try:
            date = datetime(year, month, day).strftime("%Y-%m-%d")
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid date or amount!")
            return

        if not category or not description:
            messagebox.showerror("Error", "Category and description cannot be empty!")
            return

        expense = f"{date} | {category} | ₱{amount:.2f} | {description}"
        self.expenses.append(expense)
        self.update_expenses_text()
        self.clear_fields()

    def delete_expense(self):
        """Delete the selected expense."""
        selected_line = self.expenses_text.index(tk.INSERT).split(".")[0]
        try:
            self.expenses.pop(int(selected_line) - 1)
            self.update_expenses_text()
        except IndexError:
            messagebox.showerror("Error", "No expense selected!")

    def update_expense(self):
        """Update a selected expense."""
        selected_line = self.expenses_text.index(tk.INSERT).split(".")[0]
        try:
            expense = self.expenses[int(selected_line) - 1]
            date, category, amount, description = expense.split(" | ")
            year, month, day = map(int, date.split("-"))

            self.year_var.set(year)
            self.month_var.set(month)
            self.day_var.set(day)
            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(0, category.strip())
            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, amount.strip("$"))
            self.description_entry.delete(0, tk.END)
            self.description_entry.insert(0, description.strip())

            self.expenses.pop(int(selected_line) - 1)
            self.update_expenses_text()
        except IndexError:
            messagebox.showerror("Error", "No expense selected!")

    def search_by_category(self):
        """Filter expenses by category."""
        category = self.category_entry.get().strip().lower()
        if not category:
            messagebox.showerror("Error", "Enter a category to search!")
            return

        filtered_expenses = [e for e in self.expenses if category in e.split(" | ")[1].lower()]
        if not filtered_expenses:
            messagebox.showinfo("Search Result", f"No expenses found for category '{category}'.")
        else:
            self.expenses_text.delete("1.0", tk.END)
            self.expenses_text.insert(tk.END, "\n".join(filtered_expenses) + "\n")

    def generate_summary(self):
        """Generate summary of expenses by month or year."""
        summary = {}
        for expense in self.expenses:
            date, _, amount, _ = expense.split(" | ")
            year, month, _ = date.split("-")
            key = f"{year}-{month}"
            summary[key] = summary.get(key, 0) + float(amount.strip("₱"))

        summary_text = "Summary by Month:\n\n"
        for key, total in summary.items():
            summary_text += f"{key}: ₱{total:.2f}\n"

        messagebox.showinfo("Summary Report", summary_text)

    def update_expenses_text(self):
        """Update the expense list display."""
        self.expenses_text.delete("1.0", tk.END)
        for expense in self.expenses:
            self.expenses_text.insert(tk.END, expense + "\n")

    def clear_fields(self):
        """Clear all input fields."""
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerUI(root)
    root.mainloop()
