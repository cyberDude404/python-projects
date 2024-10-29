import re

def validate_email(email):
    # Define a regex pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check email length
    if len(email) > 50:
        return False, "Invalid: Email length exceeds 50 characters."
    
    # Check for '@' symbol
    if '@' not in email:
        return False, "Invalid: Missing '@' symbol in email."
    
    # Check for '.' in domain part
    if '.' not in email.split('@')[-1]:
        return False, "Invalid: Missing '.' in domain part of email."
    
    # Check if email matches the regex pattern
    if not re.match(pattern, email):
        return False, "Invalid: Email does not match the required pattern."
    
    # If all checks pass
    return True, "Valid email address!"

# Test the function
email = input("Enter an email address: ")
is_valid, message = validate_email(email)
print(message)


