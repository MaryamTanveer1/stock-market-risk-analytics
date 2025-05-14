# 📊 Stock Market Risk Analytics Pipeline (Python + AWS)

This project is an **data pipeline** built to analyze stock market performance and risk. It uses **Python**, **AWS S3**, **AWS Athena**, and **AWS Lambda** to process, analyze, and visualize the performance of various tech stocks.

### 🚀 Project Flow

The flow of this pipeline includes multiple stages:

1. **Data Ingestion**: 
    - Data is **extracted** using the `yfinance` API for selected stock tickers (e.g., AAPL, MSFT, GOOGL, etc.).
    - The raw stock data is **cleaned**, processed, and then **uploaded** to an S3 bucket for further analysis.

2. **Data Processing & Transformation**: 
    - After uploading, the cleaned data is **transformed** using SQL queries in **AWS Athena**, where tables are created for easier access.
    - Key financial metrics such as **daily returns**, **volatility**, **moving averages**, and **Sharpe ratio** are **calculated** in Python using Pandas and NumPy.

3. **Analysis**:
    - The transformed data is **analyzed**, visualized, and stored as a final CSV file.
    - **AWS Lambda** is used to automate parts of the workflow, uploading the final analysis back to the S3 bucket.

4. **Data Retrieval**:
    - The data stored in S3 is **retrieved** using Athena queries to visualize and compare stock performance.

5. **Final Visualizations**:
    - Visualizations are **generated** for stock prices, moving averages, daily returns, and other computed metrics, and saved as images.
    - These graphs help in understanding stock behavior and risk analysis.

---

## 💡 Key Features

- **Stock Performance Analysis**: Analyze stock prices, daily returns, moving averages, and volatility.
- **Risk Metrics**: Calculate risk metrics like **Sharpe Ratio** and **Volatility** to evaluate stock performance.
- **Automation**: Use **AWS Lambda** to automate parts of the pipeline, such as uploading results to S3.

---
## 📊 Computation Graphs

### 🔹 **AAPL Closing Price Over Time**
This graph shows the **closing price** of AAPL stock over time.

![AAPL Closing Price](images/AAPL%20Closing%20Price.png)

---

### 🔹 **Stock Price Comparison**
This graph compares the **closing prices** of different stocks (AAPL, MSFT, GOOGL, etc.) over time.

![Stock Price Comparison](images/Stock%20Price%20Comparison.png)

---

### 🔹 **Daily & Cumulative Return**
The **Daily Returns** show the percentage change in stock prices from one day to the next, while the **Cumulative Return** shows the compounded growth over time.

![Daily & Cumulative Return](images/Daily%20&%20Cumulative%20Return.png)

---

### 🔹 **Daily Returns**
This graph shows the **daily returns** for a stock, reflecting the percentage change in its price each day.

![Daily Returns](images/Daily%20Returns.png)

---

### 🔹 **Moving Averages (50-day and 200-day)**
This graph shows the **50-day** and **200-day moving averages** alongside the stock’s closing price.

![Moving Averages](images/Moving_Averages.png)

---

### 🔹 **Stock Closing Price**
This graph shows the **closing price** of a stock (can be AAPL, MSFT, or others) over time.

![Stock Closing Price](images/Stock%20Closing%20Price.png)



## 🧑‍💻 AWS Services Used

- **S3 (Storage)**: All raw and processed data files are uploaded to AWS S3 buckets for secure storage.
- **Athena (Data Querying)**: Data stored in S3 is queried using **AWS Athena** with SQL to create tables and retrieve relevant stock information.
- **Lambda (Automation)**: AWS Lambda automates the process of uploading the final results to S3.

---

## 🏗️ Architecture Overview

The architecture below illustrates the flow of data from **Yahoo Finance** to the final **stock market risk analysis** stored on AWS.

![Architecture](images/architecture.png)

---

## 🌍 How It Works

1. **Data Ingestion**:  
    - Stock data is **downloaded** using the `yfinance` API for a list of stock tickers. 
    - Raw data is cleaned and **uploaded** to AWS S3, stored in the `raw` and `processed` folders.

2. **Data Processing with Athena**:
    - The cleaned data stored in S3 is **retrieved** using **AWS Athena**.  
    - An **Athena query** is executed to transform and create an external table on the stock data.

3. **Analysis & Computation**:
    - The processed data is **analyzed** in Python to calculate key metrics like **daily returns**, **moving averages**, **volatility**, and **Sharpe ratio**.
    - Computed values are then **visualized** and saved as PNG images for each metric (closing prices, returns, moving averages, etc.).

4. **Automation with Lambda**:
    - AWS Lambda is used to **automate the upload** of final results (such as CSVs or processed metrics) to the S3 bucket, streamlining the workflow.

5. **Final Outputs**:
    - The final results are **downloaded** and can be analyzed further or visualized, providing a comprehensive analysis of the stock data.

---

## 📝 Conclusion

This pipeline automates stock market data collection, analysis, and visualization, while using AWS services (S3, Athena, Lambda) to store, transform, and manage the data. The project can be extended to handle more complex datasets, additional stocks, or other financial metrics.


