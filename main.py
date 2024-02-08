# main
import random
from user_interface import UserInterface
from admin_interface import AdminInterface

class Bank:
    def __init__(self):
        self.users = []
        self.admins = []
        self.is_loan_enabled = True

    def generate_account_number(self):
        return random.randint(100000, 999999)

    def create_user_account(self, name, email, address, account_type):
        account_number = self.generate_account_number()
        user = {
            'name': name,
            'email': email,
            'address': address,
            'account_type': account_type,
            'account_number': account_number,
            'balance': 0,
            'transaction_history': [],
            'loan_taken': 0,
        }
        self.users.append(user)
        return user

    def get_user_by_account_number(self, account_number):
        for user in self.users:
            if user['account_number'] == account_number:
                return user
        return None

    def deposit(self, user, amount):
        user['balance'] += amount
        user['transaction_history'].append(f"Deposited ${amount}")

    def withdraw(self, user, amount):
        if amount > user['balance']:
            print("Withdrawal amount exceeded")
        else:
            user['balance'] -= amount
            user['transaction_history'].append(f"Withdrew ${amount}")

    def check_balance(self, user):
        return user['balance']

    def transaction_history(self, user):
        return user['transaction_history']

    def take_loan(self, user, amount):
        if user['loan_taken'] < 2:
            user['balance'] += amount
            user['loan_taken'] += 1
            user['transaction_history'].append(f"Loan taken: ${amount}")
        else:
            print("Cannot take more than two loans.")

    def transfer_amount(self, sender, receiver_account_number, amount):
        receiver = self.get_user_by_account_number(receiver_account_number)
        if receiver:
            if amount > sender['balance']:
                print("Insufficient funds for transfer.")
            else:
                sender['balance'] -= amount
                receiver['balance'] += amount
                sender['transaction_history'].append(f"Transferred ${amount} to {receiver['name']}")
                receiver['transaction_history'].append(f"Received ${amount} from {sender['name']}")
        else:
            print("Account does not exist.")

# Example usage:
bank = Bank()
user_interface = UserInterface(bank)
admin_interface = AdminInterface(bank)

while True:
    print("\n1. Create Account\n2. Login\n3. Deposit\n4. Withdraw\n5. Check Balance\n6. View Transaction History\n"
          "7. Take Loan\n8. Transfer Amount\n9. Admin Operations\n10. Exit")
    choice = input("Enter your choice (1-10): ")

    if choice == '1':
        user_interface.create_account()
    elif choice == '2':
        user_interface.login()
    elif choice == '3':
        user_interface.deposit()
    elif choice == '4':
        user_interface.withdraw()
    elif choice == '5':
        user_interface.check_balance()
    elif choice == '6':
        user_interface.view_transaction_history()
    elif choice == '7':
        user_interface.take_loan()
    elif choice == '8':
        user_interface.transfer_amount()
    elif choice == '9':
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")
        if admin_username == "Niloy" and admin_password == "niloy.cs":
            print("\n1. Create User Account\n2. Delete User Account\n3. All User Accounts\n"
                  "4. Total Available Balance\n5. Total Loan Amount\n6. Toggle Loan Feature\n7. Back")
            admin_choice = input("Enter your admin choice (1-7): ")
            if admin_choice == '1':
                admin_interface.create_user_account()
            elif admin_choice == '2':
                admin_interface.delete_user_account()
            elif admin_choice == '3':
                admin_interface.all_user_accounts()
            elif admin_choice == '4':
                admin_interface.total_available_balance()
            elif admin_choice == '5':
                admin_interface.total_loan_amount()
            elif admin_choice == '6':
                admin_interface.toggle_loan_feature()
            elif admin_choice == '7':
                continue
        else:
            print("Invalid admin credentials. Access denied.")
    elif choice == '10':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
