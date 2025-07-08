#  AI-Powered Lead Scoring Tool

An interactive Streamlit-based web app for intelligently scoring, segmenting, and visualizing leads using AI-driven insights. Designed to help marketers, sales teams, and growth hackers prioritize outreach with ML-ready features and visual dashboards.

---

##  Overview

This app lets users:
-  Upload a CSV of leads
-  Auto-generate lead scores using custom or ML-based logic
-  View live segmentation (e.g., by role, score, LinkedIn presence)
-  Filter by role, score range, LinkedIn presence
-  Export filtered leads for CRM or campaign use
-  Explore visual dashboards for insights

---

## AI/ML Features

- 🔢 **Lead Scoring Logic**:
  - Currently: simple rule-based scoring (`90 - i*5`)
  - Planned: integration with `sklearn` models like `RandomForestClassifier`, `LogisticRegression`

-  Features considered:
  - Role category extraction (e.g., Executive, HR, Technical)
  - LinkedIn presence
  - Email format validity
  - Domain info
  - Industry
  - Business type (e.g., B2B, B2B2C)

---

##  UI Features (via Streamlit + Plotly)

- 📥 CSV Uploader
- 📊 KPI Cards (Executive %, LinkedIn %, Valid Emails)
- 📌 Filters:
  - Score range
  - Role category
  - LinkedIn only
- 📈 Visualizations:
  - Role distribution (pie chart)
  - Score ranges (bar chart)
- 🧾 Downloadable filtered leads
- 🧑‍💼 Email, LinkedIn & CRM link support (planned)

---

##  Sample Input Format

Your CSV should contain:

```csv
Name,Title,Email,Company,Domain,LinkedIn,Industry,Business Type
John Doe,CEO,john@example.com,TechNova,technova.com,https://linkedin.com/in/johndoe,Technology,B2B
...
