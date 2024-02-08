# user_interface
class UserInterface:
    def __init__(self, bank):
        self.bank = bank
        self.current_user = None

    def create_account(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type (Savings/Current): ").capitalize()

        user = self.bank.create_user_account(name, email, address, account_type)
        print(f"Account created successfully! Your account number is: {user['account_number']}")

    def login(self):
        account_number = int(input("Enter your account number: "))
        user = self.bank.get_user_by_account_number(account_number)
        if user:
            print(f"Welcome back, {user['name']}!")
            self.current_user = user
        else:
            print("Invalid account number. Please try again.")

    def deposit(self):
        if self.current_user:
            amount = float(input("Enter the amount to deposit: "))
            self.bank.deposit(self.current_user, amount)
            print(f"Deposited ${amount} successfully.")
        else:
            print("Please login first.")

    def withdraw(self):
        if self.current_user:
            amount = float(input("Enter the amount to withdraw: "))
            self.bank.withdraw(self.current_user, amount)
            print(f"Withdrew ${amount} successfully.")
        else:
            print("Please login first.")

    def check_balance(self):
        if self.current_user:
            print(f"Available balance: ${self.bank.check_balance(self.current_user)}")
        else:
            print("Please login first.")

    def view_transaction_history(self):
        if self.current_user:
            print("Transaction History:")
            for transaction in self.bank.transaction_history(self.current_user):
                print(transaction)
        else:
            print("Please login first.")

    def take_loan(self):
        if self.current_user:
            amount = float(input("Enter the loan amount: "))
            self.bank.take_loan(self.current_user, amount)
            print(f"Loan of ${amount} taken successfully.")
        else:
            print("Please login first.")

    def transfer_amount(self):
        if self.current_user:
            receiver_account_number = int(input("Enter the receiver's account number: "))
            amount = float(input("Enter the amount to transfer: "))
            self.bank.transfer_amount(self.current_user, receiver_account_number, amount)
        else:
            print("Please login first.")
