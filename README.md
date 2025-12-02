# Spark Performance Analysis: Sequential vs. Distributed (RDD & SQL)

## Project Overview
This project evaluates the performance of Apache Spark by comparing three different implementations of a data analysis application. The study focuses on how execution time varies according to input data size, contrasting a sequential approach against distributed processing methods.

This work was conducted as part of the "Parallelism and Distributed Systems" course at the **Universitat Politècnica de Catalunya (UPC)**.

## Infrastructure
The experiments were executed on a distributed cluster hosted on **AWS EC2**, consisting of:
*   **Cluster Size:** 4 instances (1 Master, 3 Workers).
*   **Instance Type:** `m5.large` (Ubuntu Linux, 30GB Storage).
*   **Configuration:** Custom security groups for SSH and Spark internal communication.

## Application Logic
The application processes a dataset derived from the **IMDB database** (`infoActors.csv`).
*   **Goal:** Identify and analyze collaborations between Actors and Directors.
*   **Metrics:** For the top 20 most frequent collaborations, the system calculates:
    *   Total number of shared movies.
    *   Average rating of these movies.
    *   Minimum and Maximum ratings.

## Implementations
Three versions of the application were developed and benchmarked:
1.  **Sequential Python:** A baseline script using standard Python (`csv` and dictionaries).
2.  **Spark RDD:** A distributed implementation using the PySpark Core (RDD) API.
3.  **Spark SQL:** A distributed implementation using the PySpark DataFrames API.

## Methodology & Evaluation
*   **Dataset:** The input CSV file was concatenated multiple times to generate datasets of increasing sizes (1x, 2x, 4x, etc.).
*   **Benchmarking:** Execution time was measured using the Linux `time` command (elapsed time).
*   **Analysis:** The project analyzes the trade-off between the overhead of distributed computing for small files versus the scalability benefits observed with larger datasets.
