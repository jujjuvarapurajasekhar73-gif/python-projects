"""
User Registration System

A simple user registration module that demonstrates:
- Validation functions
- Exception handling
- Duplicate checking
- Basic in-memory storage
"""


# -------------------------------------------------------------------
# Simulated Database
# -------------------------------------------------------------------


registered_users=[]
failed_registrations=[]

# -------------------------------------------------------------------
# Validation Functions
# -------------------------------------------------------------------


#validate_name(name)The name must contain at least 3 characters.
#Return True if the name is valid, otherwise return False.

def valid_name(name:str) -> bool:

    """
    Validate that the name contains at least 3 characters.

    Args:
        name (str): The user's name.

    Returns:
        bool: True if valid, otherwise False.
    """
    if len(name) >=3:
        return True
    else:
        return False        

#The email must contain both "@" and ".".
#Return True if the email format is valid, otherwise return False.

def validate_email(email:str) ->bool:
    
    """
    Validate that the email contains both '@' and '.'.

    Args:
        email (str): The user's email address.

    Returns:
        bool: True if valid, otherwise False.
    """
    return "@" in email and "." in email

#The password must meet all of the following conditions:
#At least 8 characters long
#Contains at least one uppercase letter
#Contains at least one digit
#Return True if the password is valid, otherwise return False.

def valid_password(password:str) -> bool:

    """
    Validate the password strength.

    Rules:
        - At least 8 characters long
        - Contains at least one uppercase letter
        - Contains at least one digit

    Args:
        password (str): The user's password.

    Returns:
        bool: True if valid, otherwise False.
    """

    if len(password)>=8:
        has_upper=any(char.isupper() for char in password)
        has_digit=any(char.isdigit() for char in password)
        return has_upper and has_digit
    else:
        return False

#Create a Main Validation Function
#Create an orchestrator function called validate_user_data(name, email, password)
#This function must:
#Call the three validation functions you created
# Raise a ValueError with a clear and descriptive message if any validation fails
# Return True if all validations pass successfully

         
def valid_user_data(name: str, email: str, password: str) ->bool:

    """
    Validate all user inputs.

    Args:
        name (str): The user's name.
        email (str): The user's email.
        password (str): The user's password.

    Returns:
        bool: True if all validations pass.

    Raises:
        ValueError: If any validation rule fails.
    """

    if not valid_name(name):
        raise ValueError("The name must contain at least 3 characters.")

    if not validate_email(email):
        raise ValueError("The email must contain both '@' and '.' .")

    if not valid_password(password):
        raise ValueError(
            "At least 8 characters long."
            "Contains at least one uppercase letter."
            "Contains at least one digit."
        )
    return True



def create_user_account(name: str, email: str, password: str) ->bool:

    """
    Create a new user account after validation.

    Args:
        name (str): The user's name.
        email (str): The user's email.
        password (str): The user's password.

    Returns:
        dict: User dictionary if registration succeeds.
        None: If registration fails.

    Raises:
        ValueError: Internally raised during validation or duplicate checks.
    """

    try:
        valid_user_data(name,email,password)
        if any(user ["email"]==email for user in registered_users):
             raise ValueError("An account with this email already exists.")


        new_user = {
            "name": name,
            "email": email,
            "password": password,
            "status": "active",
                         
        }

        registered_users.append(new_user)

        return new_user

    except ValueError as error:
            failed_registrations.append({"email": email, "error": str(error)})
    return None

def run_tests():
    """
    Execute sample registration scenarios.

    Returns:
        None
    """
    test_cases = [
        ("Baraa", "baraa@email.com", "Password1"),
        ("AnotherUser", "baraa@email.com", "Password1"),
        ("Al", "al@email.com", "Password1"),
        ("Sarah", "sarah@email.com", "weakpass"),
    ]

    for index, (name, email, password) in enumerate(test_cases, start=1):
        print(f"\nTest {index}")
        result = create_user_account(name, email, password)

        if result:
            print("Registration successful:", result)
        else:
            print("Registration failed.")

    print("\nFinal Registered Users:")
    print(registered_users)

    print("\nFailed Registrations:")
    print(failed_registrations)
run_tests()



