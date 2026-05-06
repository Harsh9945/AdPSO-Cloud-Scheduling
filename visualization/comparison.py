import matplotlib.pyplot as plt
import numpy as np
import os

COLORS     = {'ldiw': '#2196F3', 'aiw': '#FF9800', 'ldaiw': '#4CAF50'}
LABELS     = {'ldiw': 'LDIW', 'aiw': 'AIW', 'ldaiw': 'LDAIW (Proposed)'}
DATASETS   = ['c_hilo', 'i_hilo', 'c_lohi', 'i_lohi']
STRATEGIES = ['ldiw', 'aiw', 'ldaiw']


def plot_makespan_comparison(results, save_dir='results'):
    fig, axes = plt.subplots(1, 4, figsize=(18, 6), sharey=False)
    fig.suptitle(
        'Makespan Comparison Across Datasets  [lower is better]',
        fontsize=15, fontweight='bold', y=1.02
    )

    x     = np.arange(len(STRATEGIES))
    width = 0.55

    for col, dataset in enumerate(DATASETS):
        ax     = axes[col]
        values = [
            np.mean([r['makespan'] for r in results[dataset][s]])
            for s in STRATEGIES
        ]

        bars = ax.bar(
            x, values, width,
            color=[COLORS[s] for s in STRATEGIES],
            edgecolor='white', linewidth=0.8
        )

        for bar, val in zip(bars, values):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() * 1.01,
                f'{val:,.0f}',
                ha='center', va='bottom', fontsize=8
            )

        ax.set_title(dataset.upper(), fontsize=12, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels([LABELS[s] for s in STRATEGIES], fontsize=9, rotation=10)
        ax.set_ylabel('Makespan (seconds)' if col == 0 else '', fontsize=10)
        ax.grid(axis='y', linestyle='--', alpha=0.4)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{v:,.0f}'))

    handles = [plt.Rectangle((0, 0), 1, 1, color=COLORS[s]) for s in STRATEGIES]
    fig.legend(handles, [LABELS[s] for s in STRATEGIES],
               loc='lower center', ncol=3, fontsize=11,
               bbox_to_anchor=(0.5, -0.08))

    plt.tight_layout()
    os.makedirs(save_dir, exist_ok=True)
    path = os.path.join(save_dir, 'comparison_makespan.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'  Saved: {path}')


def plot_comparison(results, save_dir='results'):
    plot_makespan_comparison(results, save_dir)
