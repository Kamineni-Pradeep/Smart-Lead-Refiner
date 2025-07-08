# email_validation.py
# Module for email validation 

import re
import dns.resolver

def is_valid_format(email):
    """Check if email is in a valid format using regex."""
    if not isinstance(email, str):
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def has_mx_record(domain):
    """Check if domain has MX records for receiving emails."""
    try:
        dns.resolver.resolve(domain, 'MX')
        return True
    except Exception:
        return False

def validate_email(email):
    """
    Returns a tuple: (format_valid, mx_valid)
    - format_valid: True if matches regex
    - mx_valid: True if domain has MX record
    """
    if not email or not isinstance(email, str):
        return False, False

    format_valid = is_valid_format(email)
    if not format_valid:
        return False, False

    domain = email.split('@')[-1]
    mx_valid = has_mx_record(domain)
    return format_valid, mx_valid

if __name__ == "__main__":
    print(validate_email("john@google.com"))  # Expected: (True, True)
    print(validate_email("bademail.com"))     # Expected: (False, False)
    print(validate_email("fake@madeupdomain.lol"))  # Could be (True, False) 