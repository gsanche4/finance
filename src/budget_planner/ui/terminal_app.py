from InquirerPy import inquirer
from datetime import date
from budget_planner.ui.view_expenses import view_expenses
from budget_planner.storage.expense_csv import load_expenses


class TerminalApp:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.running = True

    def run(self):
        try:
            while self.running:
                self.show_main_menu()
        except KeyboardInterrupt:
            print("\nGoodbye!")

    def show_main_menu(self):
        menu_actions = {
            "View Upcoming Expenses": self.show_upcoming_expenses,
            "Exit": self.quit,
        }
        choice = inquirer.select(
            message="What action would you like to perform?",
            choices=list(menu_actions),
        ).execute()
        menu_actions[choice]()

    def show_upcoming_expenses(self):
        try:
            expenses = load_expenses(self.csv_path)
        except (OSError, ValueError) as error:
            print(f"Could not load expenses: {error}")
            return
        view_expenses(expenses=expenses, today=date.today())

    def quit(self):
        print("Goodbye!")
        self.running = False
