# 📊 Data Description

This dataset contains information about individuals and their corresponding medical insurance charges. It is often used for regression tasks, especially to understand how personal attributes influence insurance cost.

## 📁 Features Overview

| Feature           | Type         | Description |
|------------------|--------------|-------------|
| `age`            | Numerical    | Age of the primary beneficiary (in years). |
| `gender`         | Categorical  | Gender of the individual (male/female). |
| `bmi`            | Numerical    | Body Mass Index — a measure of body fat based on height and weight. |
| `no_of_children` | Numerical    | Number of dependent children covered by the insurance. |
| `smoker`         | Categorical  | Whether the person smokes (1 for Yes, 0 for No after encoding). |
| `region`         | Categorical  | Residential region in the US (northeast, northwest, southeast, southwest). |
| `charges`        | Numerical    | Individual medical costs billed by health insurance. |

## 🔍 Notes
- **`charges`** is the **target variable**.
- Categorical features like `smoker`, `gender`, and `region` can be encoded for machine learning models.
- `bmi` and `smoker` are strongly correlated with insurance cost based on EDA.

---

The dataset is suitable for regression modeling and exploring the impact of lifestyle and demographic factors on healthcare expenses.





