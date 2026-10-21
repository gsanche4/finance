from budget_planner.ui.terminal_app import TerminalApp

CSV_PATH = 'data/expenses.csv'

if __name__ == "__main__":
    app = TerminalApp(CSV_PATH)
    app.run()
