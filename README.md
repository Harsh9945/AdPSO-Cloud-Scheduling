# AdPSO: Adaptive PSO-Based Task Scheduling for Cloud Computing

## Overview

This project implements the research paper:

**“AdPSO: Adaptive PSO-Based Task Scheduling Approach for Cloud Computing”**

The project uses Particle Swarm Optimization (PSO) with a proposed adaptive inertia weight strategy called **LDAIW (Linearly Descending Adaptive Inertia Weight)** to optimize cloud task scheduling.

## Features

* PSO-based task scheduling
* Adaptive inertia weight strategies
* Makespan minimization
* Throughput maximization
* Average Resource Utilization Ratio (ARUR)
* HCSP benchmark dataset support

## Implemented Inertia Strategies

* LDIW
* AIW
* LDAIW (Proposed)

## Technologies Used

* Python
* NumPy
* Matplotlib
* HCSP Dataset

## Project Structure

* `particle.py` → Particle implementation
* `pso.py` → Main PSO algorithm
* `inertia.py` → Inertia weight strategies
* `calculator.py` → Metrics calculation
* `main.py` → Entry point

## Metrics

* Makespan
* Throughput
* ARUR

## Research Contribution

The proposed LDAIW strategy improves exploration and exploitation balance in PSO and achieves better scheduling performance compared to traditional inertia weight approaches.

## Author

Harsh Jaiswal
