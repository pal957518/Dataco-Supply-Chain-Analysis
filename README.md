# 🚚 DataCo Smart Supply Chain Analytics

## 1. What is this project?

This project is a **Supply Chain Analytics and Late Delivery Prediction** project.

In simple words, it takes supply-chain order data, cleans it, analyzes sales and profit, predicts late deliveries using Machine Learning, and shows the results in dashboards.

The project uses:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- MySQL
- Power BI

---

# 2. What does the project do?

The complete project works like this:

```text
Raw Supply Chain Data
        ↓
Python Data Cleaning
        ↓
Feature Creation
        ↓
Data Analysis
        ↓
Machine Learning
        ↓
Clean CSV File
        ↓
   ┌────┴────┐
   ↓         ↓
MySQL    Power BI
   ↓         ↓
SQL      Dashboard
Analysis
```

There is also a **Streamlit web application** called `app.py`.

```text
Clean CSV + ML Model
        ↓
      app.py
        ↓
 Streamlit Web App
```

---

# 3. Project Files

Keep the important files in the same project folder.

| File | Simple Explanation |
|---|---|
| `app.py` | Streamlit web application |
| `Supply_Chain_Clean.csv` | Clean supply-chain data |
| `supply_chain_model.pkl` | Saved Machine Learning model |
| `dataco-smart-supply-chain.ipynb` | Main Python notebook |
| `Supply_main.sql` | MySQL database and SQL queries |
| `Supply_p.pbix` | Power BI dashboard |
| `README.md` | Project explanation |

---

# 4. What is the Visual Studio Code?

The notebook:

`dataco-smart-supply-chain.ipynb`

is the main Python workflow.

It performs these steps:

```text
Load Data
   ↓
Understand Data
   ↓
Check Missing Values
   ↓
Check Duplicate Rows
   ↓
Remove Unnecessary Columns
   ↓
Convert Dates
   ↓
Create New Features
   ↓
Exploratory Data Analysis
   ↓
Prepare Data for ML
   ↓
Remove Outliers
   ↓
Encode Data
   ↓
Train ML Models
   ↓
Predict Late Delivery
   ↓
Save Clean CSV
   ↓
Save ML Model
```

The original dataset contains **180,519 rows and 53 columns**.

---

# 5. Data Cleaning

The project removes information that is not needed for the main analysis and prediction.

Examples include:

- Customer email
- Customer name
- Customer password
- Customer street
- Product description
- Product image
- Order IDs
- Customer IDs
- Location fields that are not required

This makes the dataset easier to use.

---

# 6. Date Features

The order date is used to create useful new columns.

The project creates:

- `Order_Year`
- `Order_Month`
- `Order_Day`
- `Order_Weekday`

These columns help us understand how supply-chain activity changes over time.

---

# 7. Profit Margin

The project also calculates profit margin.

The formula is:

```text
Profit Margin Percentage =
(Order Profit Per Order / Sales) × 100
```

This helps us understand how profitable an order is.

---

# 8. Exploratory Data Analysis

The project analyzes different parts of the supply chain.

For example:

### Sales

We can check:

- Sales by year
- Sales by market
- Sales by category
- Sales by product

### Profit

We can check:

- Total profit
- Profit by category
- Most profitable products

### Delivery

We can check:

- Late delivery risk
- Shipping mode
- Order region
- Market
- Year

The target column for late-delivery prediction is:

```text
Late_delivery_risk
```

The project uses:

```text
0 = Not Late
1 = Late
```

---

# 9. Machine Learning

The project uses Machine Learning to predict whether an order is likely to have a late delivery.

The target is:

```text
Late_delivery_risk
```

The model uses these 16 input features:

1. `Shipping Mode`
2. `Customer Segment`
3. `Market`
4. `Order Region`
5. `Category Name`
6. `Department Name`
7. `Order Item Quantity`
8. `Sales`
9. `Order Item Discount`
10. `Order Item Discount Rate`
11. `Product Price`
12. `Order Profit Per Order`
13. `Days for shipment (scheduled)`
14. `Order_Year`
15. `Order_Month`
16. `Order_Weekday`

These are the values used by the prediction application.

---

# 10. Machine Learning Models

The notebook contains three classification models:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

The project saves the Random Forest model as:

```text
supply_chain_model.pkl
```

The model uses:

```text
n_estimators = 100
random_state = 42
```

---

# 11. What is `app.py`?

`app.py` creates a simple website using **Streamlit**.

You do not need to open the Jupyter Notebook every time.

The Streamlit app allows you to:

- View total sales
- View total orders
- View total profit
- View total quantity
- View late delivery percentage
- Filter the data
- View sales charts
- View market performance
- View category profit
- View order status
- View shipping performance
- View customer segment sales
- View top 10 products
- Make a late-delivery prediction
- View detailed supply-chain data

---

# 12. How to Run `app.py`

## Step 1: Open the project folder

Open the project folder in **Visual Studio Code**.

Make sure these files are present:

```text
app.py
Supply_Chain_Clean.csv
supply_chain_model.pkl
```

---

## Step 2: Open the Terminal

In VS Code:

```text
Terminal → New Terminal
```

---

## Step 3: Activate your virtual environment

If your project already has a `.venv`, activate it.

For PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## Step 4: Install required libraries

If the libraries are not installed, run:

```powershell
pip install streamlit pandas numpy plotly joblib scikit-learn
```

---

## Step 5: Start the Streamlit application

Run:

```powershell
streamlit run app.py
```

Streamlit will start the application and open it in your browser.

---

# 13. If Streamlit Does Not Start

First check Streamlit:

```powershell
streamlit --version
```

If it is not installed:

```powershell
pip install streamlit
```

Then run:

```powershell
streamlit run app.py
```

---

# 14. CSV File Error

If you see:

```text
CSV file not found
```

make sure this file exists in the same folder as `app.py`:

```text
Supply_Chain_Clean.csv
```

Correct:

```text
Project Folder
│
├── app.py
└── Supply_Chain_Clean.csv
```

Incorrect:

```text
Project Folder
│
├── app.py
│
└── Data
    └── Supply_Chain_Clean.csv
```

The current `app.py` expects the CSV in the same folder.

---

# 15. Machine Learning Model Error

The application needs the saved model for prediction.

Keep:

```text
supply_chain_model.pkl
```

in the same folder as `app.py`.

The dashboard can still work without the model, but the **Late Delivery Prediction** feature will not work.

---

# 16. Important Note About Prediction Inputs

The prediction section uses **16 values**.

They are shown using their real feature names instead of:

```text
Input 1
Input 2
Input 3
...
```

For example:

```text
Shipping Mode
Customer Segment
Market
Order Region
Category Name
Department Name
...
```

This makes the application easier for another person to understand.

### Important

Some fields such as:

```text
Shipping Mode
Customer Segment
Market
Category Name
Department Name
```

are categorical fields.

The saved model expects their **numeric encoded values**.

Therefore, do not randomly enter numbers for these fields unless you know the encoding used when the model was trained.

---

# 17. Power BI Dashboard

The Power BI file is:

```text
Supply_p.pbix
```

It provides a business dashboard for the cleaned supply-chain data.

The dashboard includes KPIs such as:

- Total Sales
- Total Profit
- Total Orders
- Total Quantity
- Late Delivery Rate

It also contains charts for:

- Sales
- Markets
- Regions
- Shipping Mode
- Order Status
- Products
- Late Delivery

---

# 18. How to Open Power BI

1. Open `Supply_p.pbix`.
2. Open it in Power BI Desktop.
3. If Power BI asks for the CSV location, select:

```text
Supply_Chain_Clean.csv
```

4. Refresh the data.
5. Check the KPI cards and charts.

---

# 19. MySQL Database

The SQL file is:

```text
Supply_main.sql
```

The project creates a database named:

```text
supply_chain
```

and a main table:

```text
orders
```

The database can be used to store and analyze the supply-chain data.

---

# 20. SQL Analysis

The SQL file contains queries for:

### Total Sales

Finds the total sales.

```sql
SUM(sales)
```

### Total Orders

Counts the order records.

```sql
COUNT(*)
```

### Total Profit

Finds total profit.

```sql
SUM(order_profit_per_order)
```

### Late Orders

Counts orders where:

```text
late_delivery_risk = 1
```

### Late Delivery Percentage

Calculates the percentage of orders with late-delivery risk.

### Sales by Market

Shows:

- Orders
- Sales
- Profit

for each market.

### Year-wise Sales

Shows:

- Orders
- Sales
- Profit

for each year.

### Top 10 Profitable Products

Shows the products with the highest total profit.

---

# 21. Recommended Order to Run the Project

If you want to run the entire project from the beginning, follow this order:

```text
1. Raw Dataset
      ↓
2. Jupyter Notebook
      ↓
3. Data Cleaning
      ↓
4. Feature Engineering
      ↓
5. EDA
      ↓
6. Machine Learning
      ↓
7. Create Clean CSV
      ↓
8. Save ML Model
      ↓
9. MySQL
      ↓
10. SQL Analysis
      ↓
11. Power BI
      ↓
12. Streamlit app.py
```

---

# 22. Simple Explanation of Each Technology

| Technology | What it does |
|---|---|
| Python | Main programming language |
| Pandas | Reads and manages data |
| NumPy | Works with numbers |
| Matplotlib | Creates charts |
| Seaborn | Creates data visualizations |
| Scikit-learn | Builds Machine Learning models |
| Joblib | Saves and loads the ML model |
| Streamlit | Creates the web application |
| MySQL | Stores data in a database |
| SQL | Analyzes database data |
| Power BI | Creates an interactive business dashboard |
| Jupyter Notebook | Runs the Python analysis step by step |

---

# 23. Project Output

At the end, the project provides:

### Data Analytics

Clean and useful supply-chain data.

### Machine Learning

A model that predicts late-delivery risk.

### Streamlit Application

An interactive web dashboard.

### MySQL Database

Structured supply-chain data and SQL analysis.

### Power BI Dashboard

A visual business dashboard.

---

# 24. Important File Names

Use these names carefully:

```text
app.py
Supply_Chain_Clean.csv
supply_chain_model.pkl
dataco-smart-supply-chain.ipynb
Supply_main.sql
Supply_p.pbix
README.md
```

File names are important because the application looks for the CSV and ML model in its own folder.

---

# 25. Security Note

Do not upload real database passwords to GitHub or other public websites.

If your MySQL connection contains a password, keep it private.

For a real project, database credentials should be stored using environment variables or another secure configuration method.

---

# 26. Quick Start

If everything is already prepared, the easiest way to start the application is:

```powershell
cd "YOUR_PROJECT_FOLDER"
```

Then:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then:

```powershell
streamlit run app.py
```

That's it.

---

# 27. Final Project Summary

This project is an **end-to-end Supply Chain Analytics project**.

It combines:

```text
Python
  +
Data Cleaning
  +
Data Analysis
  +
Machine Learning
  +
MySQL
  +
SQL
  +
Power BI
  +
Streamlit
```

The main goal is to understand supply-chain performance and use Machine Learning to predict **late delivery risk**.

The project can be understood in one simple flow:

```text
DATA
 ↓
CLEAN
 ↓
ANALYZE
 ↓
PREDICT
 ↓
STORE
 ↓
VISUALIZE
```

**DataCo Smart Supply Chain Analytics**
