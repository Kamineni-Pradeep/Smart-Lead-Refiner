# lead_scoring.py
# Module for lead scoring logic 

def score_lead(email_valid, mx_valid, role_category, has_linkedin):
    """
    Returns an integer lead score out of 100 based on:
    - Email validity
    - Role importance
    - LinkedIn presence
    """

    score = 0

    # Email validity scoring
    if email_valid and mx_valid:
        score += 40
    elif email_valid:
        score += 20  # Valid format but domain has no mail server

    # Role importance scoring
    role_weights = {
        "Executive": 35,
        "Sales": 25,
        "Technical": 20,
        "HR": 15,
        "Intern": 5,
        "Other": 10
    }
    score += role_weights.get(role_category, 10)

    # LinkedIn presence adds bonus
    if has_linkedin:
        score += 10

    return min(score, 100)  # Cap at 100 

if __name__ == "__main__":
    print(score_lead(True, True, "Executive", True))     # Should return 85
    print(score_lead(True, False, "Sales", False))       # Should return 45
    print(score_lead(False, False, "Intern", True))      # Should return 15