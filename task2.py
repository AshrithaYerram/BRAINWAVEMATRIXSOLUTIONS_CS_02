import re

def check_password_strength(password):
    strength_score = 0
    feedback = []
    
    # Length check
    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    elif len(password) >= 12:
        strength_score += 2
    else:
        strength_score += 1
    
    # Complexity checks
    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    
    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    
    if re.search(r"[0-9]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one number.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.).")
    
    # Common password check
    common_passwords = {"password", "123456", "12345678", "qwerty", "abc123", "password1"}
    if password.lower() in common_passwords:
        feedback.append("Your password is too common. Choose something more unique.")
        strength_score = max(strength_score - 2, 0)
    
    # Strength evaluation
    if strength_score <= 2:
        strength = "Weak"
    elif strength_score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return strength, feedback

# Example usage
password = input("Enter a password: ")
strength, feedback = check_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions:")
    for suggestion in feedback:
        print(f"- {suggestion}")
