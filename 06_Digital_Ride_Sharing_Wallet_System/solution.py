#---------------------------------
# Simulate the Wallet Database
#---------------------------------

wallets = []

# -------------------------------------------------
# Helper Function: Find wallet
# -------------------------------------------------


def find_wallet(username:str):

    for wallet in wallets:
         if wallet["username"]== username:
             return wallet

    return None


# -------------------------------------------------
# Create Wallet Function
# -------------------------------------------------

def create_wallet(username: str, initial_amount: float):
    if initial_amount<=0:
        raise ValueError("The intial deposit must be greater than 0")
    
    if find_wallet(username):
        raise ValueError("already wallet existed on this name!")
    wallet={
                 "username": username,
                 "balance": initial_amount, 
                 "history": []
    }
    wallets.append(wallet)
    return wallet
# -------------------------------------------------
# Add Money Function
# -------------------------------------------------

def add_money(username: str, amount: float):
    if amount<=0:
        raise ValueError("Amount to add must be greater than zero.")
        
    wallet = find_wallet(username)
    if not wallet:
        raise ValueError(" wallet account not found! ")

    wallet["balance"]+=amount
        
    wallet["history"].append({
        "type":"Deposit",
        "amount":amount
    })

    return wallet["balance"]

# -------------------------------------------------
# pay ride  Function
# -------------------------------------------------
def pay_for_ride(username: str, ride_fare: float):
    
    if ride_fare<=0:
        raise ValueError(" ride_fare must be greater than zero! ")

    wallet=find_wallet(username)

    if not wallet:
        raise ValueError("wallet account not found")

    if wallet["balance"]< ride_fare:
        raise ValueError("wallet has insufficient balance")

    wallet["balance"]-= ride_fare

    wallet["history"].append({
        "type":"Ride Payment",
        "amount":ride_fare
    })

    return wallet["balance"]

# -------------------------------------------------
#  Show Wallet & Testing Engine
# -------------------------------------------------
def show_wallet(username:str):
    wallet=find_wallet(username)
    if not wallet:
        print("wallet account not found")
        return

    print(f"\n wallet account summary:{wallet['username']}")
    print(f"\n wallet available balance:{wallet['balance']}")

    print(f"wallet history:")
    if not wallet["history"]:
       print("no transaction recorded yet")

    else:
        for txn in wallet["history"]:
            print(f"{txn['type']}:{txn['amount']}")

# -------------------------------------------------
#  Run Test()
# -------------------------------------------------

def run_wallet_tests():
    try:
        create_wallet("surya", 500.0)
        add_money("surya", 150.0)
        pay_for_ride("surya", 80.0)
        
        pay_for_ride("surya", 1000.0)
    
    except ValueError as error:
        print("Error:", error)

    
    show_wallet("surya")


if __name__ == "__main__":
    run_wallet_tests()
