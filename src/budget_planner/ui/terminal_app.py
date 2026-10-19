

from InquirerPy import inquirer
from budget_planner.ui.print_payment_schedule import print_payment_schedule
from budget_planner.ui.view_expenses import view_expenses


class TerminalApp:
    def __init__(self, data_path):
        self.data_path = data_path
        self.running = True

    def run(self):
        while self.running:
            self.main_menu()

    def main_menu(self):
        choice = inquirer.select(
            message="What action would you like to perform?",
            choices=[
                "View Payment Schedule by Expense",
                "View Expenses",
                "Exit"
            ],
        ).execute()

        menu_actions = {
            "View Payment Schedule by Expense": print_payment_schedule,
            "View Expenses": self.show_expenses,
            "Exit": self.exit_app
        }

        menu_actions[choice]()

    def show_expenses(self):
        view_expenses(self.data_path)

    def exit_app(self):
        print("Goodbye!")
        self.running = False
