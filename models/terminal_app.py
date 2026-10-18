from InquirerPy import inquirer
from runner import print_payment_schedule, view_expenses


class TerminalApp:
    def __init__(self):
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
            "View Expenses": view_expenses,
            "Exit": self.exit_app
        }

        menu_actions[choice]()

    def exit_app(self):
        print("Goodbye!")
        self.running = False
