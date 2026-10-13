# Pandas – Series, DataFrame & Data Transformation

> **Date:** 27/07/2026

---

# 📌 Keywords

- Pandas
- Series
- DataFrame
- Structured Data
- Data Engineering
- Data Science
- Data Analysis
- Index
- Position
- loc[]
- iloc[]
- dtype
- object
- category
- datetime64[ns]
- NaN
- NaT
- concat()
- drop()
- head()
- tail()
- describe()
- sort_values()
- sort_index()
- values
- shape
- size
- ndim
- index
- map()
- apply()
- lambda
- memory_usage()
- pivot()
- pivot_table()
- set_index()
- reset_index()
- MultiIndex
- merge()
- fillna()
- dropna()
- isna()
- notna()
- ffill()
- bfill()
- to_datetime()
- date_range()

---

# 🏷️ Tags / Identifiers Used

- LIB
- USA
- PAR
- SYN
- WHY
- EXA
- MET
- CAT
- ALI
- RES
- OPT
- ANE
- FUN
- DAM
- TYS
- VER
- USC
- COM
- INS
- RUN
- NOT
- MEMORY

---

# 📖 Abbreviations

| Tag | Meaning |
|------|---------|
| LIB | Library |
| USA | Usage (Example Code) |
| PAR | Parameters |
| SYN | Syntax |
| WHY | Why this is Used |
| EXA | Example |
| MET | Methods |
| CAT | Cannot Have It |
| ALI | Alias |
| RES | Expected Result |
| OPT | Optional |
| ANE | Another Example |
| FUN | Functions Used |
| DAM | Data Members |
| TYS | Types |
| VER | Version *(Used contextually; original note says Python Version)* |
| USC | Use Cases |
| COM | CLI Command |
| INS | Install Library |
| RUN | Run Command |
| NOT | Important Note |
| MEMORY | Memory Trick |

---

# Pandas

## [LIB]

```python
import pandas as pd
```

Pandas is a Python library for working with **structured/tabular data**.

## Features

- Used in Data Engineering
- Used in Data Science
- Used in Data Analysis
- Works with structured datasets
- Main Data Types:
  - Series
  - DataFrame

---

# Series

A **Series** is a **one-dimensional labeled array** capable of storing values of the same or different data types.

## Features

- One-dimensional
- Mutable
- Ordered
- Fast
- Uses automatic default index
- Can also use custom indexes
- Stores homogeneous or heterogeneous data

Supported dtypes include:

- int64
- float64
- bool
- object
- str
- category
- datetime64[ns]

---

# Position vs Index

## Position

- Physical location (0-based)
- Uses `iloc[]`

```
iloc
=
Integer Location
```

---

## Index

- Label assigned to a row or column
- Uses `loc[]`

```
loc
=
Label Location
```

---

## Important Notes

- Pandas aligns data using **index labels**, not positions.
- Arithmetic operations align by index.
- Element access using `iloc[]` is position-based.

---

## [USA]

```python
import pandas as pd

s1 = pd.Series(["k", "l", "j"])

print(s1)

m1 = pd.Series(
    ["Iron Man", "Captain America", "Thor"],
    [1, 2, 3]
)
```

---

## [NOT]

The **object** dtype comes from **NumPy**.

- NumPy arrays require every element to occupy the same number of bytes.
- Numeric types like `int64` and `float64` always occupy **8 bytes**.
- Strings have variable lengths, so NumPy stores references (pointers) to Python string objects instead of storing the string bytes directly.
- Therefore, Pandas stores strings using the **object** dtype.

---

# Series Methods

## [MET]

### concat()

Concatenates two or more Series.

#### [SYN]

```python
pd.concat([series1, series2])
```

> **Correction:** `pd.concat()` accepts an iterable (such as a list) of Series/DataFrames.

---

### drop()

Drops one or multiple labels.

#### [SYN]

```python
series.drop(label)

series.drop([label1, label2])
```

---

### head()

Returns the first **5** records by default.

```python
series.head()

series.head(n)
```

---

### tail()

Returns the last **5** records by default.

```python
series.tail()

series.tail(n)
```

---

### Aggregate Methods

```python
.max()

.min()

.sum()

.mean()
```

---

### Data Members

| Member | Description |
|----------|-------------|
| index | Returns index labels |
| values | Returns underlying values |
| shape | Returns tuple `(length,)` |
| size | Number of elements |
| ndim | Number of dimensions |

> **Correction:** For a Series, `shape` returns `(length,)`, not `(rows, columns)`.

---

### Other Methods

```python
.sort_values()
```

Sort by values.

```python
.sort_index()
```

Sort by index.

```python
.describe()
```

Returns descriptive statistics.

---

# Category dtype

`category` is a special dtype used for repeated categorical values.

Benefits:

- Saves memory
- Stores unique categories
- Faster comparisons

---

## [USA]

```python
colors = pd.Series(
    ["R", "B", "R"],
    dtype="category"
)

print(colors)
```

> **Correction:** `dtype="category"` should be passed as a string.

---

## [RES]

```
Categories (2, object):
['B', 'R']
```

> Categories are displayed in sorted order by default.

---

## Methods

```python
.cat.codes
```

Returns integer codes assigned to categories.

---

```python
.isna()
```

Checks missing values.

---

```python
.notna()
```

Checks non-missing values.

---

```python
.dropna()
```

Removes missing values.

---

```python
.fillna()
```

Replaces missing values.

---

```python
.ffill()
```

Forward Fill.

Fills missing values using the **previous valid value**.

> **Correction:** Original note states "immediate after value"; actually `ffill()` copies the previous value forward.

---

```python
.bfill()
```

Backward Fill.

Fills missing values using the **next valid value**.

---

# Datetime

Pandas datetime dtype:

```
datetime64[ns]
```

Stores both date and time.

Missing datetime value:

```
NaT
```

(Not a Time)

---

## [USA]

```python
s = pd.to_datetime(

    pd.Series([
        "2025-01-01",
        "2025-01-02"
    ])

)
```

---

## [MET]

```python
pd.to_datetime()
```

Convert to datetime.

---

```python
pd.date_range()
```

Generate date sequence.

---

### Date Components

```python
.dt.year

.dt.month

.dt.day

.dt.hour

.dt.minute

.dt.second
```

---

### Names

```python
.dt.day_name()

.dt.month_name()
```

---

### Formatting

```python
.dt.strftime()
```

---

### Other Methods

```python
.min()

.max()

.sort_values()

.isna()

.fillna()

.dropna()
```

---

## Format Codes

| Format | Meaning |
|---------|----------|
| %Y | Year |
| %m | Month |
| %d | Day |
| %H | Hour |
| %M | Minute |
| %S | Second |

---

## Frequency Codes

| Code | Meaning |
|------|----------|
| D | Day |
| W | Week |
| M | Month |
| Y | Year |

---

## NaT

Represents missing datetime values.

---

# DataFrame

A **DataFrame** is a **two-dimensional labeled data structure** consisting of multiple Series.

Similar to:

- Excel Sheet
- CSV File
- SQL Table

---

## Features

- Two-dimensional
- Collection of Series
- Mutable
- Ordered
- Columns can have different dtypes

---

## Structure

| Component | Meaning |
|------------|----------|
| Rows | Records |
| Columns | Features |
| Index | Row Labels |
| Values | Actual Data |

---

## [USA]

```python
import pandas as pd

df = pd.DataFrame({

    "Name": [
        "one",
        "two",
        "three"
    ],

    "Age": [
        12,
        23,
        34
    ]

})

print(df)
```

---

# Creating DataFrame from Series

## [SYN]

```python
df = pd.DataFrame({

    "column1": series1,

    "column2": series2

})
```

Index can also be specified using the `index=` parameter.

---

# Index

Represents row labels.

- Default starts at 0
- Can use custom labels

---

## Attributes

```python
.index
```

Returns row labels.

---

```python
.columns
```

Returns column names.

---

# DataFrame Attributes

| Attribute | Description |
|------------|-------------|
| shape | (rows, columns) |
| size | Total values |
| ndim | Always 2 |
| values | Underlying NumPy array |
| dtypes | Data type of each column |

---

# Accessing Data

```python
df["column"]
```

Single column.

---

```python
df[["col1", "col2"]]
```

Multiple columns.

---

```python
df.loc[]
```

Label-based access.

---

```python
df.iloc[]
```

Position-based access.

---

# Adding / Removing Data

```python
df["new_col"] = values
```

Adds a new column.

---

```python
df.drop()
```

Removes rows or columns.

---

```python
df.rename()
```

Renames rows or columns.

---

# Common Methods

```python
.head()
```

First five rows.

```python
.tail()
```

Last five rows.

```python
.info()
```

Summary information.

```python
.describe()
```

Statistical summary.

```python
.sort_values()
```

Sort by values.

```python
.sort_index()
```

Sort by index.

---

# Missing Values

Missing values are represented using:

```
NaN

None
```

---

Methods

```python
.isna()

.notna()

.dropna()

.fillna()
```

---

# Combining DataFrames

```python
pd.concat()
```

Combine vertically or horizontally.

---

```python
pd.merge()
```

Join DataFrames using common columns.

---

# Selecting Rows

```python
df.loc[row_label]
```

Uses index labels.

---

```python
df.iloc[row_position]
```

Uses row position.

---

# DataFrame vs Series

| Series | DataFrame |
|---------|-----------|
| 1D | 2D |
| Single Column | Multiple Columns |
| One-dimensional | Collection of Series |

---

# pivot()

Reshapes a DataFrame by converting unique values from one column into new columns.

Unlike `pivot_table()`, **pivot() does not perform aggregation**, so each `(index, column)` pair must be unique.

---

## [SYN]

```python
df.pivot(

    index=<row-column>,

    columns=<column-to-expand>,

    values=<value-column>

)
```

---

## [USA]

```python
import pandas as pd

df = pd.DataFrame({

    "Name": ["A", "A", "B", "B"],

    "Year": [2023, 2024, 2023, 2024],

    "Sales": [100, 150, 200, 250]

})

result = df.pivot(

    index="Name",

    columns="Year",

    values="Sales"

)

print(result)
```

---

## [RES]

| Name | 2023 | 2024 |
|------|------|------|
| A | 100 | 150 |
| B | 200 | 250 |

---

## Parameters

| Parameter | Purpose |
|------------|----------|
| index | Row labels |
| columns | New column names |
| values | Cell values |

---

## Difference

### pivot()

- Reshape only
- No aggregation
- Duplicate `(index, column)` combinations are **not allowed**

---

### pivot_table()

- Reshape + Aggregate
- Supports duplicate keys
- Supports `sum`, `mean`, `count`, etc.

---

## [SYN]

```python
df.pivot_table(

    index=<row>,

    columns=<column>,

    values=<value>,

    aggfunc=<function>

)
```

---

## MEMORY

```
pivot()
=
Rearrange Data

pivot_table()
=
Rearrange + Calculate
```

---

# set_index()

Converts one or more columns into the DataFrame index.

By default:

- Removes the original column (`drop=True`)
- Replaces the default integer index

Useful for `loc[]` operations.

---

## [SYN]

```python
df.set_index(column)
```

```python
df.set_index(column, inplace=True)
```

---

## Keep Original Column

```python
df.set_index(

    "ID",

    drop=False

)
```

---

## Modify Original DataFrame

```python
df.set_index(

    "ID",

    inplace=True

)
```

---

## reset_index()

Converts index back into a normal column and restores the default integer index.

```python
df.reset_index()
```

---

## MultiIndex

```python
df.set_index(["col1", "col2"])
```

Creates a hierarchical (multi-level) index.

---

## MEMORY

```
set_index()
=
Column → Index

reset_index()
=
Index → Column

loc[]
=
Search Using Labels
```

---

# map()

Applies a function **element by element** to a **Series**.

Returns a new Series.

---

## [USA]

```python
import pandas as pd

s = pd.Series([1,2,3,4])

print(

    s.map(

        lambda x: x * 10

    )

)
```

---

# apply()

Applies a function to each element in a Series or along an axis in a DataFrame.

> **Correction:** `apply()` is **not only for DataFrames**. It works with both **Series** and **DataFrames**.

- **Series.apply()** → element-wise.
- **DataFrame.apply()** → row-wise or column-wise using the `axis` parameter.

---

## [USA]

```python
ages = pd.Series([20, 25, 30])

print(

    ages.apply(

        lambda x: x + 5

    )

)

print(

    ages.memory_usage()

)
```

---

## memory_usage()

Returns the memory consumed by a Series or DataFrame (in bytes).

Useful for optimizing memory usage when working with large datasets.