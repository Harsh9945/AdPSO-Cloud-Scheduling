import numpy as np
import os

def load_hcsp(filepath):
    with open(filepath, 'r') as f:
        lines = f.read().strip().split('\n')

    first_line = lines[0].split()
    n_tasks    = int(first_line[0])
    n_vms      = int(first_line[1])
    cons_type  = int(first_line[2])

    values = [float(lines[i]) for i in range(1, len(lines))]

    etc_matrix = np.array(values).reshape(n_tasks, n_vms)

    return {
        'etc_matrix' : etc_matrix,
        'n_tasks'    : n_tasks,
        'n_vms'      : n_vms,
        'cons_type'  : cons_type,
        'filename'   : os.path.basename(filepath)
    }
