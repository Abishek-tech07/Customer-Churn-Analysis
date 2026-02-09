# 📊 Customer Churn Analysis Dashboard (Power BI + Python)

## 📌 Project Overview
Customer churn is a critical business problem for subscription-based companies.  
This project combines **Python (for exploratory data analysis)** and **Power BI (for interactive dashboards)** to analyze customer churn and identify **high-risk segments, churn patterns, and key drivers**.

The project demonstrates an **end-to-end analytics workflow**:
- Data understanding and preprocessing using Python and excel 
- Business-ready dashboard development in Power BI
- Insight-driven storytelling for decision-making

---

## 🎯 Objectives
- Analyze customer churn behavior using Python
- Prepare clean, analysis-ready data
- Build interactive Power BI dashboards
- Identify **who is churning, when they churn, and potential churn drivers**

---

## 🗂 Dataset
- **Source:** Telco Customer Churn Dataset  
- **Records:** ~7,000 customers  
- **Target Variable:** `Churn (Yes / No)`

### Key Columns
- customerID  
- tenure  
- Contract  
- InternetService  
- MonthlyCharges  
- TechSupport  
- Churn,etc

---

## 🛠 Tools & Technologies
- **Python** (EDA & preprocessing)
  - pandas
  - numpy
  - matplotlib / seaborn
- **Power BI Desktop**
- **Power Query**
- **DAX**
- **Excel**

---

## 🐍 Python Analysis (EDA & Preparation)
Python was used to:
- Inspect dataset structure and data types
- Handle missing and inconsistent values
- Analyze churn distribution
- Explore churn relationships with:
  - Contract type
  - Monthly charges
  - Tenure
  - Internet service
- Validate assumptions before dashboard creation

📷 Screenshot: `images/python_eda.png`

---

## 🔄 Data Preparation (Power Query)
Performed in **Power BI Power Query**:
- Converted churn values into numeric flag (`Churn_Flag`)
- Created **Tenure Groups** using business logic
- Cleaned data types and categorical values
- Optimized data model for efficient DAX calculations

---

## 📐 Key Measures (DAX)
```DAX
Total Customers =
DISTINCTCOUNT('churn dataset'[customerID])

Churned Customers =
CALCULATE(
    DISTINCTCOUNT('churn dataset'[customerID]),
    'churn dataset'[Churn_Flag] = 1
)

Churn Rate =
AVERAGE('churn dataset'[Churn_Flag])
