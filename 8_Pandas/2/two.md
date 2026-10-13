# EDA – Exploratory Data Analysis

**Date:** 28/7/2026

---

# Keywords

## Main Topics

* Exploratory Data Analysis (EDA)
* Data Inspection
* Data Cleaning
* Statistical Analysis
* Data Visualization
* Relationship Analysis
* Correlation Analysis
* Machine Learning Data Preparation

## Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn

## Python Functions

* `head()`
* `tail()`
* `shape`
* `info()`
* `columns`
* `dtypes`
* `isnull()`
* `dropna()`
* `fillna()`
* `duplicated()`
* `drop_duplicates()`
* `rename()`
* `astype()`
* `describe()`
* `corr()`
* `heatmap()`
* `histplot()`
* `boxplot()`
* `scatterplot()`
* `countplot()`
* `groupby()`

## Data Concepts

* Dataset Inspection
* Missing Values
* Duplicate Values
* Data Types
* Statistical Summary
* Numerical Variables
* Categorical Values
* Outliers
* Data Distribution
* Feature Understanding
* Business Insights

---

# Tags & References

| Tag     | Meaning                   |
| ------- | ------------------------- |
| `[WHY]` | Why this is used          |
| `[USC]` | Use Cases                 |
| `[MET]` | Methods                   |
| `[ALI]` | Alias                     |
| `[USA]` | Usage / Example Code      |
| `[RES]` | Expected Result           |
| `[FUN]` | Functions Used            |
| `[CAT]` | Limitations / Cannot Have |

---

# Quick Summary

* EDA stands for Exploratory Data Analysis.
* It is performed before building Machine Learning models.
* EDA helps understand, clean, analyze, and visualize datasets.
* Main activities:

  * Data Inspection
  * Data Cleaning
  * Statistical Analysis
  * Data Visualization
  * Feature Understanding
  * Correlation Analysis
* Common libraries:

  * Pandas
  * NumPy
  * Matplotlib
  * Seaborn
* A good EDA process produces cleaner and more reliable data.

---

# Table of Contents

1. [Introduction to EDA](#introduction-to-eda)
2. [Import Libraries](#import-libraries)
3. [Load Dataset](#load-dataset)
4. [Data Inspection](#data-inspection)
5. [Data Cleaning](#data-cleaning)
6. [Statistical Summary](#statistical-summary)
7. [Relationship Analysis](#relationship-analysis)
8. [Data Visualization](#data-visualization)
9. [Common EDA Functions](#common-eda-functions)
10. [Data Cleaning Checklist](#data-cleaning-checklist)
11. [Advantages](#advantages)
12. [Limitations](#limitations)
13. [Quick Summary](#quick-summary)
14. [Key Points](#key-points)

---

# Introduction to EDA

## [WHY]

Exploratory Data Analysis (EDA) is the process of understanding, cleaning, and analyzing a dataset before building any Machine Learning model.

---

## [USC] Use Cases

EDA is used to:

* Understand the dataset
* Detect errors
* Clean data
* Discover hidden patterns
* Find relationships between variables
* Generate business insights
* Prepare data for Machine Learning

---

## [MET] Methods

Common EDA methods:

* Data Inspection
* Data Cleaning
* Statistical Analysis
* Data Visualization
* Feature Understanding
* Correlation Analysis

---

# Import Libraries

## [ALI] Alias

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# Load Dataset

## [USA] Usage

```python
df = pd.read_csv("data.csv")
```

## [RES] Expected Result

Loads the dataset into a Pandas DataFrame.

---

# Data Inspection

Data inspection is the process of examining the dataset structure, columns, data types, and available information before analysis.

---

## 1. View First Records

### [WHY]

Displays the first few rows.

### [USA]

```python
df.head()
```

---

## 2. View Last Records

### [WHY]

Displays the last few rows.

### [USA]

```python
df.tail()
```

---

## 3. Dataset Shape

### [WHY]

Returns number of rows and columns.

### [USA]

```python
df.shape
```

---

## 4. Dataset Information

### [WHY]

Shows:

* Column names
* Data types
* Non-null values
* Memory usage

### [USA]

```python
df.info()
```

---

## 5. Column Names

### [WHY]

Lists all column names.

### [USA]

```python
df.columns
```

---

## 6. Data Types

### [WHY]

Displays data type of every column.

### [USA]

```python
df.dtypes
```

---
# Data Cleaning

Data cleaning is the process of identifying and correcting inaccurate, incomplete, duplicate, or inconsistent data before analysis or Machine Learning model development.

---

# 1. Missing Values

## [WHY]

Finds missing (`NULL` / `NaN`) values in the dataset.

## [USA]

```python
df.isnull()
```

---

## Count Missing Values

```python
df.isnull().sum()
```

---

## Remove Missing Values

```python
df.dropna()
```

---

## Fill Missing Values

```python
df.fillna(0)
```

```python
df.fillna(df.mean(numeric_only=True))
```

---

# 2. Duplicate Values

## [WHY]

Finds duplicate records in the dataset.

## [USA]

```python
df.duplicated()
```

---

## Count Duplicates

```python
df.duplicated().sum()
```

---

## Remove Duplicates

```python
df.drop_duplicates()
```

---

# 3. Rename Columns

## [WHY]

Changes column names in the dataset.

## [USA]

```python
df.rename(
    columns={"Old":"New"},
    inplace=True
)
```

---

# 4. Change Data Type

## [WHY]

Converts one data type into another.

## [USA]

```python
df["Age"] = df["Age"].astype(int)
```

---

# Statistical Summary

## [WHY]

Displays summary statistics for numerical columns.

## [USA]

```python
df.describe()
```

---

## [RES] Expected Result

`describe()` shows:

* Count
* Mean
* Standard Deviation
* Minimum
* 25%
* 50% (Median)
* 75%
* Maximum

---

## Include All Columns

```python
df.describe(include="all")
```

---

# Relationship Analysis

Relationship analysis is used to understand how variables interact with each other.

---

# Correlation

## [WHY]

Measures the relationship between numerical variables.

Correlation shows how strongly numerical variables are related.

Values generally range between:

* `+1` → Strong positive relationship
* `0` → No relationship
* `-1` → Strong negative relationship

---

## [USA]

```python
df.corr(numeric_only=True)
```

---

## Visualize Correlation

```python
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.show()
```

---

# Data Visualization

Data visualization represents data graphically to identify patterns, trends, distributions, and relationships.

---

# Histogram

## [WHY]

Shows data distribution.

A histogram displays the frequency distribution of numerical data by dividing values into intervals called bins.

---

## [USA]

```python
sns.histplot(df["Age"])
plt.show()
```

---

# Box Plot

## [WHY]

Detects outliers.

A box plot displays the spread of data and identifies values that are significantly different from the rest of the dataset.

---

## [USA]

```python
sns.boxplot(
    x=df["Salary"]
)

plt.show()
```

---

# Scatter Plot

## [WHY]

Finds relationships between two variables.

A scatter plot displays the relationship between two numerical variables using points.

---

## [USA]

```python
sns.scatterplot(
    data=df,
    x="Age",
    y="Salary"
)

plt.show()
```

---

# Count Plot

## [WHY]

Counts categorical values.

A count plot displays the frequency of each category in a categorical variable.

---

## [USA]

```python
sns.countplot(
    data=df,
    x="Department"
)

plt.show()
```

---

# Common EDA Functions

## [FUN]

```text
head()
tail()
sample()
shape
info()
columns
dtypes
describe()
value_counts()
unique()
nunique()
isnull()
sum()
duplicated()
drop_duplicates()
dropna()
fillna()
rename()
astype()
corr()
sort_values()
groupby()
```

---

# Data Cleaning Checklist

## [MET]

✓ Load dataset
✓ View dataset
✓ Check shape
✓ Check data types
✓ Check missing values
✓ Fill or remove missing values
✓ Check duplicate values
✓ Remove duplicates
✓ Generate statistical summary
✓ Detect outliers
✓ Analyze relationships
✓ Visualize data

---

# Advantages

## [MET]

* Better understanding of data
* Detects data quality issues
* Improves Machine Learning accuracy
* Generates business insights
* Helps in feature selection
* Makes data ready for modeling

---

# Limitations

## [CAT]

* Time-consuming for large datasets
* Requires domain knowledge
* Mostly manual interpretation
* Visualization becomes difficult for huge datasets

---

# Quick Summary

| Function             | Description           |
| -------------------- | --------------------- |
| `head()`             | First 5 rows          |
| `tail()`             | Last 5 rows           |
| `shape`              | Rows and columns      |
| `info()`             | Dataset information   |
| `describe()`         | Statistical summary   |
| `isnull()`           | Missing values        |
| `isnull().sum()`     | Count missing values  |
| `duplicated()`       | Duplicate rows        |
| `duplicated().sum()` | Count duplicates      |
| `drop_duplicates()`  | Remove duplicates     |
| `dropna()`           | Remove missing values |
| `fillna()`           | Fill missing values   |
| `corr()`             | Correlation matrix    |
| `value_counts()`     | Frequency count       |
| `unique()`           | Unique values         |
| `groupby()`          | Group data            |

---

# Key Points

* EDA stands for Exploratory Data Analysis.

* EDA is performed before Machine Learning.

* Main goals of EDA:

  * Understand the data
  * Clean the data
  * Find patterns
  * Detect outliers
  * Analyze relationships
  * Generate business insights

* Common libraries:

  * Pandas
  * NumPy
  * Matplotlib
  * Seaborn

* A good EDA results in cleaner, more reliable data and better-performing Machine Learning models.

# Matplotlib – Basic Visualization

**Date:** 28/7/2026

---

# Keywords

## Main Topics

* Matplotlib
* Data Visualization
* Graphs and Charts
* Exploratory Data Analysis (EDA)
* Scientific Computing
* Machine Learning Visualization
* Business Reports
* Plot Customization

## Library

* matplotlib

## Installation

```bash
pip install matplotlib
```

## Python Alias

```python
import matplotlib.pyplot as plt
```

## Visualization Types

* Line Chart
* Bar Chart
* Horizontal Bar Chart
* Scatter Plot
* Histogram
* Pie Chart
* Box Plot
* Subplots

## Common Functions

* `plt.plot()`
* `plt.scatter()`
* `plt.bar()`
* `plt.barh()`
* `plt.hist()`
* `plt.pie()`
* `plt.boxplot()`
* `plt.figure()`
* `plt.title()`
* `plt.xlabel()`
* `plt.ylabel()`
* `plt.grid()`
* `plt.legend()`
* `plt.show()`
* `plt.savefig()`
* `plt.subplot()`

## Parameters

* `x`
* `y`
* `color`
* `linewidth`
* `linestyle`
* `marker`
* `markersize`
* `label`
* `figsize`
* `bins`
* `labels`
* `autopct`
* `alpha`

---

# Tags & References

| Tag     | Meaning                   |
| ------- | ------------------------- |
| `[LIB]` | Library                   |
| `[INS]` | Install this library      |
| `[ALI]` | Alias                     |
| `[WHY]` | Why this is used          |
| `[USC]` | Use Cases                 |
| `[MET]` | Methods                   |
| `[USA]` | Usage / Example Code      |
| `[RES]` | Expected Result           |
| `[SYN]` | Syntax                    |
| `[PAR]` | Parameters                |
| `[EXA]` | Example                   |
| `[ANE]` | Another Example           |
| `[CAT]` | Limitations / Cannot Have |
| `[FUN]` | Functions Used            |

---

# Quick Summary

* Matplotlib is a Python library used for creating graphs and charts.
* It is widely used for data visualization.
* It provides complete control over plot customization.
* It is the foundation library for Seaborn.
* Supports:

  * Line charts
  * Bar charts
  * Scatter plots
  * Histograms
  * Pie charts
  * Box plots
  * Subplots
* Imported using:

```python
import matplotlib.pyplot as plt
```

---

# Table of Contents

1. [What is Matplotlib](#what-is-matplotlib)
2. [Basic Usage](#basic-usage)
3. [Basic Syntax](#basic-syntax)
4. [Common Matplotlib Plots](#common-matplotlib-plots)
5. [Customization](#customization)
6. [Useful Parameters](#useful-parameters)
7. [Complete Example](#complete-example)
8. [Advantages](#advantages)
9. [Limitations](#limitations)
10. [Common Functions](#common-functions)
11. [Quick Summary](#quick-summary)
12. [Key Points](#key-points)

---

# What is Matplotlib?

## [WHY]

Matplotlib is a Python library for creating graphs and charts.

It is:

* Used for data visualization.
* Provides complete control over plot customization.
* The foundation library for Seaborn.

---

## [USC] Use Cases

Matplotlib is used for:

* Data Visualization
* Exploratory Data Analysis (EDA)
* Scientific Computing
* Machine Learning Visualization
* Business Reports

---

## [MET] Methods

Common visualization methods:

* Line Charts
* Bar Charts
* Scatter Plots
* Histograms
* Pie Charts
* Box Plots
* Subplots
* Figure Customization

---

# Basic Usage

## [USA]

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)
plt.title("Graph")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
```

## [RES]

Displays a simple line graph.

---

# Basic Syntax

## [SYN]

```python
plt.plot(x, y)

plt.title("Title")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
```

---

# Common Matplotlib Plots

# 1. Line Plot

## [WHY]

Displays trends or changes over time.

---

## [SYN]

```python
plt.plot(x, y)
```

---

## [PAR]

| Parameter   | Description    |
| ----------- | -------------- |
| `x`         | X-axis values  |
| `y`         | Y-axis values  |
| `color`     | Line color     |
| `linestyle` | Line style     |
| `linewidth` | Line thickness |
| `marker`    | Marker style   |

---

## [EXA]

```python
x = [1,2,3,4]
y = [10,20,30,40]

plt.plot(x, y)
plt.show()
```

---

## [ANE]

```python
plt.plot(
    x,
    y,
    color="red",
    marker="o",
    linestyle="--"
)

plt.show()
```

---

# 2. Scatter Plot

## [WHY]

Shows the relationship between two variables.

---

## [SYN]

```python
plt.scatter(x, y)
```

---

## [PAR]

* `x`
* `y`
* `color`
* `s`

---

## [EXA]

```python
plt.scatter(x, y)
plt.show()
```

---

# 3. Bar Chart

## [WHY]

Compares values between categories.

---

## [SYN]

```python
plt.bar(x, y)
```

---

## [EXA]

```python
plt.bar(x, y)
plt.show()
```

---

# 4. Horizontal Bar Chart

## [WHY]

Displays bar chart horizontally.

---

## [SYN]

```python
plt.barh(x, y)
```

---

## [EXA]

```python
plt.barh(x, y)
plt.show()
```

---

# 5. Histogram

## [WHY]

Displays frequency distribution.

---

## [SYN]

```python
plt.hist(data)
```

---

## [PAR]

* `bins`
* `color`

---

## [EXA]

```python
data = [1,2,2,3,3,3,4,4,5]

plt.hist(data)
plt.show()
```

---

# 6. Pie Chart

## [WHY]

Shows percentage contribution.

---

## [SYN]

```python
plt.pie(values)
```

---

## [PAR]

* `labels`
* `autopct`
* `colors`

---

## [EXA]

```python
values = [40,30,20,10]
labels = ["A","B","C","D"]

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)

plt.show()
```

---

# 7. Box Plot

## [WHY]

Shows spread and outliers.

---

## [SYN]

```python
plt.boxplot(data)
```

---

## [EXA]

```python
data = [2,4,5,6,8,10,12]

plt.boxplot(data)
plt.show()
```

---
# Matplotlib – Basic Visualization

## Customization

Matplotlib provides multiple options to customize plots according to visualization requirements.

---

# Change Figure Size

## [USA]

```python
plt.figure(figsize=(8,5))
```

### Explanation

`figsize` controls the width and height of the figure.

---

# Change Line Color

## [USA]

```python
plt.plot(
    x,
    y,
    color="green"
)
```

### Explanation

The `color` parameter changes the color of the plot line.

---

# Change Line Style

## [USA]

```python
plt.plot(
    x,
    y,
    linestyle="--"
)
```

### Explanation

The `linestyle` parameter changes the appearance of the line.

Examples:

* Solid line
* Dashed line
* Dotted line

---

# Add Marker

## [USA]

```python
plt.plot(
    x,
    y,
    marker="o"
)
```

### Explanation

The `marker` parameter adds symbols to individual data points.

---

# Add Grid

## [USA]

```python
plt.grid(True)
```

### Explanation

Adds grid lines to improve readability of the graph.

---

# Add Legend

## [USA]

```python
plt.plot(
    x,
    y,
    label="Revenue"
)

plt.legend()
```

### Explanation

The legend displays labels for different plots.

---

# Add Title & Labels

## [USA]

```python
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
```

### Explanation

* `title()` → Adds graph title.
* `xlabel()` → Adds label for X-axis.
* `ylabel()` → Adds label for Y-axis.

---

# Useful Parameters

## [PAR]

| Parameter    | Description       |
| ------------ | ----------------- |
| `x`          | X-axis values     |
| `y`          | Y-axis values     |
| `color`      | Line color        |
| `linewidth`  | Line thickness    |
| `linestyle`  | Line style        |
| `marker`     | Marker style      |
| `markersize` | Marker size       |
| `label`      | Legend text       |
| `figsize`    | Figure size       |
| `bins`       | Histogram bins    |
| `labels`     | Pie chart labels  |
| `autopct`    | Percentage format |
| `alpha`      | Transparency      |

---

# Complete Example

## [USA]

```python
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,30,40]

plt.figure(figsize=(8,5))

plt.plot(
    x,
    y,
    color="blue",
    marker="o",
    linewidth=2,
    label="Revenue"
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.grid(True)
plt.legend()

plt.show()
```

---

## [RES]

Displays a customized line graph with:

* Title
* Labels
* Grid
* Markers
* Legend

---

# Advantages

## [MET]

* Easy to learn
* Highly customizable
* Large variety of charts
* Widely used in Python
* Works well with NumPy & Pandas
* Base library for Seaborn

---

# Limitations

## [CAT]

* Requires more code than Seaborn
* Default styles are less attractive
* Statistical plots require manual coding

---

# Common Functions

## [FUN]

```text
plt.plot()
plt.scatter()
plt.bar()
plt.barh()
plt.hist()
plt.pie()
plt.boxplot()
plt.figure()
plt.title()
plt.xlabel()
plt.ylabel()
plt.grid()
plt.legend()
plt.show()
plt.savefig()
plt.subplot()
```

---

# Quick Summary

| Function    | Description          |
| ----------- | -------------------- |
| `plot()`    | Line graph           |
| `scatter()` | Scatter plot         |
| `bar()`     | Vertical bar chart   |
| `barh()`    | Horizontal bar chart |
| `hist()`    | Histogram            |
| `pie()`     | Pie chart            |
| `boxplot()` | Box plot             |
| `figure()`  | Create figure        |
| `show()`    | Display graph        |
| `savefig()` | Save graph           |

---

# Key Points

* Matplotlib is the most popular Python visualization library.
* Imported using:

```python
import matplotlib.pyplot as plt
```

* Used for creating:

  * Static graphs
  * Animated graphs
  * Interactive graphs

* Provides complete customization of plots.

* Seaborn is built on top of Matplotlib.

---
# Seaborn – Statistical Visualization

**Date:** 28/7/2026

---

# Keywords

## Main Topics

* Seaborn
* Statistical Visualization
* Data Visualization
* Exploratory Data Analysis (EDA)
* Machine Learning Visualization
* Correlation Analysis
* Pandas DataFrame Visualization
* Numerical Data
* Categorical Data
* Probability Density

## Library

* seaborn

## Installation

```bash
pip install seaborn
```

## Python Aliases

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

## Visualization Types

* Scatter Plot
* Line Plot
* Bar Plot
* Count Plot
* Histogram
* Box Plot
* Violin Plot
* Pair Plot
* Heatmap
* KDE Plot

## Common Functions

* `sns.scatterplot()`
* `sns.lineplot()`
* `sns.barplot()`
* `sns.countplot()`
* `sns.histplot()`
* `sns.boxplot()`
* `sns.violinplot()`
* `sns.pairplot()`
* `sns.heatmap()`
* `sns.kdeplot()`
* `sns.set_theme()`
* `sns.load_dataset()`

## Parameters

* `data`
* `x`
* `y`
* `hue`
* `style`
* `size`
* `palette`
* `color`
* `annot`
* `cmap`
* `kde`
* `fill`
* `bins`

---

# Tags & References

| Tag     | Meaning                   |
| ------- | ------------------------- |
| `[LIB]` | Library                   |
| `[INS]` | Install this library      |
| `[ALI]` | Alias                     |
| `[WHY]` | Why this is used          |
| `[USC]` | Use Cases                 |
| `[MET]` | Methods                   |
| `[USA]` | Usage / Example Code      |
| `[RES]` | Expected Result           |
| `[SYN]` | Syntax                    |
| `[PAR]` | Parameters                |
| `[EXA]` | Example                   |
| `[ANE]` | Another Example           |
| `[OPT]` | Optional                  |
| `[CAT]` | Limitations / Cannot Have |
| `[FUN]` | Functions Used            |

---

# Quick Summary

* Seaborn is a Python statistical data visualization library.
* It is built on top of Matplotlib.
* It works seamlessly with Pandas DataFrames.
* It is mainly used for:

  * Data Analysis
  * Exploratory Data Analysis (EDA)
  * Statistical Visualization
  * Machine Learning Visualization
  * Correlation Analysis

Common visualization functions:

| Function        | Purpose                                  |
| --------------- | ---------------------------------------- |
| `scatterplot()` | Relationship between numerical variables |
| `lineplot()`    | Trend visualization                      |
| `barplot()`     | Compare category averages                |
| `countplot()`   | Count categorical values                 |
| `histplot()`    | Data distribution                        |
| `boxplot()`     | Quartiles and outliers                   |
| `violinplot()`  | Distribution with density                |
| `pairplot()`    | Pairwise relationships                   |
| `heatmap()`     | Correlation matrix                       |
| `kdeplot()`     | Probability density estimation           |

---

# Table of Contents

1. [What is Seaborn](#what-is-seaborn)
2. [Load Sample Dataset](#load-sample-dataset)
3. [Basic Syntax](#basic-syntax)
4. [Common Seaborn Plots](#common-seaborn-plots)
5. [Customization](#customization)
6. [Useful Parameters](#useful-parameters)
7. [Complete Example](#complete-example)
8. [Advantages](#advantages)
9. [Limitations](#limitations)
10. [Common Functions](#common-functions)
11. [Quick Summary](#quick-summary)
12. [Key Points](#key-points)

---

# What is Seaborn?

## [LIB]

```text
seaborn
```

---

## [INS]

```bash
pip install seaborn
```

---

## [ALI]

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

---

## [WHY]

Seaborn is:

* A Python statistical data visualization library.
* Built on top of Matplotlib.
* Works seamlessly with Pandas DataFrames.
* Used to analyze and visualize data easily.

---

## [USC] Use Cases

Seaborn is used for:

* Data Analysis
* Exploratory Data Analysis (EDA)
* Statistical Visualization
* Machine Learning Data Visualization
* Correlation Analysis

---

## [MET] Methods

Seaborn provides:

* Attractive default themes
* Built-in statistical plots
* Easy Pandas integration
* Support for categorical and numerical data
* Built-in datasets

---

# Load Sample Dataset

## [USA]

```python
import seaborn as sns

tips = sns.load_dataset("tips")
print(tips.head())
```

---

## [RES]

Displays the first 5 rows of the `"tips"` dataset.

---

## [MET]

Built-in datasets:

* tips
* iris
* titanic
* penguins
* diamonds

---

# Basic Syntax

## [SYN]

```python
sns.plot_type(
    data=dataframe,
    x="column1",
    y="column2"
)

plt.show()
```

---

## [EXA]

```python
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.show()
```

---

# Common Seaborn Plots

# 1. Scatter Plot

## [WHY]

Shows the relationship between two numerical variables.

---

## [SYN]

```python
sns.scatterplot(
    data=df,
    x="column1",
    y="column2"
)
```

---

## [PAR]

* `data`
* `x`
* `y`
* `hue`
* `style`
* `size`

---

## [EXA]

```python
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.show()
```

---

## [ANE]

```python
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex"
)

plt.show()
```

---

# 2. Line Plot

## [WHY]

Displays trends over ordered or time-series data.

---

## [SYN]

```python
sns.lineplot(
    data=df,
    x="column1",
    y="column2"
)
```

---

## [PAR]

* `data`
* `x`
* `y`
* `hue`
* `style`

---

## [EXA]

```python
sns.lineplot(
    data=tips,
    x="size",
    y="tip"
)

plt.show()
```

---

# 3. Bar Plot

## [WHY]

Compares average values of categories.

---

## [SYN]

```python
sns.barplot(
    data=df,
    x="column1",
    y="column2"
)
```

---

## [PAR]

* `data`
* `x`
* `y`
* `palette`
* `color`

---

## [EXA]

```python
sns.barplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.show()
```

---

# 4. Count Plot

## [WHY]

Counts occurrences of each category.

---

## [SYN]

```python
sns.countplot(
    data=df,
    x="column"
)
```

---

## [EXA]

```python
sns.countplot(
    data=tips,
    x="day"
)

plt.show()
```

---

# 5. Histogram

## [WHY]

Displays numerical data distribution.

---

## [SYN]

```python
sns.histplot(
    data=df,
    x="column"
)
```

---

## [PAR]

* `data`
* `x`
* `kde`
* `bins`

---

## [EXA]

```python
sns.histplot(
    data=tips,
    x="total_bill"
)

plt.show()
```

---

## [ANE]

```python
sns.histplot(
    data=tips,
    x="total_bill",
    kde=True
)

plt.show()
```

---
# Data Sourcing, Data Ingestion & SQLite3 + Pandas

**Date:** Not Provided

---

# Keywords

## Main Topics

* Data Sourcing
* Data Ingestion
* Data Sources
* Structured Data
* Semi-Structured Data
* Unstructured Data
* Batch Ingestion
* Real-Time Ingestion
* SQLite Database
* Pandas Integration
* SQL Tables
* DataFrame Creation
* Data Merging
* ETL Pipeline
* Data Warehouse
* Data Lake

## Libraries

* sqlite3
* pandas

## Installation

```bash
pip install pandas
```

## Python Imports

```python
import sqlite3
import pandas as pd
```

## Database Concepts

* Relational Database
* SQLite
* Tables
* Primary Key
* Records
* SQL Queries
* Database Connection
* Cursor
* Commit
* DataFrame

## Data Operations

* Create Database
* Create Tables
* Insert Records
* Read SQL Tables
* Merge DataFrames
* Inner Join
* Left Join
* Right Join
* Outer Join

---

# Tags & References

| Tag     | Meaning              |
| ------- | -------------------- |
| `[WHY]` | Why this is used     |
| `[USC]` | Use Cases            |
| `[MET]` | Methods              |
| `[TYS]` | Types                |
| `[LIB]` | Library              |
| `[INS]` | Installation         |
| `[ALI]` | Alias                |
| `[USA]` | Usage / Example Code |
| `[RES]` | Expected Result      |

---

# Quick Summary

* Data Sourcing is the process of collecting data from different sources.

* Data Ingestion is the process of moving collected data into storage or processing systems.

* Data sources can be:

  * Internal
  * External
  * Structured
  * Semi-Structured
  * Unstructured

* SQLite is a lightweight file-based relational database.

* Pandas can read SQL tables and convert them into DataFrames.

* Pandas `merge()` combines multiple datasets using common columns.

* Common merge types:

  * Inner
  * Left
  * Right
  * Outer

---

# Table of Contents

1. [Data Sourcing](#data-sourcing)
2. [Data Ingestion](#data-ingestion)
3. [Types of Data Sources](#types-of-data-sources)
4. [Common Data Sources](#common-data-sources)
5. [Quick Difference](#quick-difference)
6. [SQLite3 + Pandas](#sqlite3--pandas)
7. [Database Creation](#database-creation)
8. [Create Tables](#create-tables)
9. [Insert Records](#insert-records)
10. [Read Tables Using Pandas](#read-tables-using-pandas)
11. [Merging Tables Using Pandas](#merging-tables-using-pandas)
12. [Merge Types](#merge-types)

---

# Data Sourcing

## [WHY]

Data Sourcing is the process of collecting data from different sources for analysis, reporting, or Machine Learning.

---

## [USC] Use Cases

Data sourcing is used in:

* Business Analytics
* Machine Learning
* Data Engineering
* Data Warehousing
* Reporting

---

## [MET] Methods

Types of data sourcing methods:

* Internal Sources
* External Sources
* Structured Data
* Semi-Structured Data
* Unstructured Data

---

# Data Ingestion

## [WHY]

Data Ingestion is the process of importing, collecting, and transferring data from one or more sources into a storage system or processing platform.

---

## [USC] Use Cases

Data ingestion is used in:

* Data Warehouse
* Data Lake
* ETL Pipeline
* Machine Learning Pipeline

---

## [TYS] Types of Data Ingestion

## 1. Batch Ingestion

* Data is collected at scheduled intervals.
* Suitable for historical data.

### Example

```
Daily sales report
```

---

## 2. Real-Time (Streaming) Ingestion

* Data arrives continuously.
* Suitable for live applications.

### Example

```
Stock market data
IoT sensors
```

---

# Types of Data Sources

## [TYS]

---

# 1. Internal Data Sources

Examples:

* Company databases
* ERP Systems
* CRM Systems
* Sales Records
* Employee Records

---

# 2. External Data Sources

Examples:

* Government datasets
* Public APIs
* Social Media
* Third-party vendors
* Market research reports

---

# 3. Structured Data

## Definition

* Organized in rows and columns.
* Stored in SQL databases.

## Examples

* MySQL
* PostgreSQL

---

# 4. Semi-Structured Data

## Definition

* Has some structure but no fixed schema.

## Examples

* JSON
* XML
* CSV

---

# 5. Unstructured Data

## Definition

* No predefined format.

## Examples

* Images
* Videos
* Audio
* Emails
* PDFs

---

# Common Data Sources

## [MET]

Common data sources include:

* SQL Databases
* NoSQL Databases
* CSV Files
* Excel Files
* JSON Files
* XML Files
* APIs
* Cloud Storage
* IoT Devices
* Social Media
* Log Files

---

# Quick Difference

| Concept        | Meaning                                                       |
| -------------- | ------------------------------------------------------------- |
| Data Sourcing  | Finding and collecting data                                   |
| Data Ingestion | Moving collected data into a system for storage or processing |

---

# SQLite3 + Pandas

## Database Creation

---

# Libraries

## [LIB]

```text
sqlite3
pandas
```

---

## [INS]

```bash
pip install pandas
```

---

## [ALI]

```python
import sqlite3
import pandas as pd
```

---

## [WHY]

SQLite is a lightweight, file-based relational database.

It is used to store structured data without requiring a database server.

---

## [USA]

```python
conn = sqlite3.connect("shop.db")

cur = conn.cursor()
```

---

## [RES]

Creates (or opens) `"shop.db"` database.

---

# Create Tables

---

# Customer Table

## [USA]

```python
cur.execute("""
CREATE TABLE IF NOT EXISTS Customer(
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    city TEXT
)
""")
```

---

# Product Table

## [USA]

```python
cur.execute("""
CREATE TABLE IF NOT EXISTS Product(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    price REAL
)
""")
```

---

# Sales Table

## [USA]

```python
cur.execute("""
CREATE TABLE IF NOT EXISTS Sales(
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    sale_date TEXT
)
""")
```

---
# KEYWORDS / TAGS
- SQLITE3
- PANDAS
- DATABASE
- SQL DATABASE
- TABLE CREATION
- INSERT RECORDS
- READ SQL TABLES
- DATAFRAME
- MERGING TABLES
- MERGE TYPES
- EDA
- DATA ANALYSIS
- BUSINESS INSIGHTS
- DATA EXPORT
- ETL
- ELT
- DATA PIPELINE

# TAG REFERENCE USED IN NOTES
- [LIB] = Library
- [INS] = Install this library
- [ALI] = Alias
- [WHY] = Why this is used
- [USC] = Use Cases
- [MET] = Methods
- [TYS] = Types
- [USA] = Usage (Example Code)
- [RES] = Expected Result
- [FUN] = Functions Used
- [OPT] = Optional
- [COM] = CLI Command
- [RUN] = Run Command


# INSERT RECORDS
================

## [USA]

```python
customers = [
    (1,"John","New York"),
    (2,"Alice","Chicago"),
    (3,"David","Boston")
]

products = [
    (101,"Laptop",850),
    (102,"Mouse",20),
    (103,"Keyboard",40)
]

sales = [
    (1,1,101,1,"2025-01-01"),
    (2,2,102,2,"2025-01-03"),
    (3,1,103,1,"2025-01-05")
]

cur.executemany(
    "INSERT INTO Customer VALUES(?,?,?)",
    customers
)

cur.executemany(
    "INSERT INTO Product VALUES(?,?,?)",
    products
)

cur.executemany(
    "INSERT INTO Sales VALUES(?,?,?,?,?)",
    sales
)

conn.commit()
````

---

# READ TABLES USING PANDAS

=========================

## [USA]

```python
customer_df = pd.read_sql(
    "SELECT * FROM Customer",
    conn
)

product_df = pd.read_sql(
    "SELECT * FROM Product",
    conn
)

sales_df = pd.read_sql(
    "SELECT * FROM Sales",
    conn
)
```

## [RES]

Converts SQL tables into Pandas DataFrames.

---

# MERGING TABLES USING PANDAS

=============================

## Customer + Sales

### [USA]

```python
merge1 = pd.merge(
    customer_df,
    sales_df,
    on="customer_id",
    how="inner"
)
```

---

## Sales + Product

### [USA]

```python
final_df = pd.merge(
    merge1,
    product_df,
    on="product_id",
    how="inner"
)
```

## [RES]

Final DataFrame contains:

```
Customer
    +
Sales
    +
Product
```

---

# MERGE TYPES

==============

## [TYS]

### inner

Returns matching records only.

### left

Returns all rows from left table.

### right

Returns all rows from right table.

### outer

Returns all records from both tables.

---

# BASIC EDA

===========

## View Data

```python
df.head()
```

---

## Last Records

```python
df.tail()
```

---

## Dataset Shape

```python
df.shape
```

---

## Column Names

```python
df.columns
```

---

## Dataset Information

```python
df.info()
```

---

## Statistics

```python
df.describe()
```

---

## Missing Values

```python
df.isnull().sum()
```

---

## Duplicate Rows

```python
df.duplicated().sum()
```

---

## Unique Values

```python
df["city"].unique()
```

---

## Frequency Count

```python
df["city"].value_counts()
```

---

## Sorting

```python
df.sort_values("price")
```

---

## Filtering

```python
df[df["price"] > 500]
```

---

## Grouping

```python
df.groupby("city")["quantity"].sum()
```

---

## Highest Price Product

```python
df.nlargest(5,"price")
```

---

## Lowest Price Product

```python
df.nsmallest(5,"price")
```

---

# NEW COLUMN

=============

## [USA]

```python
df["Total"] = (
    df["price"] *
    df["quantity"]
)
```

---

# BUSINESS INSIGHTS

===================

## Total Revenue

```python
df["Total"].sum()
```

---

## Average Revenue

```python
df["Total"].mean()
```

---

## Highest Sale

```python
df["Total"].max()
```

---

## Lowest Sale

```python
df["Total"].min()
```

---

## Top Customers

```python
df.groupby(
    "customer_name"
)["Total"].sum()
```

---

## Top Selling Products

```python
df.groupby(
    "product_name"
)["quantity"].sum()
```

---

## Sales by City

```python
df.groupby(
    "city"
)["Total"].sum()
```

---

# SAVE RESULT

=============

## [USA]

```python
df.to_csv(
    "sales_report.csv",
    index=False
)
```

---

# CLOSE DATABASE

================

## [USA]

```python
conn.close()
```

---

# COMMON SQLITE FUNCTIONS

=========================

## [FUN]

```
connect()
cursor()
execute()
executemany()
commit()
close()
```

---

# COMMON PANDAS FUNCTIONS

=========================

## [FUN]

```
pd.read_sql()
pd.merge()
head()
tail()
shape
info()
describe()
isnull()
duplicated()
unique()
value_counts()
sort_values()
groupby()
nlargest()
nsmallest()
to_csv()
```

---

# WORKFLOW

===========

```
Create Database
        ↓
Create Tables
        ↓
Insert Records
        ↓
Commit Changes
        ↓
Read Tables using read_sql()
        ↓
Merge Tables using pd.merge()
        ↓
Perform EDA
        ↓
Generate Business Insights
        ↓
Export Report
        ↓
Close Database
```

---

# KEY POINTS

============

* sqlite3 creates a local file-based database.
* connect() opens or creates the database.
* cursor() executes SQL queries.
* executemany() inserts multiple records.
* commit() permanently saves changes.
* pd.read_sql() loads SQL tables into DataFrames.
* pd.merge() joins multiple DataFrames.
* EDA helps understand, clean, and analyze data.
* Always close the connection using conn.close().

---

# ETL

=======

## Full Form

ETL = Extract, Transform, Load

## ETL Process Flow

```
CSV, Excel, API, SQL
        |
        V
Extract
        |
        V
Raw Collected Data
        |
        V
Transform
(Clean + Convert + Merge + Validate)
        |
        V
Clean Data
        |
        V
Load
        |
        V
Data Warehouse / Database
```

## Extract

Collecting data from different sources.

Examples:

* CSV
* Excel
* API
* SQL Database

## Transform

Process of converting raw collected data into clean usable data.

Operations:

* Clean data
* Convert data types
* Merge data
* Validate data

## Load

Moving transformed clean data into storage systems.

Examples:

* Data Warehouse
* Database

---

# ELT

=======

## Full Form

ELT = Extract, Load, Transform

## Process

```
Extract Data
        |
        V
Load Data
        |
        V
Transform Data
```

## Usage

* Used in cloud environments.