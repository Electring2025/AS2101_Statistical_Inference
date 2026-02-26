import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from pathlib import Path


def plot_dual_histogram(csv_file):
    csv_name = Path(csv_file).stem
    output_folder = f"output_{csv_name}"
    Path(output_folder).mkdir(exist_ok=True)

    data = pd.read_csv(csv_file)
    if len(data.columns) != 2:
        print(f"CSV must have exactly 2 columns, found {len(data.columns)}")
        return

    col1, col2 = data.columns
    print(f"Loaded {csv_file}: {len(data)} rows, columns: [{col1}, {col2}]")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.hist(data[col1], bins='auto', color='steelblue', edgecolor='black', alpha=0.7)
    ax1.axvline(data[col1].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean = {data[col1].mean():.3f}')
    ax1.set_xlabel(f'{col1} (minutes)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax1.set_title(f'Histogram of {col1}', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)

    ax2.hist(data[col2], bins='auto', color='coral', edgecolor='black', alpha=0.7)
    ax2.axvline(data[col2].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean = {data[col2].mean():.3f}')
    ax2.set_xlabel(f'{col2} (minutes)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax2.set_title(f'Histogram of {col2}', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    output_file = os.path.join(output_folder, 'dual_histogram.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Dual histogram saved to: {output_file}")
    plt.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dual_histogram.py <csv_file>")
        sys.exit(1)

    plot_dual_histogram(sys.argv[1])

