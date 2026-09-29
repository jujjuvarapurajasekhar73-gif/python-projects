# 📊 Project 03: Expense Tracking System

An optimized memory-backed asset tracking system developed to dynamically log multi-category expenditures, compute relational aggregated financial balances, and handle structural parameter audits with robust data compliance filters.

---

## 📋 Project Requirements & Technical Specifications

<details>
<summary>📝 <b>Click to view Part 1: Database Simulation</b></summary>
<br>

* Create a single foundational global tracking register database:
  * `expenses` (List): An ordered dynamic data collection container engineered to house individual transaction logs.
  * **Data Object Blueprint:** Each separate transaction ledger slot must be wrapped inside a structured dictionary containing explicit keys for: `amount`, `category`, and `description`.
</details>

<details>
<summary>📝 <b>Click to view Part 2: Expense Ingestion Framework</b></summary>
<br>

* **`add_expense(amount, category, description)`**
  * **Financial Threshold Guard:** Audits incoming numeric fields to verify that the target transaction `amount` strictly exceeds 0.
  * **Exception Routine:** Programmatically fires a clear, descriptive `ValueError` context string if an invalid or negative financial quantity is pushed.
  * **State Commitment:** Maps verified inputs into a standalone transaction dictionary framework, appends the record onto the master database list, and yields the newly generated object map back to the caller stream.
</details>

<details>
<summary>📝 <b>Click to view Part 3 & 4: Aggregation & Analytical Modules</b></summary>
<br>

* **`calculate_total_expenses()`**
  * Iterates across the entire chronological expense register pool using loop matrices, computes the sum total of every committed ledger amount parameter, and returns the accumulated balance.
* **`calculate_total_by_category(category)`**
  * Runs conditional sorting sweeps through historical entries, isolating and compiling numeric parameters strictly for items matching the specified query string category target, and yields the filtered outcome.
</details>

<details>
<summary>📝 <b>Click to view Part 5 & 6: Data Visualization & Testing Suite</b></summary>
<br>

* **`show_expenses()`**
  * Formats and prints all recorded financial rows clearly on the terminal stream for systemic audit checking loops.
* **Verification Matrix Checkpoints:**
  * Appends multiple structured ledger rows sequentially.
  * Inputs at least one intentional negative failure boundary value to verify exception catching.
  * Outputs the final aggregated global budget totals, category specific indexes, and prints the full database configuration model cleanly.
</details>
