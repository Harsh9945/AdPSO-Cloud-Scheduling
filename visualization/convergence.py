import matplotlib.pyplot as plt
import os

COLORS = {'ldiw': '#2196F3', 'aiw': '#FF9800', 'ldaiw': '#4CAF50'}
LABELS = {'ldiw': 'LDIW', 'aiw': 'AIW', 'ldaiw': 'LDAIW (Proposed)'}


def plot_convergence(histories, dataset_name, save_dir='results'):
    fig, ax = plt.subplots(figsize=(10, 6))

    for strategy, history in histories.items():
        ax.plot(
            range(1, len(history) + 1),
            history,
            label=LABELS[strategy],
            color=COLORS[strategy],
            linewidth=2
        )

    ax.set_title(f'Convergence Comparison — {dataset_name.upper()}', fontsize=14, fontweight='bold')
    ax.set_xlabel('Iteration', fontsize=12)
    ax.set_ylabel('Makespan (seconds)', fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))

    plt.tight_layout()
    os.makedirs(save_dir, exist_ok=True)
    path = os.path.join(save_dir, f'convergence_{dataset_name}.png')
    plt.savefig(path, dpi=150)
    plt.close()
    print(f'  Saved: {path}')
