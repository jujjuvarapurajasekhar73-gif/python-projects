successful_orders = []
failed_orders = []

def valid_quantity(quantity: int) ->bool:
    """
     
     Args: Order quantity must be greater than zero.
     
     Return: 
        bool: True if valid, otherwise False.
     
    """
    if quantity > 0:
          return True
    else:
          return False

def valid_coupon(coupon_code: str) ->bool:
    """
     Rule: The system only accepts two special coupons: "MAMA10" or "DISCOUNT20". 
     If no coupon is passed (empty string ""), it is also valid. 
     Any other coupon code is invalid.
     
     
    Returns:
        bool:if coupon_code is in ["MAMA10", "DISCOUNT20", ""]. Return True or False.
    
    """
    if coupon_code in ["MAMA10", "DISCOUNT20", ""]:
        return True
    else:
         return False

def valid_price(price: float) -> bool:
    """
    Rule: The product item price must be greater than zero (> 0).
    
    Returns:
        bool: Check the price value and return a boolean.
        
    """
    if  price>0:
         return True
    else:
        return False


def validate_order_data(quantity: int, coupon_code: str, price: float):

     if not valid_quantity(quantity):
          raise ValueError("Atleast add one item in your cart")
     
     if not valid_coupon(coupon_code):
          raise ValueError("Invalid coupon code provided.")
     
     if not valid_price(price):
          raise ValueError("The product item price must be greater than zero > 0")
     
     
     return True


def process_order(item_name: str, quantity: int, coupon_code: str, price: float):
     
     try:
          validate_order_data(quantity, coupon_code, price)
          
          total = quantity * price

          if coupon_code == "MAMA10":
               total =total-10
               
          elif coupon_code == "DISCOUNT20":
               total = total - 22
             
         

          order_invoice={
               "item": item_name, 
               "total_bill": total,
               "status": "processed",
            }

          successful_orders.append(order_invoice)
          return order_invoice

     except ValueError as error:
          failed_orders.append({"item": item_name, "error_msg": str(error)})
          return None


def run_order_tests():
    # This is our list of test orders to check our system behavior
    test_orders = [
        ("Laptop", 1, "MAMA10", 50000.0),       # 1. Valid Order with 10rs discount (Success)
        ("Smartphone", 2, "DISCOUNT20", 25000.0),# 2. Valid Order with 20rs discount (Success)
        ("Headphones", 0, "", 1500.0),          # 3. Invalid Quantity: 0 (Should Fail)
        ("Mouse", 2, "WRONG50", 800.0)          # 4. Invalid Coupon Code (Should Fail)
    ]
    
    # Looping through each test order using enumerate starting from count 1
    for index, (item_name, quantity, coupon_code, price) in enumerate(test_orders, start=1):
        print(f"\n--- Processing Order {index},{item_name} ---")
        
        # Calling your main manager function here
        invoice = process_order(item_name, quantity, coupon_code, price)
        
        if invoice:
            print(f" Registration Success! Invoice: {invoice}")
        else:
            print(" Registration Failed.")

    # Printing final summary report of our database lists
    print("\n========================================")
    print(" FINAL SUCCESSFUL ORDERS DATABASE:")
    print(successful_orders)
    
    print("\n FINAL FAILED ORDERS DATABASE:")
    print(failed_orders)

# 👈 Remember to call the function at the very end to execute it!
run_order_tests()

          

         
