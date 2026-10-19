# Swiggy Replica: End-to-End Consumer Analytics & ML Pipeline

## Overview
This project simulates the core data infrastructure of a consumer logistics and food delivery platform like Swiggy. It features an end-to-end pipeline that handles synthetic data generation, relational database analytics, and a machine learning recommendation engine.

## Tech Stack
* **Languages:** Python, SQL
* **Libraries:** Pandas, Scikit-Learn
* **Database:** SQLite
* **Concepts:** ETL pipelines, Relational Schemas, Business Intelligence, Collaborative Filtering

## Pipeline Architecture

### 1. Data Engineering (ETL)
* `data_generator.py`: Generates thousands of rows of synthetic transactional data (Users, Restaurants, Orders) to simulate high-volume platform traffic.

### 2. Data Analytics (SQL)
* `database_analytics.py`: Automates the ingestion of raw CSV data into a relational SQLite database. Executes business intelligence queries to track key performance indicators, including top-grossing cuisines and delivery bottleneck identification.

### 3. Machine Learning (Recommendation Engine)
* `recommendation_engine.py`: Implements a User-Item Collaborative Filtering algorithm using Cosine Similarity to suggest new restaurants to users based on historical purchasing patterns, increasing simulated cross-sell opportunities.

## How to Run
1. Run `data_generator.py` to create the raw `.csv` files.
2. Run `database_analytics.py` to build the `swiggy.db` SQL database and view business metrics.
3. Run `recommendation_engine.py` to output algorithmic restaurant suggestions for target users.
