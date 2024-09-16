import getpass
import os
import time

# Define the User class to store user details and manage account information
class User:
    users_details = []  # List to hold all users' information
    userID = []  # List to hold user objects

    def __init__(self, username="", password="", email="", phone="", acc_balance=0):
        # Initialize user object with necessary details
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.acc_balance = acc_balance
        main_user = {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "phone": self.phone,
            "acc_balance": self.acc_balance
        }
        User.userID.append(self)  # Add user object to userID list
        User.users_details.append(main_user)  # Add user details to users_details list

    # Method to update user details
    def updateUser(self, **kwargs):
        self.username = kwargs.get("username", self.username)
        self.password = kwargs.get("password", self.password)
        self.email = kwargs.get("email", self.email)
        self.phone = kwargs.get("phone", self.phone)
        self.acc_balance = kwargs.get("acc_balance", self.acc_balance)


# Function to print the app header
def header():
    print("--------------------------------------")
    print("\t BANKING APP")
    print("--------------------------------------")


# Function to clear the terminal screen (cross-platform)
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')


# Check if a username exists in the system
def check_users(username):
    for login in User.users_details:
        if login["username"] == username:
            return True
    return False


# Get user details by username
def get_user(username):
    for user in User.users_details:
        if user["username"] == username:
            return user
    return None


# Function to handle deposits
def deposit(username):
    clear_screen()
    header()
    print("\t Deposit")
    amount = int(input("Enter the amount to deposit: "))

    user = get_user(username)
    if user:
        user["acc_balance"] += amount  # Add the deposit amount to the balance
        print(f"{amount} has been deposited. New balance: {user['acc_balance']}")
    else:
        print("User not found.")


# Function to handle withdrawals
def withdraw(username):
    clear_screen()
    header()
    print("\t Withdraw")
    amount = int(input("Enter the amount to withdraw: "))

    user = get_user(username)
    if user:
        if user["acc_balance"] >= amount:  # Check if user has enough balance
            user["acc_balance"] -= amount  # Deduct the amount from the balance
            print(f"{amount} has been withdrawn. New balance: {user['acc_balance']}")
        else:
            print("Insufficient balance.")
    else:
        print("User not found.")


# Function to change the user's PIN
def change_pin(username):
    clear_screen()
    header()
    print("\t Change PIN")

    user = get_user(username)
    if user:
        old_pin = getpass.getpass("Enter your current PIN: ")
        if old_pin == user["password"]:  # Verify current PIN
            new_pin = getpass.getpass("Enter your new PIN: ")
            confirm_pin = getpass.getpass("Confirm your new PIN: ")

            if new_pin == confirm_pin:  # Check if new PINs match
                user["password"] = new_pin  # Update PIN
                print("Your PIN has been successfully changed.")
            else:
                print("New PINs do not match.")
        else:
            print("Incorrect current PIN.")
    else:
        print("User not found.")


# Function to transfer money from one user to another
def money_transfer(sender_username):
    clear_screen()
    header()
    print("\t Money Transfer")
    receiver_username = input("Enter the receiver's username (type 'quit' to cancel): ")

    if receiver_username == "quit":
        return "Transaction cancelled."

    if check_users(receiver_username):
        amount = int(input("Enter the amount to transfer: "))
        sender_user = get_user(sender_username)
        receiver_user = get_user(receiver_username)

        if sender_user and receiver_user:
            if sender_user["acc_balance"] >= amount:  # Check if sender has enough balance
                sender_user["acc_balance"] -= amount  # Deduct from sender
                receiver_user["acc_balance"] += amount  # Add to receiver
                print(f"Successfully transferred {amount} to {receiver_username}.")
                print(f"New balance: {sender_user['acc_balance']}")
            else:
                print("Insufficient balance.")
        else:
            print("User not found.")
    else:
        print("Receiver username does not exist.")


# Main application loop
def main():
    header()

    # Create two users for testing
    user1 = User(username="menijay", password="12345", phone="345345", acc_balance=200)
    user2 = User(username="john", password="12345", phone="123456", acc_balance=300)

    is_logged_in = False
    i = 0

    # Login process
    while i < 3:
        username = input("Please Enter your username: ")
        password = getpass.getpass()

        for login in User.users_details:
            if username == login["username"] and password == login["password"]:
                clear_screen()
                print("Successfully Signed In")
                header()
                print(f"Welcome {username}")
                is_logged_in = True
                break
        else:
            print("Incorrect Logins")

        if is_logged_in:
            break

        if i == 2:
            print("Tried too many times")
            return

        i += 1

    # Main menu loop after login
    while is_logged_in:
        print("Please Select an option:")
        print("1. Transfer Money")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Check Balance")
        print("6. Sign Out")
        print("7. Exit")

        option = int(input("Make your option: "))

        match option:
            case 1:
                money_transfer(sender_username=username)
            case 2:
                deposit(username)
            case 3:
                withdraw(username)
            case 4:
                change_pin(username)
            case 5:
                user = get_user(username)
                print(f"Your balance is: {user['acc_balance']}")
            case 6:
                # Sign out and log in to another account
                print("Signing out...")
                time.sleep(5)
                clear_screen()
                main()  # Call main function to restart login
                break
            case 7:
                # Exit the application
                print("Exiting...")
                is_logged_in = False
                break
            case _:
                print("Enter a valid option")


if __name__ == "__main__":
    clear_screen()
    main()
