import pandas as pd
import matplotlib.pyplot as plt
import os

csv_file = '../data/execution_times.csv'
graph_dir = '../data/graphs'
os.makedirs(graph_dir, exist_ok=True)

df = pd.read_csv(csv_file, sep=';')
df['Time(ms)'] = df['Time(ms)'].str.replace(',', '.').astype(float)
df.rename(columns={'Time(ms)': 'Time_ms'}, inplace=True)

mean_20k = df[df['Size'] == 20000].groupby('Algorithm')['Time_ms'].mean().reset_index()
mean_20k.to_csv(os.path.join(graph_dir, 'mean_times_20000.csv'), index=False)
print("Tabela de médias salva em 'mean_times_20000.csv'")

df_filtered = df[(df['Size'] >= 1000) & (df['Size'] <= 20000)]

algorithms = df_filtered['Algorithm'].unique()

for algorithm in algorithms:
    algo_df = df_filtered[df_filtered['Algorithm'] == algorithm]

    algo_df = algo_df.groupby('Size')['Time_ms'].mean().reset_index()

    plt.figure(figsize=(8, 5))
    plt.plot(algo_df['Size'], algo_df['Time_ms'], marker='o', color='teal')
    plt.title(f'{algorithm} Execution Time')
    plt.xlabel('Array Size')
    plt.ylabel('Time (ms)')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(os.path.join(graph_dir, f'{algorithm}_execution_time.png'))
    plt.close()

pivot_df = df_filtered.groupby(['Size', 'Algorithm'])['Time_ms'].mean().unstack()

plt.figure(figsize=(10, 6))
for algorithm in pivot_df.columns:
    plt.plot(pivot_df.index, pivot_df[algorithm], marker='o', label=algorithm)

plt.title('Execution Time Comparison (1000 to 20000)')
plt.xlabel('Array Size')
plt.ylabel('Time (ms)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(graph_dir, 'all_algorithms_filtered.png'))
plt.show()