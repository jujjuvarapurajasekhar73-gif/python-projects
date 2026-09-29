# 🏦 Project 05: Mini Banking System

A production-grade transactional banking database simulator developed to orchestrate dynamic balance adjustments, enforce secure overdraft protection limits, and chronologically archive structural statement registries utilizing robust error handling matrices.

---

## 📋 Project Requirements & Technical Specifications

<details>
<summary>📝 <b>Click to view Part 1: Ledger Database Simulation</b></summary>
<br>

* **`accounts` (Global Database List):** Houses the structured inventory registers of all client banking entities.
* **Account Dictionary Layout:** Each entity profile must maintain a structured dictionary layout wrapping explicit validation paths:
  * `name` (String Primary Client Key Identifier)
  * `balance` (Float Precision Capital Telemetry Metric)
  * `transactions` (Nested Core Sequential List Container Tracking Historic System Operations)
* **Transaction Dictionary Layout:** Each historical row token within the nested list must contain key-value pairings for `type` and `amount`.
</details>

<details>
<summary>📝 <b>Click to view Part 2: Secure Account Constructor</b></summary>
<br>

* **`create_account(name, initial_balance)`**
  * **Negative Asset Filter:** Audits baseline input values to ensure the `initial_balance` is non-negative. If violated, throws a `ValueError`.
  * **Identity Collision Guard:** Sweeps the existing ledger pool to prevent duplicate names. If a matching name is found, triggers a `ValueError`.
  * Commits the unique dictionary object configuration straight to the global memory grid and returns the newly generated record context.
</details>

<details>
<summary>📝 <b>Click to view Part 3 & 4: Capital Mutation Pipelines (Deposit & Withdraw)</b></summary>
<br>

* **`deposit(name, amount)`**
  * Verifies incoming financial quantity thresholds strictly exceed 0 parameters.
  * Locates the matching database record layout, increments the active balance factor, appends a transaction ledger row wrapping type `"Deposit"`, and yields the updated net balance.
* **`withdraw(name, amount)`**
  * Enforces positive validation criteria boundaries (> 0) on the input variable target.
  * **Overdraft Safety Gate:** Audits current accounting limits to ensure sufficient funds exist before executing any reductions. If the client tries to withdraw more than their balance, programmatically raises a descriptive `ValueError`.
  * Decrements the asset metric, injects a transaction log row designated as `"Withdrawal"`, and returns the final balance.
</details>

<details>
<summary>📝 <b>Click to view Part 5 & 6: Statement Visualization & Stress Test Suite</b></summary>
<br>

* **`show_account(name)`**
  * Loops through logs to clearly display the account profile name, current balance, and formats the entire tracking transaction ledger stream on the console interface.
* **Stress Verification Testing Engine Checkpoints:**
  * provisions at least one unique fresh customer account registry pass.
  * Fires multiple parallel deposit pipeline transactions.
  * Runs multiple successful withdrawal transactions.
  * Triggers an intentional overdraft limit failure breach to verify exception handling routes.
  * Attempts a duplicate data ingestion attack using an existing profile name to verify safety blocks.
  * Outputs the final detailed statement balance check dashboard cleanly.
</details>
