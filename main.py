from time import sleep

# Enhanced Bank Account Management System

# 🏦 Data Structures to Store Information
account_holders = []  # Account names
balances = []  # Account balances
transaction_histories = []  # Account transaction logs
loans = []  # Account loan details

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03


def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")


def create_account(user_id: int, user: str, f_name: str, l_name: str) -> (list, int, list, int):
    """Create a new account."""

    new_account = [user_id, user, f_name, l_name]  # Create new list with user data
    new_balances = 0  # Create balance
    new_history = []  # Create history list
    new_loans = 0  # Create loan

    return new_account, new_balances, new_history, new_loans


def deposit():
    """Deposit money into an account."""
    pass  # TODO: Add logic


def withdraw():
    """Withdraw money from an account."""
    pass  # TODO: Add logic


def check_balance():
    """Check balance of an account."""
    pass  # TODO: Add logic


def list_accounts():
    """List all account holders and details."""
    pass  # TODO: Add logic


def transfer_funds():
    """Transfer funds between two accounts."""
    pass  # TODO: Add logic


def view_transaction_history():
    """View transactions for an account."""
    pass  # TODO: Add logic


def apply_for_loan():
    """Allow user to apply for a loan."""
    pass  # TODO: Add logic


def repay_loan():
    """Allow user to repay a loan."""
    pass  # TODO: Add logic


def identify_card_type():
    """Identify type of credit card."""
    pass  # TODO: Add logic


def username_check(user: str) -> bool:
    """Check if username exist"""
    for i in range(len(account_holders)):
        if account_holders[i][1] == user:
            return True
    return False


def main():
    """Run the banking system."""
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        # Map choices to functions
        if choice == 1:  # 1️⃣ Create Account

            print('\n' * 30)
            print("===================================")
            print(" 👤 Let's create your new account.")
            print("Please provide the following information:")

            while True:
                username = input("Choose a username: ").lower()
                username_exist = username_check(username)
                if username_exist:
                    print(f"Oops! That {username} is already taken. Please try a different one.")
                    continue
                break

            account_id = len(account_holders)  # ID is current account_holders len
            first_name = input("Enter your first name: ").title()
            last_name = input("Enter your last name: ").title()

            new_account, new_balances, new_history, new_loans = create_account(account_id, username, first_name,
                                                                               last_name)

            print("\nCreating your account...")

            account_holders.append(new_account)
            balances.append(new_balances)
            transaction_histories.append(new_history)
            loans.append(new_loans)

            sleep(3)
            print(f"Your account has been created successfully! 🎉 ")
            print(account_holders, balances, transaction_histories, loans)
            print(f"Thank you {first_name} {last_name} for choosing Enhanced Bank System. "
                  f"Enjoy your banking experience!")
            sleep(2)

        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            identify_card_type()
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")


if __name__ == "__main__":
    main()
