from pathlib import Path

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

DATASET_FILE = "HR_Analytics-4.csv"


def resolve_data_path():
    """Find the HR dataset in the project folder, current working directory, or common download locations."""
    candidates = []
    base_dir = Path(__file__).resolve().parent

    for location in [base_dir, Path.cwd()]:
        candidates.append(location / DATASET_FILE)

    home_dir = Path.home()
    for location in [home_dir / "Downloads", home_dir / "Desktop", home_dir]:
        candidates.append(location / DATASET_FILE)

    for location in [base_dir, home_dir]:
        if location.exists():
            for match in location.rglob(DATASET_FILE):
                candidates.append(match)

    seen = set()
    for candidate in candidates:
        resolved = candidate.resolve(strict=False)
        if resolved in seen:
            continue
        seen.add(resolved)
        if resolved.exists() and resolved.is_file():
            return resolved
    return None


def load_data():
    data_path = resolve_data_path()
    if data_path is not None:
        return pd.read_csv(data_path)

    st.warning(
        "The HR dataset was not found in the workspace. A demo dataset is being used so the dashboard still works."
    )

    demo_rows = [
        {"Department": "Sales", "Gender": "Female", "Attrition": "Yes", "Age": 30, "MonthlyIncome": 50000, "OverTime": "Yes"},
        {"Department": "Sales", "Gender": "Male", "Attrition": "No", "Age": 35, "MonthlyIncome": 62000, "OverTime": "No"},
        {"Department": "Research & Development", "Gender": "Male", "Attrition": "No", "Age": 42, "MonthlyIncome": 70000, "OverTime": "No"},
        {"Department": "Human Resources", "Gender": "Female", "Attrition": "Yes", "Age": 28, "MonthlyIncome": 48000, "OverTime": "Yes"},
        {"Department": "Finance", "Gender": "Male", "Attrition": "No", "Age": 41, "MonthlyIncome": 66000, "OverTime": "No"},
        {"Department": "Marketing", "Gender": "Female", "Attrition": "No", "Age": 33, "MonthlyIncome": 56000, "OverTime": "Yes"},
        {"Department": "Technical", "Gender": "Male", "Attrition": "Yes", "Age": 39, "MonthlyIncome": 75000, "OverTime": "Yes"},
        {"Department": "Technical", "Gender": "Female", "Attrition": "No", "Age": 45, "MonthlyIncome": 80000, "OverTime": "No"},
    ]
    return pd.DataFrame(demo_rows)


st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="👥",
    layout="wide"
)

df = load_data()

st.title("👥 HR Analytics Dashboard")
st.write("Employee Data Analysis and Attrition Dashboard")

st.sidebar.header("🔎 Filters")

department = st.sidebar.multiselect(
    "Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

attrition = st.sidebar.multiselect(
    "Attrition",
    options=df["Attrition"].unique(),
    default=df["Attrition"].unique()
)

filtered_df = df[
    (df["Department"].isin(department)) &
    (df["Gender"].isin(gender)) &
    (df["Attrition"].isin(attrition))
]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Employees",
    len(filtered_df)
)

col2.metric(
    "Average Age",
    round(filtered_df["Age"].mean(), 1)
)

col3.metric(
    "Average Monthly Income",
    round(filtered_df["MonthlyIncome"].mean(), 0)
)

attrition_rate = filtered_df["Attrition"].eq("Yes").mean() * 100

col4.metric(
    "Attrition Rate",
    f"{attrition_rate:.1f}%"
)

st.divider()

st.subheader("📊 Employee Overview")

col1, col2 = st.columns(2)

with col1:
    st.write("### Gender Distribution")

    gender_count = filtered_df["Gender"].value_counts()

    fig, ax = plt.subplots()

    ax.pie(
        gender_count,
        labels=gender_count.index,
        autopct="%1.1f%%"
    )

    ax.set_title("Gender Distribution")

    st.pyplot(fig)

with col2:
    st.write("### Attrition Distribution")

    attrition_count = filtered_df["Attrition"].value_counts()

    fig, ax = plt.subplots()

    ax.pie(
        attrition_count,
        labels=attrition_count.index,
        autopct="%1.1f%%"
    )

    ax.set_title("Employee Attrition")

    st.pyplot(fig)

st.divider()

st.subheader("🏢 Employees by Department")

department_count = filtered_df["Department"].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    x=department_count.index,
    y=department_count.values,
    ax=ax
)

ax.set_xlabel("Department")
ax.set_ylabel("Employees")

plt.xticks(rotation=20)

st.pyplot(fig)

st.subheader("🎂 Age Distribution")

fig, ax = plt.subplots(figsize=(10, 5))

sns.histplot(
    filtered_df["Age"],
    bins=15,
    kde=True,
    ax=ax
)

ax.set_xlabel("Age")
ax.set_ylabel("Number of Employees")

st.pyplot(fig)

st.subheader("🎯 Age vs Attrition")

fig, ax = plt.subplots(figsize=(10, 5))

sns.boxplot(
    data=filtered_df,
    x="Attrition",
    y="Age",
    ax=ax
)

st.pyplot(fig)

st.subheader("⏰ Overtime vs Attrition")

fig, ax = plt.subplots(figsize=(10, 5))

sns.countplot(
    data=filtered_df,
    x="OverTime",
    hue="Attrition",
    ax=ax
)

ax.set_xlabel("Overtime")
ax.set_ylabel("Employees")

st.pyplot(fig)

st.subheader("💰 Monthly Income Distribution")

fig, ax = plt.subplots(figsize=(10, 5))

sns.histplot(
    filtered_df["MonthlyIncome"],
    kde=True,
    ax=ax
)

ax.set_xlabel("Monthly Income")
ax.set_ylabel("Employees")

st.pyplot(fig)

st.subheader("📋 Employee Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇️ Download Filtered Data",
    data=csv,
    file_name="HR_Filtered_Data.csv",
    mime="text/csv"
)

st.divider()

st.caption(
    "HR Analytics Dashboard | Python, Pandas, NumPy, Matplotlib, Seaborn & Streamlit"
)