# Day 314 => PySpark Basics 

## Project Overview
This project demonstrates the basic usage of **PySpark** for handling large datasets in a scalable way.  
It covers:
- Loading and reading data
- Basic DataFrame operations
- SQL queries with Spark
- Data cleaning and transformations
- Saving results in CSV and Parquet formats
- Optional basic ML using Spark MLlib

The goal is to provide a hands-on foundation for **Big Data processing using PySpark**.

---

## Dataset
- Sample dataset used: `data.csv`  
- Columns example:
  - `name` (string)
  - `age` (integer)
  - `experience` (integer)
  - `department` (string)
  - `salary` (float)

> You can replace this dataset with any large CSV to scale this project.

---

## Setup Instructions

### 1. Install PySpark
```bash
pip install pyspark
````

### 2. Run the Notebook

* Open `PySpark_Basics.ipynb` in Jupyter Notebook or VSCode.
* Execute all cells sequentially.

---

## Project Steps / Features

1. **SparkSession Creation**

   * Entry point for all PySpark applications.

2. **Load Data**

   * Read CSV with header and schema inference.

3. **DataFrame Operations**

   * Select, filter, groupBy, sort
   * Add new columns
   * Handle missing values

4. **Spark SQL**

   * Run SQL queries on PySpark DataFrames

5. **Data Export**

   * Save cleaned dataset in CSV or Parquet format

6. **MLlib (Optional)**

   * Build simple Linear Regression model
   * Train and predict on dataset

---

## Key Concepts Learned

* Distributed computing mindset
* Lazy execution in PySpark
* Efficient handling of large datasets
* Combining SQL and Python for analytics
* Basic machine learning pipeline in Spark

---

## Future Improvements / Next Steps

* Handle larger datasets (>GBs) using Spark clusters
* Stream processing using **Spark Streaming + Kafka**
* Build production-level ETL pipelines
* Implement advanced ML algorithms (Random Forest, Gradient Boosting)
* Connect with cloud storage (AWS S3 / GCP BigQuery)

---

## References

* [PySpark Official Documentation](https://spark.apache.org/docs/latest/api/python/)
* [PySpark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
* [PySpark MLlib Guide](https://spark.apache.org/docs/latest/ml-guide.html)

