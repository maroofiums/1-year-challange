# Day301 **Customer Churn Prediction – End-to-End ML Pipeline**

[Try the App Online 🚀](https://churn-prediction-by-maroofiums.streamlit.app/)

---

## **Project Overview**

This project focuses on building a **production-ready machine learning pipeline** to predict **customer churn**—i.e., which customers are likely to leave a service. The pipeline is designed to be **reusable, scalable, and ready for deployment** in a real-world scenario.

**Dataset:**

* **Telco Churn Dataset** – includes customer demographics, account info, and service usage details.
* Key features: `tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `PaymentMethod`, `OnlineSecurity`, `TechSupport`, etc.

---

## **Problem Statement**

Customer churn is costly for businesses. Identifying customers who might leave allows companies to **take proactive measures**, reduce losses, and improve customer retention. The goal of this project is to **build a predictive system** that processes raw customer data and outputs churn predictions reliably.

---

## **Approach & Implementation**

1. **Data Preprocessing Pipeline:**

   * Handle missing values and inconsistent data.
   * Encode categorical features using **manual mappings** for consistency and production readiness.
   * Maintain consistent **feature order** required by trained models.
   * Implemented a **Scikit-learn Pipeline** combining preprocessing and model training.

2. **Model Selection:**

   * Trained **Logistic Regression** for interpretability.
   * Trained **Random Forest** for higher accuracy and feature importance insights.
   * Evaluated using **cross-validation** and metrics like Accuracy, Precision, Recall, and ROC-AUC.

3. **Hyperparameter Tuning:**

   * Used **GridSearchCV** to find the best parameters.
   * Ensured optimal generalization on unseen data.

4. **Model Export & Reusability:**

   * Exported the final pipeline using **joblib**, including preprocessing and model.
   * Enables loading directly into a Streamlit app or other production environment.

5. **Deployment:**

   * Integrated the trained pipeline into a **Streamlit app** for interactive predictions.
   * Users can input customer information and get **churn predictions with probabilities**.

---

## **Challenges & Solutions**

1. **Feature Encoding:**

   * Multiple categorical features with “No internet service” caused encoding conflicts.
   * Solved with **manual mapping** to ensure consistent numeric representation.

2. **Feature Order Requirement:**

   * The model required features in the **exact order** as during training.
   * Streamlit inputs are reordered programmatically before prediction.

3. **Version Compatibility:**

   * Model trained on an older version of Scikit-learn; manual mapping ensured reproducibility.

---

## **Final Product**

* A **fully functional ML pipeline** capable of:

  1. Preprocessing raw input.
  2. Predicting customer churn and probability.
  3. Being reused in other applications.

* **Interactive Streamlit App:** [Try it here](https://churn-prediction-by-maroofiums.streamlit.app/)

**Skills Demonstrated:**

* Scikit-learn pipeline construction
* Feature encoding & preprocessing
* Hyperparameter tuning
* Model export & deployment
* Streamlit interactive UI

---

### **Key Takeaways**

* **Manual label mapping** can be safer than LabelEncoder for production apps.
* Always ensure **feature names and order** match between training and deployment.
* Combining **pipeline + model export + Streamlit UI** enables rapid prototyping and real-world usage.
