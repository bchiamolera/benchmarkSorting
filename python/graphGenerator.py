import pandas as pd
import matplotlib.pyplot as plt
import os

csv_file = '../data/execution_times.csv'
graph_dir = '../data/graphs'
os.makedirs(graph_dir, exist_ok=True)

df = pd.read_csv(csv_file, sep=';')

df['Time(ms)'] = df['Time(ms)'].str.replace(',', '.').astype(float)

df.rename(columns={'Time(ms)': 'Time_ms'}, inplace=True)

algorithms = df['Algorithm'].unique()

for algorithm in algorithms:
    algo_df = df[df['Algorithm'] == algorithm]

    plt.figure(figsize=(8, 5))
    plt.plot(algo_df['Size'], algo_df['Time_ms'], marker='o', color='teal')
    plt.title(f'{algorithm} Execution Time')
    plt.xlabel('Array Size')
    plt.ylabel('Time (ms)')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(os.path.join(graph_dir, f'{algorithm}_execution_time.png'))
    plt.close()

pivot_df = df.pivot(index='Size', columns='Algorithm', values='Time_ms')

plt.figure(figsize=(10, 6))
for algorithm in pivot_df.columns:
    plt.plot(pivot_df.index, pivot_df[algorithm], marker='o', label=algorithm)

plt.title('Execution Time Comparison - All Algorithms')
plt.xlabel('Array Size')
plt.ylabel('Time (ms)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(graph_dir, 'all_algorithms.png'))
plt.show()