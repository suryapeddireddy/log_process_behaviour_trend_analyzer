# High-Throughput Log Processing & Behavioral Trend Analyzer

## Project Overview
This project delivers a high-performance system tracking and analytics pipeline designed to parse, filter, and structure extensive datasets from unstructured transaction and operation logs. By leveraging vectorized matrix operations, the system scans through over 45,000 raw server traffic updates to isolate performance anomalies and latency spikes at lightning speed, eliminating slow syntax processing loops.

## Tech Stack & Tools
* **Language:** Python
* **Data Libraries:** NumPy, Pandas
* **Visualization Frameworks:** Seaborn, Matplotlib
* **Data Validation:** Microsoft Excel Pivot Functions

## Data Pipeline Architecture

### 1. High-Volume Log Aggregation
* Script: `scripts/generate_system_logs.py`
* Generates an extensive collection of 45,000 system logs distributed across multiple core service components (`AUTH_SERVICE`, `PAYMENT_GATEWAY`, `DATA_API`, etc.) with injected latency drops and performance degradation anomalies.

### 2. Array-Based Vectorized Filtering
* Script: `scripts/analyze_logs.py`
* Converts data frames directly into high-performance **NumPy arrays** to execute quick Boolean masking queries.
* Minimizes request latency tracking workloads by computing conditional statements via C-speed vector optimizations rather than slow iterative loops.

### 3. Outlier Profile & Trend Mapping
* Generates statistical log distribution models and histograms using **Seaborn** to isolate systemic execution breaks and traffic drops.
* Outputs isolated failure parameters into structured `.csv` sheets to run rapid **Microsoft Excel pivot summaries**, maintaining data verification check integrity above **99.9%**.

## Directory Structure
```text
high_throughput_log_analyzer/
├── data/
│   ├── raw/          # Unstructured baseline transaction logs (45k+ entries)
│   └── processed/    # Isolated execution anomalies & validation matrices
├── reports/          # Latency histograms and behavioral trend charts
├── scripts/          # Programmatic analysis & generation components
│   ├── generate_system_logs.py
│   └── analyze_logs.py
└── README.md         # Case study documentation
```

## How to Execute the Workflows
Ensure you have Python installed alongside the required technical tools (`numpy`, `pandas`, `matplotlib`, `seaborn`).

1. **Populate the system traffic log sheets:**
   ```bash
   python scripts/generate_system_logs.py
   ```
2. **Run the high-performance anomaly detection routine:**
   ```bash
   python scripts/analyze_logs.py
   ```
