* Python
* NumPy
* Pandas
* Data cleaning
* EDA
* Feature engineering
* Scikit-learn
* Train/test splitting
* Regression
* Classification
* Metrics
* Encoding/scaling
* Cross-validation
* Hyperparameter tuning
* Basic model interpretation

---

# 🟢 Level 1 — Python + NumPy fundamentals

### Task 1 — Find missing values

Given:

```python
data = [10, 20, None, 40, None, 60]
```

Write Python code to count the missing values.

---

### Task 2 — Remove duplicates

```python
values = [10, 20, 20, 30, 40, 40, 50]
```

Create a list containing only unique values.

---

### Task 3 — Find mean manually

```python
values = [10, 20, 30, 40, 50]
```

Calculate the mean **without NumPy**.

---

### Task 4 — NumPy statistics

Create a NumPy array:

```python
arr = np.array([10, 20, 30, 40, 50])
```

Find:

* mean
* median
* standard deviation
* minimum
* maximum

---

### Task 5 — Normalize an array

Given:

```python
arr = np.array([10, 20, 30, 40, 50])
```

Perform **min-max normalization**.

Expected formula:

```text
x' = (x - min) / (max - min)
```

---

### Task 6 — Standardization

Given the same array, standardize it using:

```text
z = (x - mean) / standard_deviation
```

---

### Task 7 — Boolean filtering

Given:

```python
arr = np.array([10, 25, 30, 15, 40, 50])
```

Return values greater than `25`.

---

# 🟡 Level 2 — Pandas

### Task 8 — Create a DataFrame

Create this DataFrame:

```text
name     age    salary
A        22     30000
B        25     45000
C        21     28000
D        30     60000
```

Then display it.

---

### Task 9 — Select rows

From the DataFrame above, find employees whose:

```text
salary > 40000
```

---

### Task 10 — Select multiple conditions

Find employees who:

```text
age > 22
AND
salary > 30000
```

---

### Task 11 — Missing values

Given:

```python
df = pd.DataFrame({
    "age": [22, 25, None, 30, None],
    "salary": [30000, None, 40000, 60000, 50000]
})
```

Do all three:

1. Count missing values
2. Fill missing age with mean age
3. Fill missing salary with median salary

---

### Task 12 — Drop missing rows

Remove rows containing missing values.

```python
df.dropna()
```

Then compare the number of rows before and after.

---

### Task 13 — Remove duplicates

Given:

```python
df = pd.DataFrame({
    "name": ["A", "B", "B", "C"],
    "age": [20, 25, 25, 30]
})
```

Remove duplicate rows.

---

### Task 14 — GroupBy

Given:

```text
city       sales
Chennai    100
Chennai    200
Mumbai     300
Mumbai     100
Delhi      500
```

Find total sales by city.

You should know:

```python
df.groupby("city")["sales"].sum()
```

---

### Task 15 — Sorting

Sort employees by salary from highest to lowest.

---

### Task 16 — Create a new feature

Given:

```text
height
weight
```

Create:

```text
BMI = weight / height²
```

Assume height is in meters.

---

### Task 17 — Apply a function

Given:

```python
df["salary"]
```

Create a new column:

```text
salary_category
```

Rules:

```text
salary < 30000       → Low
30000–50000          → Medium
> 50000              → High
```

---

# 🟠 Level 3 — EDA

These are **very important**.

### Task 18 — Basic EDA

Given a dataset `df`, write code to find:

```python
df.shape
df.head()
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
```

Know what every one does.

---

### Task 19 — Numerical columns

Find all numerical columns in a DataFrame.

---

### Task 20 — Categorical columns

Find all categorical/object columns.

---

### Task 21 — Correlation

Given a dataset containing:

```text
age
salary
experience
purchased
```

Calculate the correlation matrix.

Then identify which features are most correlated with `purchased`.

---

### Task 22 — Outlier detection

Given:

```python
df["salary"]
```

Use the **IQR method** to identify outliers.

Remember:

```text
Q1
Q3
IQR = Q3 - Q1

lower = Q1 - 1.5 × IQR
upper = Q3 + 1.5 × IQR
```

---

### Task 23 — Remove outliers

Using the IQR boundaries, create a DataFrame containing only non-outlier rows.

---

# 🔵 Level 4 — Feature Engineering / Preprocessing

### Task 24 — Label Encoding

Given:

```text
color
------
Red
Blue
Green
Red
Blue
```

Convert it into numerical values using `LabelEncoder`.

---

### Task 25 — One-hot encoding

Given:

```text
city
------
Chennai
Mumbai
Delhi
Chennai
```

Convert it using:

```python
pd.get_dummies()
```

---

### Task 26 — Train/test split

Given:

```python
X
y
```

Split into:

```text
80% training
20% testing
```

Use `random_state=42`.

---

### Task 27 — Feature scaling

Given numerical features:

```text
age
salary
experience
```

Apply `StandardScaler`.

Know the difference between:

```python
fit()
transform()
fit_transform()
```

This is **very commonly tested**.

---

### Task 28 — Build a preprocessing pipeline

Dataset:

```text
age        → numerical
salary     → numerical
city       → categorical
```

Create a `ColumnTransformer` that:

* scales numerical columns
* one-hot encodes categorical columns

---

# 🔴 Level 5 — Machine Learning

Now the actual ML coding.

### Task 29 — Linear Regression

Given:

```text
hours_studied → marks
```

Train a `LinearRegression` model.

Perform:

```text
train_test_split
fit
predict
```

Calculate:

```text
MAE
MSE
RMSE
R²
```

---

### Task 30 — Multiple Linear Regression

Dataset:

```text
experience
age
education
```

Predict:

```text
salary
```

Train a multiple linear regression model.

---

### Task 31 — Logistic Regression

Given:

```text
age
salary
```

Predict:

```text
purchased
```

where:

```text
0 = No
1 = Yes
```

Train a Logistic Regression model.

---

### Task 32 — Classification metrics

Given:

```python
y_test
y_pred
```

Calculate:

```text
Accuracy
Precision
Recall
F1-score
Confusion matrix
```

You should be able to write these **without searching**.

---

### Task 33 — Decision Tree

Train a `DecisionTreeClassifier` on a classification dataset.

Do:

```text
split
train
predict
evaluate
```

Then experiment with:

```python
max_depth
```

and observe how the result changes.

---

### Task 34 — Random Forest

Train:

```python
RandomForestClassifier()
```

Compare its performance with your Decision Tree.

---

### Task 35 — KNN

Train a `KNeighborsClassifier`.

Try:

```text
k = 3
k = 5
k = 7
```

Compare accuracy.

---

# 🔥 Bonus test-level tasks

If you finish the 35, do these too.

### Task 36 — Handle imbalanced data

Given:

```text
Class 0 → 950 samples
Class 1 → 50 samples
```

Explain through code why accuracy may be misleading.

Calculate:

```text
precision
recall
F1
```

---

### Task 37 — Cross-validation

Train a Logistic Regression model using:

```python
cross_val_score()
```

with:

```text
cv=5
```

Find the mean CV score.

---

### Task 38 — Hyperparameter tuning

Use `GridSearchCV` to find the best:

```text
max_depth
```

for a Decision Tree.

---

### Task 39 — Feature importance

Train a Random Forest and display the importance of each feature.

---

### Task 40 — Complete ML mini-test

Given a CSV dataset:

```text
customer_age
income
tenure
city
monthly_spend
churn
```

Your task:

1. Load the dataset
2. Inspect it
3. Find missing values
4. Remove duplicates
5. Handle missing values
6. Encode `city`
7. Separate `X` and `y`
8. Train/test split
9. Scale numerical features
10. Train Logistic Regression
11. Predict
12. Calculate accuracy
13. Calculate precision
14. Calculate recall
15. Calculate F1
16. Display confusion matrix

**This one is closest to the kind of end-to-end coding exercise I would prioritize for tomorrow.**

---

# 🎯 What I want you to focus on tonight

Don't try to memorize 40 algorithms.

Your priority should be:

```text
                 ML CODING TEST
                       │
       ┌───────────────┼────────────────┐
       ↓               ↓                ↓
     Python          Pandas         NumPy
       │               │                │
       └───────────────┼────────────────┘
                       ↓
                      EDA
                       ↓
              Data Preprocessing
                       ↓
          ┌────────────┴────────────┐
          ↓                         ↓
      Regression              Classification
          ↓                         ↓
    LinearRegression       LogisticRegression
                                  │
                    ┌─────────────┼─────────────┐
                    ↓             ↓             ↓
              Decision Tree   Random Forest     KNN
                    │
                    ↓
                  Metrics
                    │
          Accuracy / Precision
          Recall / F1 / RMSE / R²
```