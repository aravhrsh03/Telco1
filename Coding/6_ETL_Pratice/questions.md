
# Data Engineering ETL Practice Questions

## Question 1: Customer Order ETL Pipeline

### Scenario
A retail company maintains customer, product, and order information in separate CSV files.  
Build an ETL pipeline to combine these datasets and generate a sales report.

### Input Files

#### orders.csv

| OrderID | CustomerID | ProductID | Quantity |
|---|---|---|---|
|101|1|P101|2|
|102|2|P102|1|
|103|3|P101|3|
|104|4|P103|2|
|105|2|P104|5|

#### customers.csv

| CustomerID | CustomerName | City |
|---|---|---|
|1|John|Chennai|
|2|Emma|Bangalore|
|3|Raj|Hyderabad|
|4||Pune|

#### products.csv

| ProductID | Product | Price |
|---|---|---|
|P101|Laptop|50000|
|P102|Mouse|800|
|P103|Keyboard|1500|
|P104|Monitor|12000|

---

### ETL Requirements

1. Read all CSV files.
2. Validate schema and column names.
3. Handle missing customer names.
4. Replace missing customer names with `"Unknown"`.
5. Join orders with customer details.
6. Join the result with product details.
7. Create a new column:

```

TotalSales = Quantity × Price

```

8. Save the final output as:

```

final_sales.csv

```

---

### Expected Output

| OrderID | Customer | Product | TotalSales |
|---|---|---|---|
|101|John|Laptop|100000|
|102|Emma|Mouse|800|
|103|Raj|Laptop|150000|
|104|Unknown|Keyboard|3000|
|105|Emma|Monitor|60000|

---

### Test Cases

|Test ID|Scenario|Expected Result|
|-|-|-|
|TC01|Missing customer name|Replaced with Unknown|
|TC02|Quantity=2 and Price=50000|TotalSales=100000|
|TC03|All datasets merged|5 records generated|
|TC04|Duplicate orders check|No duplicates|

---

# Question 2: Employee Salary ETL

## Scenario

An HR system stores employee information. Some employees have missing salary details.

Create an ETL process to clean salary data and calculate employee bonuses.

---

## Input File

### employee.csv

|EmpID|Name|Department|Salary|
|-|-|-|-|
|1|Raj|IT|50000|
|2|John|HR|45000|
|3|Emma|IT||
|4|Chris|Sales|35000|

---

## ETL Requirements

1. Read employee data.
2. Identify missing salary values.
3. Calculate department-wise average salary.
4. Replace missing salaries using department average.
5. Add a bonus column.

Formula:

```

Bonus = Salary × 10%

```

6. Save cleaned employee data.

---

## Expected Output

|Name|Salary|Bonus|
|-|-|-|
|Raj|50000|55000|
|Emma|50000|55000|

---

## Test Cases

|Test ID|Scenario|Expected Result|
|-|-|-|
|TC01|Missing salary|Filled using department average|
|TC02|Bonus calculation|10% bonus added|
|TC03|Row validation|Original row count maintained|

---

# Question 3: Banking Transaction ETL

## Scenario

A bank wants to calculate account balances and identify accounts with negative balances.

---

## Input Data

|Account|Deposit|Withdraw|
|-|-|-|
|1001|5000|1000|
|1002|10000|2000|
|1003|7000|9000|

---

## ETL Requirements

1. Read transaction data.
2. Calculate balance:

```

Balance = Deposit - Withdraw

```

3. Create account status:

Rules:

- Balance >= 0 → OK
- Balance < 0 → Overdrawn

---

## Expected Output

|Account|Balance|Status|
|-|-|-|
|1001|4000|OK|
|1003|-2000|Overdrawn|

---

## Test Cases

|Test ID|Validation|Expected|
|-|-|-|
|TC01|Balance calculation|Deposit - Withdraw|
|TC02|Negative balance detection|Marked Overdrawn|
|TC03|Missing values|No missing records|

---

# Question 4: Hospital Data Cleaning ETL

## Scenario

A hospital database contains incomplete and invalid patient information.

---

## Input Data

|Patient|Age|Gender|
|-|-|-|
|John|35|M|
|Emma||F|
|Raj|150|M|
|Chris|29||

---

## ETL Requirements

1. Load patient data.
2. Calculate average valid age.
3. Replace missing ages with average age.
4. Replace invalid ages (>120) with average age.
5. Replace missing gender with:

```

Unknown

```

---

## Test Cases

|Test ID|Expected Result|
|-|-|
|TC01|Missing age replaced|
|TC02|Invalid age corrected|
|TC03|Missing gender filled|

---

# Question 5: Product Inventory ETL

## Scenario

A warehouse system contains incorrect stock values.

---

## Input Data

|Product|Stock|
|-|-|
|Laptop|10|
|Mouse|-5|
|Keyboard|20|
|Monitor||

---

## ETL Requirements

1. Replace negative stock with 0.
2. Replace missing stock with 0.
3. Create StockStatus column.

Rules:

|Stock Range|Status|
|-|-|
|0|Out of Stock|
|1-10|Low|
|>10|Available|

---

## Test Cases

|Test ID|Expected Result|
|-|-|
|TC01|Negative stock corrected|
|TC02|Missing stock replaced|
|TC03|Stock status generated|

---

# Question 6: Student Marks ETL

## Scenario

A school wants to calculate student performance reports.

---

## Input Data

|Student|Math|Science|
|-|-|-|
|John|80|90|
|Emma|70||
|Raj|100|95|

---

## ETL Requirements

1. Load student marks.
2. Fill missing marks using subject average.
3. Calculate:

```

Total = Math + Science

```

4. Calculate percentage:

```

Percentage = Total / Maximum Marks × 100

```

5. Assign grades.

Example:

|Percentage|Grade|
|-|-|
|90-100|A|
|75-89|B|
|50-74|C|
|<50|D|

---

## Test Cases

|Test ID|Expected Result|
|-|-|
|TC01|Missing marks filled|
|TC02|Total calculated|
|TC03|Grade assigned correctly|

---

# Question 7: API + CSV ETL Pipeline

## Scenario

Product stock information is received from an API while product details exist in CSV format.

---

## API Response

```json
[
 {
  "ProductID":"P101",
  "Stock":20
 },
 {
  "ProductID":"P102",
  "Stock":15
 }
]
```

---

## CSV Data

| ProductID | Product | Price |
| --------- | ------- | ----- |
| P101      | Laptop  | 50000 |
| P102      | Mouse   | 800   |

---

## ETL Requirements

1. Consume API response.
2. Read CSV product data.
3. Convert API response into dataframe.
4. Merge API and CSV datasets.
5. Save final dataset.

---

## Test Cases

| Test ID | Expected Result             |
| ------- | --------------------------- |
| TC01    | API data loaded             |
| TC02    | Dataset merged successfully |
| TC03    | Missing products identified |

---

# Question 8: ELT Pipeline Implementation

## Scenario

Implement an ELT architecture where raw data is stored before transformation.

---

## Requirements

1. Extract three CSV files.
2. Store raw files.
3. Load raw data into staging tables.
4. Perform transformations after loading.
5. Calculate:

```
TotalSales = Quantity × Price
```

6. Generate final dataset.

---

## Test Cases

| Test ID | Expected Result                      |
| ------- | ------------------------------------ |
| TC01    | Raw data stored                      |
| TC02    | Transformation happens after loading |
| TC03    | TotalSales calculated                |
| TC04    | Final CSV created                    |

---

# Question 9: Duplicate Detection ETL

## Input Data

| ID | Name |
| -- | ---- |
| 1  | John |
| 1  | John |
| 2  | Emma |
| 3  | Raj  |

---

## Requirements

1. Detect duplicate records.
2. Count duplicates.
3. Remove duplicate rows.
4. Save cleaned dataset.

---

## Test Cases

| Test ID | Expected Result     |
| ------- | ------------------- |
| TC01    | Duplicate count = 1 |
| TC02    | Final records = 3   |

---

# Question 10: End-to-End Data Engineering Pipeline

## Scenario

Build a complete production-style ETL pipeline using multiple data sources.

---

## Input Sources

* orders.csv
* customers.csv
* products.csv
* payment.json
* shipping.csv

---

## Pipeline Requirements

### Extract

* Read all data sources.
* Validate file availability.
* Validate schema.

### Transform

Perform:

1. Data quality checks.
2. ID validation.
3. Duplicate removal.
4. Missing value handling.
5. Dataset merging.
6. Total sales calculation.

Formula:

```
TotalSales = Quantity × Price
```

7. Generate business summary report.

Report should include:

* Total sales amount
* Number of orders
* Top-selling products
* Sales by city
* Customer purchase summary

### Load

Load final dataset into:

* MySQL OR
* PostgreSQL

---

## Test Cases

| Test ID | Validation            | Expected Result            |
| ------- | --------------------- | -------------------------- |
| TC01    | All files loaded      | Success                    |
| TC02    | Missing customer name | Replaced with Unknown      |
| TC03    | Duplicate orders      | Removed                    |
| TC04    | Missing product price | Flagged for review         |
| TC05    | Sales calculation     | Quantity × Price           |
| TC06    | Output CSV            | Created successfully       |
| TC07    | Database loading      | Rows inserted successfully |
| TC08    | Summary report        | Generated successfully     |

---

# Skills Covered

* CSV Processing
* API Integration
* Data Cleaning
* Data Validation
* Missing Value Handling
* Duplicate Detection
* Data Transformation
* ETL Architecture
* ELT Architecture
* Database Loading
* Data Quality Testing

