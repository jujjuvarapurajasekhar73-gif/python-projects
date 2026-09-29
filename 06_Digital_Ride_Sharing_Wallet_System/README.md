# 📱 Project 06: Digital Ride Sharing Wallet System

A production-grade algorithmic digital wallet database simulator engineered to manage dynamic ride-sharing account capital flows, evaluate real-time fare deductions, and enforce strict boundary compliance using atomic transaction logging structures.

---

## 📋 Project Requirements & Technical Specifications

<details>
<summary>📝 <b>Click to view Part 1: Ledger Database Simulation & Helper Utilities</b></summary>
<br>

* **`wallets` (Global Register List):** Acts as the memory-backed master data directory tracking active user profiles.
* **Wallet Dictionary Schema:** Each profile object operates as a structured dictionary wrapping explicit entity coordinates:
  * `username` (Primary Unique String Key)
  * `balance` (Float Precision Ledger Factor)
  * `history` (Nested Container List Archiving Transaction Dictionaries)
* **`find_wallet(username: str) -> dict | None`**
  * Serves as an isolated internal scanner utility that sweeps the database list linearly. Returns the targeted wallet dictionary configuration instantly if a match is found; otherwise fields a clean `None` response.
</details>

<details>
<summary>📝 <b>Click to view Part 2: Secure Wallet Allocation Engine</b></summary>
<br>

* **`create_wallet(username: str, initial_amount: float) -> dict`**
  * **Capital Threshold Guard:** Validates that the input initialization deposit factor strictly exceeds 0 boundaries. If breached, triggers a transactional `ValueError` string exception.
  * **Identity Collision Gate:** Invokes the internal `find_wallet()` utility layer to audit existing records. Raises a descriptive `ValueError` if a duplicate entity signature attempts ingestion.
  * Commits the data mapping cleanly onto the memory pool register array and yields the generated profile tracker back to the system thread channel.
</details>

<details>
<summary>📝 <b>Click to view Part 3 & 4: Capital Mutation Pipelines (Deposit & Ride Payments)</b></summary>
<br>

* **`add_money(username: str, amount: float) -> float`**
  * Enforces positive validation criteria bounds (> 0) on incoming financial variables.
  * Audits account registry flags, increases the balance factor directly inline, injects a dynamic sub-dictionary transaction token (`"type": "Deposit"`) inside historical tracking rows, and returns the active current balance.
* **`pay_for_ride(username: str, ride_fare: float) -> float`**
  * Audits incoming parameters to safeguard network operations from negative limits.
  * **Solvency Check Gate:** Evaluates current cash balances against the target fare parameters. If the system detects insufficient funds, programmatically halts calculations and triggers an alert exception `ValueError`.
  * Deducts the ride cost metrics, pushes a log entry designated as `"Ride Payment"`, and returns the post-transaction net balance.
</details>

<details>
<summary>📝 <b>Click to view Part 5 & 6: Data Visualization & Stress Verification Suite</b></summary>
<br>

* **`show_wallet(username: str)`**
  * Queries localized user states to format and print the total available cash tracking balance alongside an explicit ledger stream detailing all historic operation logs sequentially.
* **Stress Verification Testing Engine Checkpoints (`run_wallet_tests`):**
  * Provisions a valid customer account registry profile model (`"surya"`).
  * Executes standard cash ingestion deposits (`add_money`).
  * Deducts standard ride fares cleanly (`pay_for_ride`).
  * Triggers an intentional overdraft transaction attack to audit error handling routines and resilience layers.
  * Outputs the final updated transaction statement dashboard dashboard layout on the terminal framework.
</details>
