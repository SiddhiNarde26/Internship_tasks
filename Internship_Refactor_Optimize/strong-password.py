import re

# --- Constants ---
MIN_PASSWORD_LENGTH = 8
# You can add more constants here if needed for future criteria, e.g.:
# HAS_SPECIAL_CHAR = True

# --- Regex Patterns (Compiled Once) ---
# This pattern checks for any character (except newline) at least MIN_PASSWORD_LENGTH times.
_EIGHT_CHARS_REGEX = re.compile(rf".{{{MIN_PASSWORD_LENGTH},}}")
_UPPERCASE_REGEX = re.compile(r"[A-Z]+")
_LOWERCASE_REGEX = re.compile(r"[a-z]+")
_DIGIT_REGEX = re.compile(r"\d+")


# --- Helper Functions for Password Checks ---
def _has_min_length(password: str) -> bool:
    """
    Checks if the password meets the minimum length requirement.
    Uses a pre-compiled regex for efficiency.
    """
    return bool(_EIGHT_CHARS_REGEX.search(password))

def _has_uppercase(password: str) -> bool:
    """
    Checks if the password contains at least one uppercase letter.
    Uses a pre-compiled regex for efficiency.
    """
    return bool(_UPPERCASE_REGEX.search(password))

def _has_lowercase(password: str) -> bool:
    """
    Checks if the password contains at least one lowercase letter.
    Uses a pre-compiled regex for efficiency.
    """
    return bool(_LOWERCASE_REGEX.search(password))

def _has_digit(password: str) -> bool:
    """
    Checks if the password contains at least one digit.
    Uses a pre-compiled regex for efficiency.
    """
    return bool(_DIGIT_REGEX.search(password))


# --- Main Password Strength Test Function ---
def testPasswordStrength(password: str) -> bool:
    """
    Checks if a password is strong based on predefined criteria.

    Criteria:
    - At least MIN_PASSWORD_LENGTH characters long.
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one digit.

    Args:
        password (str): The password string to test.

    Returns:
        bool: True if the password meets all criteria, False otherwise.
    """
    if not _has_min_length(password):
        return False
    if not _has_uppercase(password):
        return False
    if not _has_lowercase(password):
        return False
    if not _has_digit(password):
        return False
    
    # If all checks pass, the password is considered strong
    return True


# --- Example Usage (Main execution block) ---
if __name__ == "__main__":
    # Test cases
    print("--- Testing Passwords ---")

    test_password_1 = "Addsas9%"  # Should be True
    print(f"'{test_password_1}' is strong: {testPasswordStrength(test_password_1)}")

    test_password_2 = "short"  # Too short, missing uppercase, missing digit
    print(f"'{test_password_2}' is strong: {testPasswordStrength(test_password_2)}")

    test_password_3 = "NO_DIGIT_HERE" # Missing digit
    print(f"'{test_password_3}' is strong: {testPasswordStrength(test_password_3)}")

    test_password_4 = "nouppercase123" # Missing uppercase
    print(f"'{test_password_4}' is strong: {testPasswordStrength(test_password_4)}")

    test_password_5 = "NOLOWERCASE123" # Missing lowercase
    print(f"'{test_password_5}' is strong: {testPasswordStrength(test_password_5)}")

    test_password_6 = "ValidP@ssw0rd!" # Should be True (if using extended regex later)
    print(f"'{test_password_6}' is strong: {testPasswordStrength(test_password_6)}")