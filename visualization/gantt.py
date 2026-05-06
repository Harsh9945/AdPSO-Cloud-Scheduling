import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os


def plot_gantt(mapping, etc_matrix, n_tasks, n_vms, title, save_path):
    # build timeline for each VM
    vm_timelines = [[] for _ in range(n_vms)]
    vm_ready     = np.zeros(n_vms)

    for task_id in range(n_tasks):
        vm_id    = int(mapping[task_id])
        duration = etc_matrix[task_id][vm_id]
        start    = vm_ready[vm_id]
        end      = start + duration
        vm_timelines[vm_id].append((task_id, start, duration))
        vm_ready[vm_id] = end

    # only show VMs that have at least one task
    active_vms = [v for v in range(n_vms) if len(vm_timelines[v]) > 0]

    fig, ax = plt.subplots(figsize=(14, max(6, len(active_vms) * 0.5)))
    cmap    = plt.cm.get_cmap('tab20', n_tasks)

    for row, vm_id in enumerate(active_vms):
        for (task_id, start, duration) in vm_timelines[vm_id]:
            ax.barh(
                row, duration, left=start, height=0.6,
                color=cmap(task_id % 20), edgecolor='white', linewidth=0.3
            )

    makespan = np.max(vm_ready[active_vms])
    ax.axvline(makespan, color='red', linestyle='--', linewidth=1.5, label=f'Makespan = {makespan:,.0f}s')

    ax.set_yticks(range(len(active_vms)))
    ax.set_yticklabels([f'VM{v}' for v in active_vms], fontsize=8)
    ax.set_xlabel('Time (seconds)', fontsize=11)
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(axis='x', linestyle='--', alpha=0.4)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))

    plt.tight_layout()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f'  Saved: {save_path}')


def plot_gantt_comparison(results, etc_matrix, n_tasks, n_vms, dataset_name, save_dir='results'):
    strategies = ['ldiw', 'aiw', 'ldaiw']
    labels     = {'ldiw': 'LDIW', 'aiw': 'AIW', 'ldaiw': 'LDAIW (Proposed)'}

    for strategy in strategies:
        best    = min(results[dataset_name][strategy], key=lambda r: r['makespan'])
        mapping = best['mapping']
        title   = f'Gantt Chart — {labels[strategy]} — {dataset_name.upper()}'
        path    = os.path.join(save_dir, f'gantt_{dataset_name}_{strategy}.png')
        plot_gantt(mapping, etc_matrix, n_tasks, n_vms, title, path)
