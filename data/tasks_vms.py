import os
from data.loader import load_hcsp

DATASET_DIR = os.path.join(os.path.dirname(__file__), 'datasets')

INSTANCES = {
    'c_hilo' : 'A.u_c_hilo',
    'i_hilo' : 'A.u_i_hilo',
    'c_lohi' : 'A.u_c_lohi',
    'i_lohi' : 'A.u_i_lohi',
}

def get_dataset(instance_name):
    if instance_name not in INSTANCES:
        raise ValueError(f"Unknown instance '{instance_name}'. Choose from: {list(INSTANCES.keys())}")

    filepath = os.path.join(DATASET_DIR, INSTANCES[instance_name])
    data     = load_hcsp(filepath)

    return data
