# admin_interface
class AdminInterface:
    def __init__(self, bank):
        self.bank = bank

    def create_user_account(self):
        name = input("Enter user's name: ")
        email = input("Enter user's email: ")
        address = input("Enter user's address: ")
        account_type = input("Enter account type (Savings/Current): ").capitalize()

        return self.bank.create_user_account(name, email, address, account_type)

    def delete_user_account(self):
        account_number = int(input("Enter the account number to delete: "))
        user = self.bank.get_user_by_account_number(account_number)
        if user:
            self.bank.users.remove(user)
            print(f"Account {account_number} deleted.")
        else:
            print("Account not found.")

    def all_user_accounts(self):
        print("All User Accounts:")
        for user in self.bank.users:
            print(user)

    def total_available_balance(self):
        total_balance = sum(user['balance'] for user in self.bank.users)
        print(f"Total Available Balance: ${total_balance}")

    def total_loan_amount(self):
        total_loan = sum(user['loan_taken'] for user in self.bank.users)
        print(f"Total Loan Amount: ${total_loan}")

    def toggle_loan_feature(self):
        self.bank.is_loan_enabled = not self.bank.is_loan_enabled
        status = "enabled" if self.bank.is_loan_enabled else "disabled"
        print(f"Loan feature is now {status}.")
