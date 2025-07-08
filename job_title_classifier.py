# job_title_classifier.py
# Module for job title classification and role mapping 

def classify_title(title):
    """
    Takes a job title string and returns a standardized role category.
    """
    if not title or not isinstance(title, str):
        return "Other"

    title = title.lower()

    if any(keyword in title for keyword in ["ceo", "chief", "founder", "president", "vp", "vice president", "co-founder", "executive director"]):
        return "Executive"
    elif any(keyword in title for keyword in ["cto", "engineer", "developer", "scientist", "technologist", "data", "product manager"]):
        return "Technical"
    elif any(keyword in title for keyword in ["hr", "people operations", "recruiter", "talent"]):
        return "HR"
    elif "intern" in title:
        return "Intern"
    elif any(keyword in title for keyword in ["sales", "marketing", "business development", "growth", "account manager"]):
        return "Sales"
    else:
        return "Other" 

if __name__ == "__main__":
    print(classify_title("CEO"))                        # Executive
    print(classify_title("Software Engineer"))          # Technical
    print(classify_title("Growth Manager"))             # Sales
    print(classify_title("HR Business Partner"))        # HR
    print(classify_title("Intern - Marketing"))         # Intern
    print(classify_title("Product Designer"))           # Other
