import numpy as np


class Particle:

    def __init__(self, n_tasks, n_vms):
        self.n_tasks = n_tasks
        self.n_vms   = n_vms

        # position: float array, each value in [0, n_vms-1]
        # represents which VM each task is assigned to
        self.position = np.random.uniform(0, n_vms - 1, n_tasks)

        # velocity: float array
        self.velocity = np.random.uniform(0, 1, n_tasks)

        # personal best
        self.pbest_position = self.position.copy()
        self.pbest_value    = -np.inf       # we are MAXIMIZING objective

        # track if this particle improved this iteration
        self.improved = False

    def get_mapping(self):
        # convert float positions → integer VM indices
        mapping = np.round(self.position).astype(int)
        mapping = np.clip(mapping, 0, self.n_vms - 1)
        return mapping

    def update_velocity(self, w, c1, c2, gbest_position):
        r1 = np.random.random(self.n_tasks)
        r2 = np.random.random(self.n_tasks)

        self.velocity = (
            w  * self.velocity +
            c1 * r1 * (self.pbest_position - self.position) +
            c2 * r2 * (gbest_position      - self.position)
        )

    def update_position(self):
        self.position = self.position + self.velocity

        # if any position goes out of bounds → assign random valid VM
        out_of_bounds = (self.position < 0) | (self.position >= self.n_vms)
        self.position[out_of_bounds] = np.random.uniform(
            0, self.n_vms - 1, np.sum(out_of_bounds)
        )

    def update_pbest(self, current_value):
        self.improved = False
        if current_value > self.pbest_value:
            self.pbest_value    = current_value
            self.pbest_position = self.position.copy()
            self.improved       = True
