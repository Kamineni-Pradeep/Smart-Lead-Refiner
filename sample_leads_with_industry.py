import pandas as pd
import random

# Load your CSV
df = pd.read_csv(".\smart-lead-refiner\sample_leads.csv")

# Define lists
industries = ["SaaS", "Healthcare", "FinTech", "E-commerce", "Marketing", "Cybersecurity"]
business_types = ["B2B", "B2C", "B2B2C"]

# Assign random values
df["Industry"] = [random.choice(industries) for _ in range(len(df))]
df["BusinessType"] = [random.choice(business_types) for _ in range(len(df))]

# Save new CSV
df.to_csv("sample_leads_with_industry.csv", index=False) 