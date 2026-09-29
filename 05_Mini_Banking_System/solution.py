"""
Mini Banking System

A simple banking system that allows:
- Account creation
- Deposits
- Withdrawals
- Transaction tracking
- Account summary display
"""
# -------------------------------------------------
# Simulated Database
# -------------------------------------------------

accounts=[ ]


# -------------------------------------------------
# Helper Function: Find Account
# -------------------------------------------------

def find_account(name:str):
    """
    Find an account by name.

    Args:
        name (str): Account holder name.

    Returns:
        dict: Account dictionary if found.
        None: If account does not exist.
    """
    for account in accounts:
        if account["name"]==name:
            return account
    return None



# -------------------------------------------------
# Create Account
# -------------------------------------------------

def create_account (name: str, intialbalance: float):
    """
    Create a new bank account.

    Args:
        name (str): Account holder name.
        initial_balance (float): Starting balance.

    Returns:
        dict: Created account dictionary.

    Raises:
        ValueError: If balance is negative or account exists.
    """
    if intialbalance < 0:
        raise ValueError("The initialbalance not negative")
    
    if find_account(name):
        raise ValueError("Account with this name already exists.")

    account={"name":name, 
             "balance":intialbalance, 
             "transaction":[]
    }

    accounts.append(account)
    return account

# -------------------------------------------------
# Deposit
# -------------------------------------------------

def deposit(name:str, amount:float):
    """
    Deposit money into an account.

    Args:
        name (str): Account holder name.
        amount (float): Amount to deposit.

    Returns:
        float: Updated balance.

    Raises:
        ValueError: If amount is invalid or account not found.
    """
    
    if amount<=0:
        raise ValueError("Deposit amount must be greater than 0.")
    
    account=find_account(name)
    
    if not account:
        raise ValueError("Deposit amount must be greater than 0.")
    
    account["balance"]+=amount
    
    account["transaction"].append({
        "type":"Deposit",
        "amount":amount
    })

    return account["balance"]


# -------------------------------------------------
# Withdraw
# -------------------------------------------------

def withdraw(name:str, amount:float):
    """
    Withdraw money from an account.

    Args:
        name (str): Account holder name.
        amount (float): Amount to withdraw.

    Returns:
        float: Updated balance.

    Raises:
        ValueError: If insufficient funds or invalid amount.
    """
    if amount<=0:
        raise ValueError("withdrawl amount must be greater than 0")
    
    account=find_account(name)

    if not account:
        raise ValueError("account not found!")
    
    if account["balance"]<amount:
        raise ValueError("insufficient balance in your account")
    
    account["balance"]-=amount

    account["transaction"].append({
        "type":"withdrawl",
        "amount":amount
    })

    return account["balance"]


# -------------------------------------------------
# Show Account Summary
# -------------------------------------------------

def show_account(name: str):
    """
    Display account summary including transactions.

    Args:
        name (str): Account holder name.
    """
    account = find_account(name)

    if not account:
        print("Account not found.")
        return

    print(f"\nAccount Summary for {account['name']}")
    print(f"Current Balance: ${account['balance']}")

    print("Transaction:")
    if not account["transaction"]:
        print("No transactions yet.")
    else:
        for transaction in account["transaction"]:
            print(f"- {transaction['type']} : ${transaction['amount']}")

# -------------------------------------------------
# Testing Section
# -------------------------------------------------


def run_tests():
    try:
        create_account("Raja", 1000)
        deposit("Raja", 200)
        withdraw("Raja", 150)
        withdraw("Raja", 2000)  # Overdraft test

    except ValueError as error:
        print("Error:", error)

    show_account("Raja")


run_tests()
