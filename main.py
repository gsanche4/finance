from budget_planner.ui.terminal_app import TerminalApp

FILEPATH = 'data/expenses.csv'

if __name__ == "__main__":
    app = TerminalApp(FILEPATH)
    app.run()
