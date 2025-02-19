from time import sleep

# Enhanced Bank Account Management System
'''
# 🏦 Data Structures to Store Information
account_holders = []  # Account names
balances = []  # Account balances
transaction_histories = []  # Account transaction logs
loans = []  # Account loan details
'''

account_holders = [[0, 'gosho', 'Georgi', 'Todorov'], [1, 'jerry', 'Vasil', 'Iliev'], [2, 'kito', 'Kitodar', 'Todorov']]
balances = [4700.0, 3680.0, 7000.0]
transaction_histories = [[['Deposit', 5000.0], ['Withdraw', -300.0]],
                         [['Deposit', 2000.0], ['Deposit', 1250.0], ['Deposit', 800.0], ['Withdraw', -300.0],
                          ['Withdraw', -120.0], ['Deposit', 50.0]], [['Deposit', 12000.0], ['Withdraw', -5000.0]]]
loans = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

MIN_LOAN_AMOUNT = 1000
MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03
MIN_PERIOD_YEARS = 1
MAX_PERIOD_YEARS = 10


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


def create_account(user: str, f_name: str, l_name: str) -> str:
    """Create a new account."""
    user_id = len(account_holders)
    new_account = [user_id, user, f_name, l_name]  # Create new list with user data
    new_balances = 0.0  # Create balance
    new_history = []  # Create history list
    new_loans = [0, 0, 0, 0]  # Create loan

    print("\nCreating your account...")

    account_holders.append(new_account)
    balances.append(new_balances)
    transaction_histories.append(new_history)
    loans.append(new_loans)
    sleep(2)

    return "Your account has been created successfully! 🎉"


def deposit(user: str, value: float) -> str:
    """Deposit money into an account."""
    uid = find_id(user)
    history = ["Deposit", value]  # Initialize history list
    first_name, last_name = account_holders[uid][2], account_holders[uid][
        3]  # Get the user's first and last names for a personalized message
    value = round(value, 2)
    message = ''

    if value > 0:  # Check if the deposit value is valid (greater than zero)
        balances[uid] += value
        transaction_histories[uid].append(history)

        message = f"{first_name} {last_name} you have received a deposit of ${value:.2f}."

    else:
        message = "Error: Invalid amount. Please enter a positive number."

    return message


def withdraw(user: str, value: float) -> str:
    """Withdraw money from an account."""
    uid = find_id(user)
    history = ["Withdraw", -value]  # Initialize history list
    user_balance = balances[uid]  # Get the current balance of the user
    value = round(value, 2)  # Round the withdrawal value to two decimal places for precision
    message = ''

    if value <= 0:  # Check if the withdrawal value is greater than zero
        message = "Error: Please enter a valid withdrawal amount greater than zero."

    elif value > user_balance:  # Check if the user has sufficient funds
        message = f"Error: Insufficient funds to complete the withdrawal. Your balance is ${user_balance:.2f}."

    elif value <= user_balance:  # If the withdrawal value is valid, proceed with the transaction
        balances[uid] -= value
        transaction_histories[uid].append(history)

        message = f"Withdrawal successful! You have withdrawn ${value:.2f}."
    else:
        message = "Withdrawal failed. Please ensure the amount is valid."

    return message


def check_balance(user: str) -> str:
    """Check balance of an account."""
    uid = find_id(user)
    balance = balances[uid]

    return f'${balance:.2f}'


def list_accounts() -> None:
    """List all account holders and details."""

    print(f"ID  Username    Firstname  Lastname    Balance $      Remaining Loans $")
    for uid in range(len(account_holders)):  # Loop through all account holders
        print(f"{uid:<4}", end='')  # Print account ID, ensuring a minimum width of 4 characters for alignment
        print(f"{account_holders[uid][1]:<10}  {account_holders[uid][2]:<10} {account_holders[uid][3]:<10}",
              end=' ' * 4)
        print(f"{balances[uid]:.2f}", end=' ' * 6)  # Print the account balance with 2 decimal places, with some padding
        print(f"{loans[uid][0]:.2f}") if loans[uid][0] > 0 else print(
            "")  # Print the loan balance with 2 decimal places


def transfer_funds(sender: str, receiver: str, amount: float) -> str:
    """Transfer funds between two accounts."""
    uid_sender, uid_receiver = find_id(sender), find_id(receiver)
    sender_balance, receiver_balance = balances[uid_sender], balances[uid_receiver]
    value = round(amount, 2)
    history_type = "Transfer"
    history = [[history_type, value], [history_type, -value]]
    message = ''

    if value <= 0:
        message = "Error: Please enter a valid amount greater than zero."

    elif value > sender_balance:
        message = f"Error: Insufficient funds to complete the transfer. Sender balance is ${sender_balance:.2f}."

    elif value <= sender_balance:
        balances[uid_sender] -= value
        balances[uid_receiver] += value
        transaction_histories[uid_sender].append(history[0])
        transaction_histories[uid_receiver].append(history[1])

        message = f"The transfer of ${value:.2f} has been completed to {account_holders[uid_receiver][1]}"

    return message


def view_transaction_history(user: str, last_transactions: int) -> None:
    """View transactions for an account."""
    uid = find_id(user)  # Retrieve the unique user ID using the username
    history = range(len(transaction_histories[uid]))  # Generate a range for all transactions for the given user
    total_amount, negative, positive = 0.0, 0.0, 0.0  # Initialize variables for calculating total and categorized amounts

    if last_transactions in range(
            len(transaction_histories[uid]) + 1):  # Check if the input number of transactions is within the valid range
        if last_transactions != 0:  # If the user wants to see a specific number of recent transactions (not all)
            history = range(len(transaction_histories[uid]) - last_transactions, len(transaction_histories[uid]))

        print('No   Title      Amount [$]')
        for i in history:  # Loop through each transaction and print details
            title, amount = transaction_histories[uid][i]
            print(f"{i + 1}: {title:<10}  {amount:+.2f}")

            if amount > 0:  # Categorize the transaction amount as positive or negative
                positive += amount
            else:
                negative += amount

            total_amount += amount  # Keep a running total of all amounts
        print("-------------------------")
        print(f'  Balance: ${total_amount:+.2f}')

    else:  # Handle case when the input number is out of range
        print("Invalid input. The number entered is out of range. Please try again.")

    sleep(3)


def loan_calculator(loan: float, period_years: int) -> list:
    months = period_years * 12
    rate = INTEREST_RATE / 12
    monthly_pay = loan * (rate / (1 - (1 + rate) ** -months))
    monthly_pay = round(monthly_pay, 2)
    total_loan = round(monthly_pay * period_years * 12, 2)

    return [total_loan, monthly_pay, months, INTEREST_RATE]


def apply_for_loan(user: str, declared_loan: float, period: int) -> str:
    """Allow user to apply for a loan."""
    uid = find_id(user)
    declared_loan = round(declared_loan, 0)
    history = ["Loan Movement", declared_loan]
    message = ''
    is_valid = True

    if loans[uid][0] != 0:
        is_valid = False
        message += f"Error: User '{account_holders[uid][1]}' has a loan remaining of ${loans[uid][0]:.2f}.\n"

    if period > MAX_PERIOD_YEARS or period < MIN_PERIOD_YEARS:
        is_valid = False
        message += f"Error: The period needs to be greater than {MIN_PERIOD_YEARS} and smaller than {MAX_PERIOD_YEARS} years.\n"

    if declared_loan > MAX_LOAN_AMOUNT or declared_loan < MIN_LOAN_AMOUNT:
        is_valid = False
        message += f"Error: Please enter a loan amount between ${MIN_LOAN_AMOUNT} and ${MAX_LOAN_AMOUNT}.\n"

    if is_valid:
        created_loan = loan_calculator(declared_loan, period)
        loans[uid] = created_loan
        balances[uid] += declared_loan
        transaction_histories[uid].append(history)
        message += loan_status(user)

    return message


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


def empty_string(*args: str) -> bool:
    """ Check if any of the provided strings are empty  """
    if '' in args:
        return True
    return False


def find_id(username: str) -> int | None:
    """ Finds the id number of the username """
    for u_id in range(
            len(account_holders)):  # Iterate over all account holders by their index in the account_holders list
        if account_holders[u_id][1] == username:
            return u_id  # Return the index (user ID) of the account holder if a match is found
    return None


def loan_status(user) -> str:
    uid = find_id(user)
    message = ''

    if loans[uid][0] != 0:
        message = f'''
        Loan status for user '{account_holders[uid][1]}':
        Remaining loan: ${loans[uid][0]}
        Monthly payment: ${loans[uid][1]:.2f}
        Remaining months: {loans[uid][2]}
        Interest Rate: {loans[uid][3] * 100:.0f}% '''

    else:
        message = 'Error: No loans available yet..'

    return message


def test():
    print(f'account_holders = {account_holders}')
    print(f'balances = {balances}')
    print(f'transaction_histories = {transaction_histories}')
    print(f'loans = {loans}')


def main():
    """Run the banking system."""

    while True:
        display_menu()
        test()

        choice = int(input("Enter your choice: "))
        # Map choices to functions
        if choice == 1:  # 1️⃣ Create Account

            print("===================================")
            print(" 👤 Let's create your new account.")
            print("Please provide the following information:")

            while True:
                username = input("Choose a username: ").strip().lower()

                if username_check(username):
                    print(
                        f"Oops! That '{username}' is already taken. Please try a different one.")
                    sleep(1)
                    continue

                first_name = input("Enter your first name: ").strip().title()
                last_name = input("Enter your last name: ").strip().title()

                if empty_string(username, first_name, last_name):
                    print("Oops! The input you provided is invalid. Please try again.")
                    sleep(1)
                    continue

                break

            print(create_account(username, first_name, last_name))
            print(f"Thank you for choosing Enhanced Bank System. "
                  f"Enjoy your banking experience!")
            sleep(2)

        elif choice == 2:  # "2️⃣ Deposit Money"

            account = input("Please enter your account name: ").lower().strip()

            if username_check(account):

                deposit_value = float(input("Please enter the amount you'd like to deposit: "))
                print(deposit(account, deposit_value))

            else:
                print("Error: The username you entered does not exist. Please check and try again.")
            sleep(1)

        elif choice == 3:  # 3️⃣ Withdraw Money

            account = input("Please enter your account name: ").lower().strip()

            if username_check(account):

                withdraw_value = float(input("Enter the amount you'd like to withdraw: "))
                print(withdraw(account, withdraw_value))
                sleep(1)


            else:
                print("Error: The username you entered does not exist. Please check and try again.")

        elif choice == 4:  # "4️⃣ Check Balance"

            account = input("Please enter your account name: ").lower().strip()

            if username_check(account):
                account_balance = check_balance(account)
                print(f"Your current account balance is {account_balance}.")
                print("Thank you for banking with us!")

            else:
                print("Error: The username you entered does not exist. Please check and try again.")

            sleep(1)

        elif choice == 5:  # 5️⃣ List All Accounts
            list_accounts()

        elif choice == 6:
            # Sender Receiver
            sender_account = input("Please enter sender account name: ").lower().strip()
            receiver_account = input("Please enter receiver account name: ").lower().strip()

            sender_is_valid = username_check(sender_account)
            receiver_is_valid = username_check(receiver_account)

            if sender_is_valid and receiver_is_valid:
                amount = float(input("Enter the amount you wish to transfer."))
                print(transfer_funds(sender_account, receiver_account, amount))

            elif not receiver_is_valid:
                print("Receiver account not found. Please ensure the account number is correct.")


            elif not sender_is_valid:
                print("Sender account not found. Please ensure the account number is correct.")

            sleep(2)


        elif choice == 7:

            account = input("Please enter your account name: ").lower().strip()

            if username_check(account):
                uid = find_id(account)
                history_length = len(transaction_histories[uid])
                transactions = int(input(
                    f"Enter 0 to see all transactions or input a number (<= {history_length}) to view the last [X] transactions."))
                view_transaction_history(account, transactions)



        elif choice == 8:
            account = input("Please enter your account name: ").lower().strip()
            period_years = int(
                input(f"Please enter a period between {MIN_PERIOD_YEARS} and {MAX_PERIOD_YEARS} years: "))
            loan_amount = float(input(f"Enter a loan amount between ${MIN_LOAN_AMOUNT} and ${MAX_LOAN_AMOUNT}:"))

            if username_check(account):
                print(apply_for_loan(account, loan_amount, period_years))
            else:
                print("Error: The username you entered does not exist. Please check and try again.")
            sleep(2)

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
