

from InquirerPy import inquirer
from datetime import date
from budget_planner.ui.view_expenses import view_expenses
from budget_planner.storage.expense_csv import load_expenses


class TerminalApp:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.running = True

    def run(self):
        while self.running:
            self.main_menu()

    def main_menu(self):
        choice = inquirer.select(
            message="What action would you like to perform?",
            choices=[
                "View Expenses",
                "Exit"
            ],
        ).execute()

        menu_actions = {
            "View Expenses": self.show_expenses,
            "Exit": self.exit_app
        }

        menu_actions[choice]()

    def show_expenses(self):
        expenses = load_expenses(self.csv_path)
        view_expenses(expenses=expenses, day=date.today())

    def exit_app(self):
        print("Goodbye!")
        self.running = False
