# Banking App

This is a simple command-line banking application written in Python. The app allows users to perform basic banking operations such as transferring money, making deposits, withdrawing funds, changing PINs, and checking account balances. Users can also sign out and log in to another account, or exit the application.

## Features

- **User Authentication**: Log in with a username and password.
- **Money Transfer**: Transfer money to another registered user.
- **Deposit**: Add funds to your account.
- **Withdraw**: Withdraw funds from your account.
- **Change PIN**: Securely change your account PIN.
- **Check Balance**: View your current account balance.
- **Sign Out**: Log out and sign in as another user.
- **Exit**: Exit the application.

## Requirements

- Python 3.x
- `getpass` module (pre-installed in Python)

## How to Run

1. Clone or download the project to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to start the application:

    ```bash
    python banking_app.py
    ```

4. You will be prompted to log in with your username and password. 

## Usage

1. **Login**:
    - Enter your username and password to log in.
    - If you fail to log in after three attempts, the program will exit.

2. **Main Menu**:
    After logging in, you will be presented with the following options:

    1. **Transfer Money**: Transfer funds to another user by entering their username and the amount.
    2. **Deposit**: Add funds to your account by entering the amount you wish to deposit.
    3. **Withdraw**: Withdraw funds by specifying the amount.
    4. **Change PIN**: Change your account password/PIN securely.
    5. **Check Balance**: View your current account balance.
    6. **Sign Out**: Log out and log in with another account.
    7. **Exit**: Exit the application.

3. **Money Transfer**:
    - Enter the username of the person you want to transfer money to.
    - Specify the amount to transfer.

4. **Deposits and Withdrawals**:
    - For deposits and withdrawals, enter the amount, and the system will update your balance accordingly.

5. **Change PIN**:
    - Enter your current PIN, followed by your new PIN and confirmation to successfully change it.

6. **Exit**:
    - Select the "Exit" option to terminate the application.

## Example

```bash
--------------------------------------
     BANKING APP
--------------------------------------
Please Enter your username: menijay
Password: [hidden]
Successfully Signed In
Welcome menijay
Please Select an option:
1. Transfer Money
2. Deposit
3. Withdraw
4. Change PIN
5. Check Balance
6. Sign Out
7. Exit
Make your option: 1

--------------------------------------
     BANKING APP
--------------------------------------
Money Transfer
Enter the receiver's username (type 'quit' to cancel): john
Enter the amount to transfer: 100
Successfully transferred 100 to john.
New balance: 100
