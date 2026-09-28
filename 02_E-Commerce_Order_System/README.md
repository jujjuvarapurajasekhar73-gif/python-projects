# 🛒 Project 02: E-Commerce Order System

An optimized, condition-driven order processing engine developed to dynamically evaluate shopping carts, handle custom coupon discount codes, and process transactions cleanly utilizing atomic exception failure logging gates.

---

## 📋 Project Requirements & Technical Specifications

<details>
<summary>📝 <b>Click to view Part 1: Database Simulation</b></summary>
<br>

* Create two global lists acting as data storage registries:
  * `successful_orders`: Stores structured dictionary invoices of successfully processed transactions.
  * `failed_orders`: Logs chronological metadata collections and exception messages of failed orders.
</details>

<details>
<summary>📝 <b>Click to view Part 2: Order Validation Constraints</b></summary>
<br>

* **`validate_order_data(quantity, coupon_code, price)`**
  * **Quantity Check:** Enforces that the item quantity must exceed 0. If 0 or negative, raise a `ValueError`.
  * **Price Check:** Enforces that the unit price must be greater than 0. If invalid, raise a `ValueError`.
  * **Coupon Check:** Validates input coupon codes against approved whitelist criteria. If unapproved, raise a `ValueError`.
</details>

<details>
<summary>📝 <b>Click to view Part 3: Main Order Processing Engine</b></summary>
<br>

* **`process_order(item_name: str, quantity: int, coupon_code: str, price: float)`**
  * **System Logic Blueprint:** Must contain a structured `try-except ValueError` fault tolerance block.
  * **🟢 Inside the `try:` Block (8 spaces indentation):**
    * **Call Validation:** Invokes `validate_order_data(quantity, coupon_code, price)` immediately to filter inputs.
    * **Calculate Initial Bill:** Computes the base total price via: `total = quantity * price`.
    * **Apply Discount Coupon Rules:** Evaluates an `if-elif` sequence to apply a custom updated discount system:
      * **Rule 1:** If `coupon_code == "MAMA10"`, subtract a flat 10 from the total.
      * **Rule 2:** If `coupon_code == "DISCOUNT20"`, subtract a flat 22 from the total.
    * **Create Order Record:** Packages a dictionary called `order_invoice` containing: `{"item": item_name, "total_bill": total, "status": "processed"}`.
    * **Append to Database:** Appends this invoice dictionary to the global `successful_orders` list and returns the invoice.
  * **🔴 Inside the `except ValueError as error:` Block (8 spaces indentation):**
    * **Log Failed Orders:** If an error occurs, catches it and logs a tracking payload: `failed_orders.append({"item": item_name, "error_msg": str(error)})`.
    * **Return None:** Concludes the failure branch by writing `return None`.
</details>

---

## 💻 Live E-Commerce Testing Engine Blueprint

<details>
<summary>💻 <b>Click to view Production Execution Setup</b></summary>
<br>

```python
# ==============================================================================
# PART 1: GLOBAL DATABASE TRACKING REGISTERS
# ==============================================================================
successful_orders = []
failed_orders = []

# ==============================================================================
# PART 2: CORE VALIDATION LAYER
# ==============================================================================
def validate_order_data(quantity, coupon_code, price):
    if quantity <= 0:
        raise ValueError("Invalid Quantity: Transaction parameter must exceed 0 pieces.")
    if price <= 0:
        raise ValueError("Invalid Price: Item unit cost must be a positive value.")
    if coupon_code and coupon_code not in ["MAMA10", "DISCOUNT20", ""]:
        raise ValueError(f"Unapproved Breach: Coupon code '{coupon_code}' is invalid.")
    return True

# ==============================================================================
# PART 3: MAIN SYSTEM INVOICE CONSTRUCTOR
# ==============================================================================
def process_order(item_name: str, quantity: int, coupon_code: str, price: float):
    try:
        # 1. Fire validation orchestrator check
        validate_order_data(quantity, coupon_code, price)
        
        # 2. Calculate base initial bill
        total = quantity * price
        
        # 3. Apply custom coupon rules hierarchy 
        if coupon_code == "MAMA10":
            total -= 10
        elif coupon_code == "DISCOUNT20":
            total -= 22
            
        # 4. Create structured record invoice
        order_invoice = {
            "item": item_name,
            "total_bill": total,
            "status": "processed"
        }
        
        # 5. Commit transaction to database
        successful_orders.append(order_invoice)
        return order_invoice
        
    except ValueError as error:
        # 6. Fallback recovery logging track
        failed_orders.append({
            "item": item_name,
            "error_msg": str(error)
        })
        return None

# ==============================================================================
# PART 4: AUTOMATED VERIFICATION TESTING SUITE
# ==============================================================================
def run_order_tests():
    test_orders = [
        ("Laptop", 1, "MAMA10", 50000.0),         # 1. Valid Success Order (-10)
        ("Smartphone", 2, "DISCOUNT20", 25000.0), # 2. Valid Success Order (-22)
        ("Headphones", 0, "", 1500.0),            # 3. Invalid Quantity (0)
        ("Mouse", 2, "WRONG50", 800.0)            # 4. Invalid Coupon Code
    ]
    
    for index, (item, qty, coupon, prc) in enumerate(test_orders, start=1):
        print(f"\nProcessing Order {index} ({item}):")
        invoice = process_order(item, qty, coupon, prc)
        
        if invoice:
            print(f"✅ Success! Invoice Generated: {invoice}")
        else:
            print("❌ Order Failed.")

    print("\n==============================")
    print("📦 FINAL SUCCESSFUL ORDERS DATABASE:")
    print(successful_orders)
    print("\n⚠️ FINAL FAILED ORDERS DATABASE:")
    print(failed_orders)

# Trigger test loop live!
run_order_tests()
```
</details>

<details>
<summary>🖥️ <b>Click to view Expected Terminal Output</b></summary>
<br>

```text
Processing Order 1 (Laptop):
✅ Success! Invoice Generated: {'item': 'Laptop', 'total_bill': 49990.0, 'status': 'processed'}

Processing Order 2 (Smartphone):
✅ Success! Invoice Generated: {'item': 'Smartphone', 'total_bill': 49978.0, 'status': 'processed'}

Processing Order 3 (Headphones):
❌ Order Failed.

Processing Order 4 (Mouse):
❌ Order Failed.

==============================
📦 FINAL SUCCESSFUL ORDERS DATABASE:
[{'item': 'Laptop', 'total_bill': 49990.0, 'status': 'processed'}, {'item': 'Smartphone', 'total_bill': 49978.0, 'status': 'processed'}]

⚠️ FINAL FAILED ORDERS DATABASE:
[{'item': 'Headphones', 'error_msg': 'Invalid Quantity: Transaction parameter must exceed 0 pieces.'}, {'item': 'Mouse', 'error_msg': "Unapproved Breach: Coupon code 'WRONG50' is invalid."}]
```
</details>
