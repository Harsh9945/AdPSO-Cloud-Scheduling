import sys
import io
import numpy as np
from tabulate                    import tabulate
from data.tasks_vms              import get_dataset
from core.pso                    import PSO
from visualization.convergence   import plot_convergence
from visualization.comparison    import plot_comparison
from visualization.gantt         import plot_gantt

# fix windows terminal encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

STRATEGIES = ['ldiw', 'aiw', 'ldaiw']
DATASETS   = ['c_hilo', 'i_hilo', 'c_lohi', 'i_lohi']
N_TRIALS   = 5


def run_all():
    results   = {d: {s: [] for s in STRATEGIES} for d in DATASETS}
    histories = {d: {s: [] for s in STRATEGIES} for d in DATASETS}

    for dataset in DATASETS:
        print(f"\nLoading dataset : {dataset}")
        d          = get_dataset(dataset)
        etc_matrix = d['etc_matrix']
        n_tasks    = d['n_tasks']
        n_vms      = d['n_vms']
        print(f"  Tasks : {n_tasks}  |  VMs : {n_vms}")

        for strategy in STRATEGIES:
            print(f"  Running {strategy.upper()} ({N_TRIALS} trials)...", end='', flush=True)

            for trial in range(N_TRIALS):
                np.random.seed(trial * 7)
                pso = PSO(etc_matrix, n_tasks, n_vms, strategy=strategy)
                r   = pso.run()
                results[dataset][strategy].append(r)

            best   = min(results[dataset][strategy], key=lambda r: r['makespan'])
            histories[dataset][strategy] = best['history']
            avg_ms = np.mean([r['makespan'] for r in results[dataset][strategy]])
            print(f" done.  Avg Makespan : {avg_ms:,.0f}")

    return results, histories


def print_summary(results):
    print("\n" + "="*72)
    print("RESULTS SUMMARY  -  Average over 5 trials")
    print("="*72)

    for dataset in DATASETS:
        print(f"\nDataset : {dataset.upper()}")
        table    = []
        ldiw_ms  = np.mean([r['makespan'] for r in results[dataset]['ldiw']])

        for strategy in STRATEGIES:
            trials   = results[dataset][strategy]
            avg_ms   = np.mean([r['makespan']   for r in trials])
            avg_tp   = np.mean([r['throughput'] for r in trials])
            avg_arur = np.mean([r['arur']       for r in trials])
            vs_ldiw  = ((ldiw_ms - avg_ms) / ldiw_ms) * 100

            table.append([
                strategy.upper(),
                f"{avg_ms:>15,.2f}",
                f"{avg_tp:.6f}",
                f"{avg_arur:.4f}",
                f"{vs_ldiw:+.2f}%"
            ])

        print(tabulate(
            table,
            headers=['Strategy', 'Makespan (s)', 'Throughput', 'ARUR', 'vs LDIW'],
            tablefmt='grid'
        ))


if __name__ == '__main__':
    print("AdPSO - Adaptive PSO Task Scheduling")
    print("="*72)
    print(f"Strategies : {', '.join(s.upper() for s in STRATEGIES)}")
    print(f"Datasets   : {', '.join(DATASETS)}")
    print(f"Trials     : {N_TRIALS} per strategy per dataset")
    print(f"Particles  : 20  |  Iterations : 200")

    results, histories = run_all()
    print_summary(results)

    print("\n" + "="*72)
    print("Generating Visualizations...")
    print("="*72)

    print("\n[1] Convergence graph (i_lohi dataset):")
    plot_convergence(histories['i_lohi'], 'i_lohi')

    print("\n[2] Makespan comparison (all 4 datasets):")
    plot_comparison(results)

    print("\n[3] Gantt chart (LDAIW best trial on i_hilo):")
    d_hilo  = get_dataset('i_hilo')
    best_hilo = min(results['i_hilo']['ldaiw'], key=lambda r: r['makespan'])
    plot_gantt(
        best_hilo['mapping'], d_hilo['etc_matrix'], d_hilo['n_tasks'], d_hilo['n_vms'],
        'Gantt Chart - LDAIW (Proposed) - I_HILO',
        'results/gantt_ldaiw_i_hilo.png'
    )

    print("\n[4] Gantt chart (LDAIW best trial on i_lohi):")
    d_lohi  = get_dataset('i_lohi')
    best_lohi = min(results['i_lohi']['ldaiw'], key=lambda r: r['makespan'])
    plot_gantt(
        best_lohi['mapping'], d_lohi['etc_matrix'], d_lohi['n_tasks'], d_lohi['n_vms'],
        'Gantt Chart - LDAIW (Proposed) - I_LOHI',
        'results/gantt_ldaiw_i_lohi.png'
    )

    print("\nAll visualizations saved to results/ folder.")
    print("Done.")
