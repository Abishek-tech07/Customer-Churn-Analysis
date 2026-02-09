# ===============================
# CUSTOMER CHURN ANALYSIS PROJECT
# FULL SINGLE SCRIPT (VS CODE)
# ===============================

# ---------- 1. IMPORT LIBRARIES ----------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

print("\n--- Libraries Imported Successfully ---")


# ---------- 2. LOAD DATA ----------
df = pd.read_csv("churn_dataset.csv")

print("\n--- Data Loaded ---")
print(df.head())
print(df.shape)


# ---------- 3. TARGET COLUMN CHECK ----------
print("\n--- Churn Value Counts ---")
print(df["Churn"].value_counts())

# Convert Yes/No to 1/0 if needed
if df["Churn"].dtype == "object":
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

print("\n--- Churn Converted to Binary ---")
print(df["Churn"].value_counts())


# ---------- 4. EDA (VISUAL ANALYSIS) ----------

# 4.1 Churn Distribution
sns.countplot(x="Churn", data=df)
plt.title("Churn Distribution")
plt.show()

# 4.2 Churn vs Tenure
sns.boxplot(x="Churn", y="tenure", data=df)
plt.title("Churn vs Tenure")
plt.show()

# 4.3 Churn vs Contract
sns.countplot(x="Contract", hue="Churn", data=df)
plt.title("Churn by Contract Type")
plt.xticks(rotation=45)
plt.show()

# 4.4 Churn vs Monthly Charges
sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
plt.title("Churn vs Monthly Charges")
plt.show()

# 4.5 Churn vs Tech Support
sns.countplot(x="TechSupport", hue="Churn", data=df)
plt.title("Churn by Tech Support")
plt.xticks(rotation=45)
plt.show()


# ---------- 5. FEATURE ENGINEERING ----------

# Remove customerID if exists
df_model = df.drop(columns=["customerID"], errors="ignore")

# Convert categorical columns to numbers
df_model = pd.get_dummies(df_model, drop_first=True)

print("\n--- Data After Encoding ---")
print(df_model.head())


# ---------- 6. FEATURE SCALING ----------
scaler = StandardScaler()

numeric_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
numeric_cols = [col for col in numeric_cols if col in df_model.columns]

df_model[numeric_cols] = scaler.fit_transform(df_model[numeric_cols])

print("\n--- Numeric Features Scaled ---")


# ---------- 7. TRAIN TEST SPLIT ----------
X = df_model.drop("Churn", axis=1)
y = df_model["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\n--- Data Split Completed ---")
print("Train:", X_train.shape)
print("Test :", X_test.shape)


# ---------- 8. LOGISTIC REGRESSION ----------
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

y_pred_log = log_model.predict(X_test)

print("\n--- LOGISTIC REGRESSION RESULTS ---")
print("Accuracy :", accuracy_score(y_test, y_pred_log))
print("Precision:", precision_score(y_test, y_pred_log))
print("Recall   :", recall_score(y_test, y_pred_log))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log))


# ---------- 9. RANDOM FOREST ----------
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

print("\n--- RANDOM FOREST RESULTS ---")
print("Accuracy :", accuracy_score(y_test, y_pred_rf))
print("Precision:", precision_score(y_test, y_pred_rf))
print("Recall   :", recall_score(y_test, y_pred_rf))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rf))


# ---------- 10. FEATURE IMPORTANCE ----------
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\n--- TOP 10 CHURN DRIVERS ---")
print(feature_importance.head(10))

sns.barplot(
    x="Importance",
    y="Feature",
    data=feature_importance.head(10)
)
plt.title("Top 10 Churn Drivers")
plt.show()


# ---------- 11. BUSINESS INSIGHTS ----------
print("\n--- BUSINESS INSIGHTS ---")
print("1. Month-to-month contracts have highest churn")
print("2. Low tenure customers are high risk")
print("3. Customers without tech support churn more")

print("\n--- RECOMMENDATIONS ---")
print("• Promote long-term contracts")
print("• Improve onboarding in first 6 months")
print("• Bundle tech support services")


# ---------- 12. EXPORT FOR POWER BI ----------
df_model.to_csv("churn_final_for_powerbi.csv", index=False)

print("\n--- FILE EXPORTED: churn_final_for_powerbi.csv ---")
print("READY FOR POWER BI DASHBOARD")