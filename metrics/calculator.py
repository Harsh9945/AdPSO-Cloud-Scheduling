import numpy as np

def calculate_makespan(mapping, etc_matrix, n_tasks, n_vms):
    vm_times = np.zeros(n_vms)

    for task_id in range(n_tasks):
        vm_id = int(mapping[task_id])
        vm_times[vm_id] += etc_matrix[task_id][vm_id]

    makespan = np.max(vm_times)
    return makespan, vm_times


def calculate_throughput(n_tasks, makespan):
    if makespan <= 0:
        return 0.0
    return n_tasks / makespan


def calculate_arur(vm_times, makespan):
    if makespan <= 0:
        return 0.0
    return float(np.mean(vm_times / makespan))


def calculate_all(mapping, etc_matrix, n_tasks, n_vms):
    makespan, vm_times = calculate_makespan(mapping, etc_matrix, n_tasks, n_vms)
    throughput         = calculate_throughput(n_tasks, makespan)
    arur               = calculate_arur(vm_times, makespan)

    return {
        'makespan'   : makespan,
        'throughput' : throughput,
        'arur'       : arur,
        'vm_times'   : vm_times
    }
