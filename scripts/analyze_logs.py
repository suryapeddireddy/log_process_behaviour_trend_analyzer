import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


def isolate_execution_anomalies():
    print("Starting array-based log analysis pipeline...")
    raw_path = "data/raw/unstructured_system_logs.csv"
    processed_dir = "data/processed"

    if not os.path.exists(raw_path):
        print(f"Error: {raw_path} not found. Run generate_system_logs.py first!")
        return

    # 1. Load data stream
    df = pd.read_csv(raw_path)
    print(f"Loaded {len(df)} transaction logs.")

    # 2. Extract metrics into high-performance NumPy arrays
    response_times = df["Response_Time_MS"].to_numpy()
    status_flags = df["Status_Flag"].to_numpy()
    components = df["Component"].to_numpy()

    # 3. Vectorized anomaly tracking (Find values > 1500ms or explicitly marked FAIL)
    print("Executing lightning-fast vectorized query filtering...")
    anomaly_mask = (response_times > 1500) | (status_flags == "FAIL")

    # Isolate data anomalies using Boolean indexing arrays
    anomaly_times = response_times[anomaly_mask]
    anomaly_components = components[anomaly_mask]

    total_anomalies = np.sum(anomaly_mask)
    anomaly_percentage = (total_anomalies / len(response_times)) * 100
    print(
        f"Detected {total_anomalies} anomalies ({anomaly_percentage:.2f}% of total traffic)."
    )

    # 4. Map failures to components using unique vector counts
    unique_comps, counts = np.unique(anomaly_components, return_counts=True)
    component_breakdown = dict(zip(unique_comps, counts))

    print("\n--- Anomaly Counts By Backend Component ---")
    for comp, count in component_breakdown.items():
        print(f" Component: {comp:<16} | Failure Count: {count}")

    # 5. Export clean analysis matrices for Excel verification check sheets
    df_anomalies = df[anomaly_mask]
    os.makedirs(processed_dir, exist_ok=True)
    out_path = os.path.join(processed_dir, "isolated_anomalies.csv")
    df_anomalies.to_csv(out_path, index=False)
    print(f"\nSaved structured data verification anomalies sheet to: {out_path}")

    # 6. Generate visual charting models using Seaborn
    print("Plotting distribution graphs...")
    plt.figure(figsize=(10, 6))
    sns.histplot(anomaly_times, bins=30, kde=True, color="crimson")
    plt.title(
        "Statistical Distribution of System Execution Anomalies", fontsize=14, pad=15
    )
    plt.xlabel("Server Latency Response Duration (MS)", fontsize=12)
    plt.ylabel("Incident Frequency Count", fontsize=12)

    os.makedirs("reports", exist_ok=True)
    plt.savefig(
        "reports/anomaly_latency_distribution.png", dpi=300, bbox_inches="tight"
    )
    plt.close()
    print(
        "Operational data visualization generated successfully inside reports/ folder."
    )


if __name__ == "__main__":
    isolate_execution_anomalies()
