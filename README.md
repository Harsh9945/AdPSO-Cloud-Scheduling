# AdPSO: Adaptive PSO-Based Task Scheduling for Cloud Computing

## Overview

This project implements the research paper:

**“AdPSO: Adaptive PSO-Based Task Scheduling Approach for Cloud Computing”**

The project focuses on optimizing cloud task scheduling using **Particle Swarm Optimization (PSO)** with a proposed adaptive inertia weight strategy called:

# LDAIW (Linearly Descending Adaptive Inertia Weight)

The implementation aims to:

* Minimize Makespan
* Maximize Throughput
* Improve Average Resource Utilization Ratio (ARUR)
* Balance workload among Virtual Machines (VMs)

---

# Research Motivation

In cloud computing, thousands of tasks must be assigned efficiently to Virtual Machines.

Poor scheduling causes:

* High execution time
* VM overload
* Low throughput
* Resource wastage

Since task scheduling is an NP-Hard optimization problem, traditional brute-force methods are impractical.

This project uses swarm intelligence and metaheuristic optimization to solve the scheduling problem efficiently.

---

# Key Features

* Particle Swarm Optimization (PSO)
* Adaptive inertia weight strategies
* HCSP benchmark dataset support
* Makespan optimization
* Throughput maximization
* ARUR improvement
* Convergence analysis
* Gantt chart generation
* Comparative visualization

---

# Implemented Inertia Weight Strategies

| Strategy | Description                        |
| -------- | ---------------------------------- |
| LDIW     | Linearly Descending Inertia Weight |
| AIW      | Adaptive Inertia Weight            |
| LDAIW    | Proposed hybrid adaptive strategy  |

---

# Core Concepts

## Particle Swarm Optimization (PSO)

Each particle represents a complete task-to-VM scheduling solution.

The swarm searches for the best scheduling configuration using:

* Personal Best (pBest)
* Global Best (gBest)
* Velocity updates
* Position updates

---

## Exploration vs Exploitation

### Exploration

Search globally across the solution space.

### Exploitation

Fine-tune near promising solutions.

The proposed LDAIW strategy balances both effectively.

---

# Objective Function

The project optimizes:

Objective = Throughput + (1 / Makespan)

Where:

* Makespan = Total execution completion time
* Throughput = Tasks completed per second
* ARUR = Average Resource Utilization Ratio

---

# Dataset

The project uses the HCSP (Heterogeneous Computing Scheduling Problem) benchmark dataset.

Dataset variants:

* c_hilo
* i_hilo
* c_lohi
* i_lohi

Each dataset contains:

* 1024 tasks
* 32 Virtual Machines

The ETC (Expected Time to Compute) matrix defines execution time of each task on each VM.

---

# Project Structure

```bash
AdPSO/
│
├── data/
│   └── datasets/
│
├── metrics/
│
├── results/
│   ├── convergence graphs
│   ├── comparison graphs
│   └── gantt charts
│
├── visualization/
│
├── inertia.py
├── loader.py
├── tasks_vms.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Module Description

| File           | Description                |
| -------------- | -------------------------- |
| main.py        | Main execution script      |
| inertia.py     | Inertia weight strategies  |
| loader.py      | Dataset loading            |
| tasks_vms.py   | Task and VM handling       |
| metrics/       | Makespan, Throughput, ARUR |
| visualization/ | Graph and chart generation |

---

# PSO Velocity Equation

The core PSO update equation is:

v(t+1) = w*v(t) + c1*r1*(pbest-x) + c2*r2*(gbest-x)

Where:

* w = inertia weight
* c1 = cognitive coefficient
* c2 = social coefficient
* r1, r2 = random values

---

# Proposed LDAIW Strategy

LDAIW combines:

* Linear decreasing behavior from LDIW
* Adaptive feedback from AIW

Advantages:

* Better exploration in early iterations
* Adaptive behavior when particles get stuck
* Stable convergence in later iterations
* Reduced local optimum trapping

---

# Experimental Setup

| Parameter  | Value   |
| ---------- | ------- |
| Particles  | 20      |
| Iterations | 200     |
| Tasks      | 1024    |
| VMs        | 32      |
| w1         | 0.9     |
| w2         | 0.4     |
| c1         | 2       |
| c2         | 1.49455 |

---

# Results

The proposed AdPSO approach achieved:

* Lower Makespan
* Higher Throughput
* Better ARUR

Compared against:

* Traditional PSO
* LDIW
* AIW
* APSO
* PSO-BOOST
* Hyper-Heuristic approaches

### Improvements Reported

* Up to 10% lower makespan
* Up to 12% higher throughput
* Up to 60% better resource utilization

---

# Generated Outputs

The project generates:

* Makespan comparison graphs
* Throughput comparison graphs
* ARUR comparison graphs
* Convergence graphs
* Gantt charts

All outputs are saved inside:

```bash
results/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AdPSO-Cloud-Scheduling.git
```

## Move into Project Directory

```bash
cd AdPSO-Cloud-Scheduling
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python main.py
```

---

# Requirements

* Python 3.10+
* NumPy
* Matplotlib
* Pandas

Install using:

```bash
pip install -r requirements.txt
```

---

# Research Contribution

The main contribution of this work is:

# LDAIW (Linearly Descending Adaptive Inertia Weight)

which improves:

* Exploration and exploitation balance
* Scheduling performance
* Cloud resource utilization
* Convergence behavior

especially for heterogeneous cloud workloads.

---

# Future Improvements

Possible future enhancements:

* Multi-objective optimization
* Cost-aware scheduling
* Energy-aware scheduling
* Hybrid PSO-GA approaches
* Real cloud deployment
* GUI dashboard
* Streamlit visualization

---

# References

S. Nabi, M. Ahmad, M. Ibrahim, and H. Hamam,

“AdPSO: Adaptive PSO-Based Task Scheduling Approach for Cloud Computing,”

Sensors, 2022.

DOI: https://doi.org/10.3390/s22030920

---

