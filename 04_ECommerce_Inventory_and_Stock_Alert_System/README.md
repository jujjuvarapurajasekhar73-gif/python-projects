# 📦 Project 04: E-Commerce Inventory & Stock Alert System

A high-performance memory-backed database engine developed to orchestrate dynamic warehouse asset modifications, evaluate algorithmic restock indicators, and safeguard pipelines from inventory deficits using custom validation checks.

---

## 📋 Project Requirements & Technical Specifications

<details>
<summary>📝 <b>Click to view Part 1: Database Architecture</b></summary>
<br>

* **`inventory` (List Container Database):** Acts as the foundational data store tracking product levels inside memory heap layouts.
* **Data Object Blueprint:** Each internal register record must follow a standardized dynamic dictionary blueprint structure configuration wrapping explicit attributes:
  * `item_name` (String Identifier Key)
  * `stock` (Integer Quantity Tracking Metric)
  * `price` (Float Precision Valuation Factor)
</details>

<details>
<summary>📝 <b>Click to view Part 2: Dynamic Stock Update Engine</b></summary>
<br>

* **`update_stock(item_name: str, quantity_change: int) -> dict`**
  * Parses the global warehouse directory database layout rows step-by-step to match the incoming identifier string array input.
  * **Guard Clause Validation Boundary:** Checks if the combined calculation (`current_stock + quantity_change`) drops below 0 boundaries. If breached, raises an atomic transactional `ValueError` code loop message: `"Not enough stock available, mama!"`.
  * **Fallback Validation Boundary:** If the entire scanner pipeline finishes parsing and yields 0 tracking matches, throws a distinct `ValueError` context: `"Product not found in inventory!"`.
  * Commits state changes directly inside the data object grid and returns the target record matrix back to the invocation layer thread.
</details>

<details>
<summary>📝 <b>Click to view Part 3: Algorithmic Low Stock Monitoring Subsystem</b></summary>
<br>

* **`check_low_stock(threshold: int = 5) -> list`**
  * Operates as an automated real-time monitoring sentinel loop sweeps system.
  * Leverages a default argument fallback threshold level (bounded at value 5) to audit item quantity values cleanly.
  * Collects structural warning alert string arrays for every product container breaching the low inventory threshold floor limits, returning an aggregated diagnostics report index list.
</details>

<details>
<summary>📝 <b>Click to view Part 4: System Integration Test Timeline Suite</b></summary>
<br>

Verify systemic execution resilience properties inside `run_inventory_tests()` by checking:
1. Valid transaction order sales logs processing sweeps (e.g., deducting quantities from Laptop).
2. Valid stock entry additions processing sweeps (e.g., increments on Headphones metrics).
3. Intentional out-of-stock validation check breaches (e.g., over-drafting from Smartphone low stocks registers).
4. Automated system sweeps retrieving critical low supply warning metrics inline.
</details>
