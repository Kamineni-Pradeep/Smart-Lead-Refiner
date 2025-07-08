# main.py
# Entry point for Smart Lead Refiner 

import pandas as pd
from email_validation import validate_email
from job_title_classifier import classify_title
from lead_scoring import score_lead

def process_leads(input_path, output_path):
    # Read raw leads
    df = pd.read_csv(input_path)
    
    results = []

    for _, row in df.iterrows():
        # Step 1: Extract raw fields
        name = row.get('Name', '')
        title = row.get('Title', '')
        email = row.get('Email', '')
        company = row.get('Company', '')
        domain = row.get('Domain', '')
        linkedin = row.get('LinkedIn', '')
        
        # Step 2: Validate email
        format_valid, mx_valid = validate_email(email)
        
        # Step 3: Classify role
        role_category = classify_title(title)
        
        # Step 4: Check LinkedIn presence
        has_linkedin = isinstance(linkedin, str) and linkedin.strip().startswith("http")
        
        # Step 5: Score the lead
        lead_score = score_lead(format_valid, mx_valid, role_category, has_linkedin)

        # Step 6: Append result row
        results.append({
            "Name": name,
            "Title": title,
            "Email": email,
            "Company": company,
            "Domain": domain,
            "LinkedIn": linkedin,
            "Email Format Valid": format_valid,
            "Email Domain Valid": mx_valid,
            "Role Category": role_category,
            "Lead Score": lead_score
        })

    # Step 7: Save enriched leads to new file
    output_df = pd.DataFrame(results)
    output_df.to_csv(output_path, index=False)
    print(f"✅ Processed {len(df)} leads → saved to: {output_path}")

if __name__ == "__main__":
    process_leads("smart-lead-refiner\sample_leads.csv", "output.csv") 