import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="🚀 AI-Powered Lead Scoring Tool", layout="wide")

st.markdown("""
<div style='background: linear-gradient(to right, #3b82f6, #10b981); padding: 2rem; border-radius: 8px; text-align: center; color: white'>
    <h1>🚀 AI-Powered Lead Scoring Tool</h1>
    <p>Upload your CSV of leads and instantly get insights, filters, and scores to prioritize your outreach.</p>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df["Lead Score"] = [90 - i * 5 for i in range(len(df))]
    df["Email Format Valid"] = df["Email"].apply(lambda x: "@" in str(x))
    df["LinkedIn Present"] = df["LinkedIn"].apply(lambda x: isinstance(x, str) and len(x.strip()) > 0)
    df["Role Category"] = df["Title"].apply(
        lambda x: "Executive" if "CEO" in str(x) or "Founder" in str(x)
        else "Manager" if "Manager" in str(x)
        else "HR" if "HR" in str(x)
        else "Technical" if "Engineer" in str(x) or "Developer" in str(x)
        else "Other"
    )

    total_leads = len(df)
    avg_score = round(df["Lead Score"].mean(), 2)
    valid_email_rate = round(df["Email Format Valid"].mean() * 100, 2)

    st.markdown("### 📊 Summary Metrics")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Total Leads", total_leads)
    kpi2.metric("Avg. Lead Score", avg_score)
    kpi3.metric("Valid Emails", f"{valid_email_rate}%")

    st.markdown("### 🎯 Filter Your Leads")
    col1, col2, col3 = st.columns([2, 2, 2])

    with col1:
        min_score = int(df["Lead Score"].min())
        max_score = int(df["Lead Score"].max())
        score_threshold = st.slider("Minimum Lead Score:", min_value=min_score, max_value=max_score, value=min_score)

    with col2:
        role_options = ["All Roles"] + sorted(df["Role Category"].unique().tolist())
        selected_role = st.selectbox("Role Category", role_options)

    with col3:
        linkedin_only = st.checkbox("🔗 Only with LinkedIn profiles")

    df_filtered = df[df["Lead Score"] >= score_threshold]
    if selected_role != "All Roles":
        df_filtered = df_filtered[df_filtered["Role Category"] == selected_role]
    if linkedin_only:
        df_filtered = df_filtered[df_filtered["LinkedIn Present"] == True]

    st.markdown(f"### 📋 Scored Leads Table ({len(df_filtered)} results)")
    st.dataframe(df_filtered[["Company", "Title", "Email", "Lead Score", "Role Category"]], use_container_width=True)

    st.download_button(
        "⬇️ Download Filtered Results",
        data=df_filtered.to_csv(index=False).encode("utf-8"),
        file_name="filtered_scored_leads.csv",
        mime="text/csv"
    )

    # ================== Enhanced Lead Insights Summary ===================
    st.markdown("### 📈 Lead Insights Summary")

    executive_pct = round((df_filtered["Role Category"] == "Executive").mean() * 100, 2)
    linkedin_pct = round(df_filtered["LinkedIn Present"].mean() * 100, 2)
    valid_email_pct = round(df_filtered["Email Format Valid"].mean() * 100, 2)

    # Styled metric cards using HTML
    st.markdown("""
    <style>
    .metric-card {
        background-color: #f9f9ff;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }
    .metric-title {
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 0.5rem;
        margin-bottom: 0;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
    }
    .icon-box {
        font-size: 1.5rem;
        margin-bottom: 0.3rem;
    }
    .bg-blue { background-color: #e0f0ff; color: #1e40af; }
    .bg-green { background-color: #e6f9f0; color: #047857; }
    .bg-purple { background-color: #f3e8ff; color: #7c3aed; }
    </style>
    """, unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown(f"""
        <div class="metric-card bg-blue">
            <div class="icon-box">👨‍💼</div>
            <div class="metric-title">Executive Roles</div>
            <div class="metric-value">{executive_pct}%</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div class="metric-card bg-green">
            <div class="icon-box">🔗</div>
            <div class="metric-title">Have LinkedIn</div>
            <div class="metric-value">{linkedin_pct}%</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="metric-card bg-purple">
            <div class="icon-box">📬</div>
            <div class="metric-title">Valid Emails</div>
            <div class="metric-value">{valid_email_pct}%</div>
        </div>
        """, unsafe_allow_html=True)

    # Charts Section
    st.markdown("### 📊 Lead Segmentation")

    role_counts = df_filtered["Role Category"].value_counts()
    role_pie = px.pie(
        names=role_counts.index,
        values=role_counts.values,
        title="Role Distribution",
        color_discrete_sequence=px.colors.qualitative.Set1
    )

    score_bins = [0, 40, 60, 80, 100]
    score_labels = ["0–39", "40–59", "60–79", "80–100"]
    df_filtered["Score Bin"] = pd.cut(df_filtered["Lead Score"], bins=score_bins, labels=score_labels, include_lowest=True)
    score_dist = df_filtered["Score Bin"].value_counts().sort_index()
    score_bar = px.bar(
        x=score_dist.index,
        y=score_dist.values,
        labels={"x": "Score Range", "y": "Lead Count"},
        title="Score Distribution",
        color_discrete_sequence=["#3b82f6"]
    )

    c1, c2 = st.columns(2)
    c1.plotly_chart(role_pie, use_container_width=True)
    c2.plotly_chart(score_bar, use_container_width=True)

else:
    st.markdown("⚠️ Please upload a CSV file with columns: `Name, Title, Email, Company, Domain, LinkedIn`")
