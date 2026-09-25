# HR Analytics Dashboard

## 📌 Project Overview

This project is an **HR Analytics Dashboard** developed to analyze employee information and understand employee attrition.

The project uses **Python, Pandas, NumPy, Matplotlib, Seaborn, and Streamlit** to perform data analysis and create an interactive dashboard.

The dashboard allows users to explore employee data using filters and different visualizations.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze employee data
- Understand employee demographics
- Analyze employee attrition
- Analyze employees by department
- Understand age distribution
- Analyze overtime and its relationship with attrition
- Analyze monthly income
- Provide an interactive HR dashboard
- Allow users to filter and download the analyzed data

---

## 🛠️ Technologies Used

### Python

Python is used as the main programming language for data analysis and dashboard development.

### Pandas

Pandas is used for:

- Reading the CSV dataset
- Data manipulation
- Data filtering
- Data analysis
- Creating summary information

### NumPy

NumPy is used for numerical operations and data processing.

### Matplotlib

Matplotlib is used to create charts such as:

- Pie charts
- Employee distribution charts
- Other visualizations

### Seaborn

Seaborn is used to create statistical visualizations such as:

- Bar charts
- Histograms
- Box plots
- Count plots

### Streamlit

Streamlit is used to convert the Python analysis into an interactive web dashboard.

---

## 📊 Dashboard Features

The dashboard contains the following features:

### 1. KPI Cards

The dashboard displays:

- Total Employees
- Average Age
- Average Monthly Income
- Attrition Rate

### 2. Filters

Users can filter the dashboard using:

- Department
- Gender
- Attrition

The charts and KPI values update according to the selected filters.

### 3. Gender Distribution

A pie chart is used to display the distribution of employees by gender.

### 4. Attrition Distribution

A pie chart shows the number of employees who stayed and employees who left.

### 5. Employees by Department

A bar chart displays the number of employees in each department.

### 6. Age Distribution

A histogram is used to understand the age distribution of employees.

### 7. Age vs Attrition

A box plot is used to compare employee age across attrition categories.

### 8. Overtime vs Attrition

A count plot is used to analyze the relationship between overtime and employee attrition.

### 9. Monthly Income Distribution

A histogram is used to visualize the distribution of employee monthly income.

### 10. Employee Data Table

The dashboard provides an interactive table containing the filtered employee records.

### 11. Download Data

Users can download the filtered employee data as a CSV file.

---

## 📁 Project Structure

```text
hr-analyst/
│
├── app.py
├── hr.ipynb
├── HR_Analytics-4.csv
├── requirements.txt
└── README.md
```

### Files Description

**app.py**

Contains the Streamlit dashboard application.

**hr.ipynb**

Contains the Python/Jupyter Notebook analysis and data exploration.

**HR_Analytics-4.csv**

Contains the employee HR dataset used for the project.

**requirements.txt**

Contains the Python libraries required to run the project.

**README.md**

Contains project documentation and instructions.

---

## 📦 Requirements

The project uses the following Python libraries:

```text
streamlit
pandas
numpy
matplotlib
seaborn
```

Install the required libraries using:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/Dileep0505/hr-analyst.git
```

### Step 2: Open the project folder

```bash
cd hr-analyst
```

### Step 3: Install the required libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit application

```bash
streamlit run app.py
```

The dashboard will open in your web browser.

---

## 📈 Data Analysis

The project analyzes different employee attributes including:

- Age
- Gender
- Department
- Attrition
- Monthly Income
- Overtime
- Employee information

These attributes are used to create meaningful HR visualizations and identify patterns in the employee dataset.

---

## 🌐 Deployment

The Streamlit application can be deployed online using **Streamlit Community Cloud**.

The GitHub repository contains the application code and dependency file required for deployment.

---

## 🔗 Project Repository

GitHub Repository:

https://github.com/Dileep0505/hr-analyst

---

## 👨‍💻 Author

**Dileep**

HR Analytics Project using Python and Streamlit.
