import re

def assess_password_strength(password):
    # Initialize strength score
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*).")
    
    # Evaluate the overall strength based on the score
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Medium"
    else:
        strength = "Weak"
    
    # Provide feedback on strength
    feedback.insert(0, f"Password Strength: {strength}")
    return feedback

# Example Usage
password = input("Enter your password: ")
feedback = assess_password_strength(password)

for line in feedback:
    print(line)
