# Smart-Lead-Refiner
AI-powered lead scoring and filtering tool built with Streamlit. Upload your lead data, visualize insights, and prioritize outreach using smart filters and metrics.
# 🚀 AI-Powered Lead Scoring Tool

A Streamlit-based web app that helps businesses score and segment their leads using intelligent AI logic. Simply upload a CSV and get instant insights with visualizations, filters, and downloadable results.

---

## 📌 Features

- ✅ Upload CSV files with lead data
- 📊 Automatic **Lead Scoring**
- 🧠 AI-based **Role Categorization** (Executive, Manager, Technical, etc.)
- 📧 Email validation and 🔗 LinkedIn presence detection
- 🎯 Smart filters: Score threshold, Role category, LinkedIn filter
- 📥 Download filtered leads as CSV
- 📈 Lead Insights Dashboard:
  - Executive %, LinkedIn %, Valid Emails
  - Role Distribution (Pie Chart)
  - Score Range Distribution (Bar Chart)
- 🌐 Responsive UI with clean visual design using Streamlit + Plotly

---

## 📂 Input Format (CSV)

Make sure your CSV includes these columns:

Example:
```csv
John Doe,CEO,john@example.com,TechNova,technova.com,https://linkedin.com/in/johndoe
Jane Smith,Engineer,jane@example.com,CloudBright,cloudbright.ai,https://linkedin.com/in/janesmith

🛠️ Tech Stack
Frontend: Streamlit

Visualizations: Plotly Express

Machine Learning Ready: Future support for ML models using scikit-learn (Random Forest, Logistic Regression)
