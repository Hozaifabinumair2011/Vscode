import re

def check_password_strength(password):
    strength = 0

    # Check length
    if len(password) >= 8:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for digits
    if re.search(r"\d", password):
        strength += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    return strength

def password_strength_message(strength):
    if strength == 5:
        return "Very Strong"
    elif strength >= 3:
        return "Strong"
    elif strength >= 2:
        return "Medium"
    else:
        return "Weak"

password = input("Enter a password: ")
strength = check_password_strength(password)
print(f"Password Strength: {password_strength_message(strength)}")

if strength < 5:
    print("Suggestions:")
    if len(password) < 8:
        print("- Password should be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        print("- Password should contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        print("- Password should contain at least one lowercase letter.")
    if not re.search(r"\d", password):
        print("- Password should contain at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("- Password should contain at least one special character.")