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

<details>
<summary>📝 <b>Click to view Part 4: Testing Verification Suite</b></summary>
<br>

Verify behavioral patterns by executing the following 4 distinct use cases inside a testing loop:
1. Valid Success Order using "MAMA10" coupon
2. Valid Success Order using "DISCOUNT20" coupon
3. Invalid Quantity entry (value 0)
4. Invalid Coupon Code entry
</details>
