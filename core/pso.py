import numpy as np
from core.particle      import Particle
from core.inertia       import calculate_ldiw, calculate_aiw, calculate_ldaiw
from metrics.calculator import calculate_all


class PSO:

    def __init__(self, etc_matrix, n_tasks, n_vms, strategy='ldaiw',
                 n_particles=20, max_itr=200,
                 w1=0.9, w2=0.4, c1=2.0, c2=1.49455):

        self.etc_matrix  = etc_matrix
        self.n_tasks     = n_tasks
        self.n_vms       = n_vms
        self.strategy    = strategy
        self.n_particles = n_particles
        self.max_itr     = max_itr
        self.w1          = w1
        self.w2          = w2
        self.c1          = c1
        self.c2          = c2

    def _objective(self, mapping):
        m = calculate_all(mapping, self.etc_matrix, self.n_tasks, self.n_vms)
        return m['throughput'] + (1.0 / m['makespan']), m

    def _get_w(self, itr, ps):
        if self.strategy == 'ldiw':
            return calculate_ldiw(self.w1, self.w2, itr, self.max_itr)
        elif self.strategy == 'aiw':
            return calculate_aiw(self.w1, self.w2, ps)
        else:
            return calculate_ldaiw(self.w1, self.w2, ps, itr, self.max_itr)

    def run(self):
        # --- initialise particles ---
        particles = [Particle(self.n_tasks, self.n_vms)
                     for _ in range(self.n_particles)]

        gbest_value    = -np.inf
        gbest_position = None
        gbest_metrics  = None

        # evaluate initial positions
        for p in particles:
            obj, metrics = self._objective(p.get_mapping())
            p.update_pbest(obj)
            if obj > gbest_value:
                gbest_value    = obj
                gbest_position = p.position.copy()
                gbest_metrics  = metrics

        # convergence history — one makespan value per iteration
        history = []
        ps      = 1.0       # success rate starts at 1

        # --- main loop ---
        for itr in range(1, self.max_itr + 1):

            w             = self._get_w(itr, ps)
            improved_count = 0

            for p in particles:
                p.update_velocity(w, self.c1, self.c2, gbest_position)
                p.update_position()

                obj, metrics = self._objective(p.get_mapping())
                p.update_pbest(obj)

                if p.improved:
                    improved_count += 1
                    if obj > gbest_value:
                        gbest_value    = obj
                        gbest_position = p.position.copy()
                        gbest_metrics  = metrics

            # update success rate for next iteration
            ps = improved_count / self.n_particles
            if ps <= 0:
                ps = 1.0

            history.append(gbest_metrics['makespan'])

        # final best mapping
        final_mapping = np.round(gbest_position).astype(int)
        final_mapping = np.clip(final_mapping, 0, self.n_vms - 1)

        return {
            'makespan'   : gbest_metrics['makespan'],
            'throughput' : gbest_metrics['throughput'],
            'arur'       : gbest_metrics['arur'],
            'vm_times'   : gbest_metrics['vm_times'],
            'mapping'    : final_mapping,
            'history'    : history
        }
