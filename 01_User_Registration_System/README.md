# 🔐 Project: Building a Secure User Registration System

This folder houses the official engineering requirements and structural documentation for the User Registration System. To view the implementation architecture, check the accompanying solution file.

---

## 📋 Project Requirements & Technical Specifications

<details>
<summary>📝 <b>Click to view Part 1: Database Simulation</b></summary>
<br>

* Create two global lists acting as data storage registries:
  * `registered_users`: Stores structured dictionary profiles of successfully validated users.
  * `failed_registrations`: Stores metadata captures and exception strings of failed registration attempts.
</details>

<details>
<summary>📝 <b>Click to view Part 2: Validation Functions</b></summary>
<br>

You must enforce the following validation constraints:
* **`validate_name(name)`**
  * The name must contain at least 3 characters.
  * Return `True` if valid, otherwise `False`.
* **`validate_email(email)`**
  * The email must contain both `@` and `.` characters.
  * Return `True` if valid, otherwise `False`.
* **`validate_password(password)`**
  * Must be at least 8 characters long.
  * Contains at least one uppercase letter.
  * Contains at least one numeric digit.
  * Return `True` if valid, otherwise `False`.
</details>

<details>
<summary>📝 <b>Click to view Part 3: Main Validation Orchestrator</b></summary>
<br>

* **`validate_user_data(name, email, password)`**
  * Calls the three independent validation sub-functions.
  * Programmatically raises a `ValueError` with a clear, descriptive context message if any check fails.
  * Return `True` if all validation layers pass successfully.
</details>

<details>
<summary>📝 <b>Click to view Part 4: Account Constructor</b></summary>
<br>

* **`create_user_account(name, email, password)`**
  * Invokes `validate_user_data()` to filter inputs.
  * Audits the `registered_users` registry for duplicate emails. If a collision is found, raises a `ValueError`.
  * If valid, creates a dictionary: `{"name": name, "email": email, "password": password, "status": "active"}`. Append to database list and return the record.
  * If any exception hits, catches the `ValueError`, stores the email and error message inside `failed_registrations`, and returns `None`.
</details>

<details>
<summary>📝 <b>Click to view Part 5: Testing Verification Suite</b></summary>
<br>

Verify behavioral patterns by executing the following 5 distinct use cases at the bottom of the script:
1. A valid registration pipeline pass
2. A duplicate email identity collision check
3. An invalid short name entry check
4. An invalid email formatting layout check
5. A weak password structure check
</details>

