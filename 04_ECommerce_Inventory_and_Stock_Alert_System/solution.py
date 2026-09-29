# Global database holding product inventory dictionaries
inventory = [
    {"item_name": "Laptop", "stock": 15, "price": 50000.0},
    {"item_name": "Smartphone", "stock": 4, "price": 20000.0},  # Low stock!
    {"item_name": "Headphones", "stock": 25, "price": 1500.0}
]

def update_stock(item_name: str, quantity_change: int) ->str :
   
    for product in inventory:   
        
        if product["item_name"] == item_name:       
            
            if product["stock"] + quantity_change < 0:
                raise ValueError("Not enough stock available, mama!")
               
            product["stock"] += quantity_change
            return product

    raise ValueError("Product not found in inventory!")

def check_low_stock(threshold: int=5) ->int:
    low_stock_list=[]
    for product in inventory:
         
         if product["stock"]<threshold:
             low_stock_list.append(f"{product['item_name']} is running low! Only {product['stock']} left.")

    return low_stock_list


def run_inventory_tests():
    print("--- 📦 Testing Stock Updates ---")
   
    try:
        print("Laptop sold 5:", update_stock("Laptop", -5))
        print("Headphones added 10:", update_stock("Headphones", 10))
        print("Smartphone available 4: reuriment 10:",update_stock("Smartphone", -10))
    except ValueError as error:
        print("Expected Error:", error)

    print("\n--- ⚠️ Testing Errors ---")
    print("\n--- 🚨 Low Stock Alerts ---")
    print("Alerts:", check_low_stock())

if __name__ == "__main__":
    run_inventory_tests()

