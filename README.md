# Hückel Molecular Orbital Solver

## Overview
This repository contains a Python-based, modular implementation of Hückel molecular orbital theory for modelling π-electron systems in conjugated organic molecules. Given a molecular connectivity description, the program constructs the Hückel Hamiltonian matrix, solves the corresponding eigenvalue problem, and computes key molecular orbital properties such as orbital energies, HOMO–LUMO gaps, total π-electron energy, and electron density distributions. This project serves as a practical implementation of Hückel theory.

---

## Table of Contents:
- [Overview](#differential-expression-analysis)
- [Content](#content)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Input](#input)

---

## Content
Hückel molecular orbitals theory is an approximate quantum mechanical method used to describe π-electron systems in planar, conjugated molecules.

Assumptions:
- There are only π-electrons
- Each atom contributes one p-orbital
- Only nearest-neighbour orbitals interact
- No orbital overlap
- Two empirical parameters are used:
    - α: atomic orbital energy
    - β: resonance integral between bonded atoms

The Hückel Hamiltonian matrix is defined as:

$$
H_{ij} =
\begin{cases}
\alpha & i = j \\
\beta & i,j \text{ bonded} \\
0 & \text{otherwise}
\end{cases}
$$

This converts molecular connectivity into a matrix eigenvalue problem.

Molecular Orbitals

The Schrödinger equation reduces to:

$$
H \mathbf{c}_k = E_k \mathbf{c}_k
$$

Solving this yields:

- Eigenvalues, $$E_k$$: π-molecular orbital energies
- Eigenvectors,  $$C_k$$: atomic orbital coefficients

From these, additional chemical properties can be derived.

---

## Project Structure

```
huckel_solver/
├── huckel/
│   ├── __init__.py
│   ├── parser.py
│   ├── hamiltonian.py
│   ├── solver.py
│   └── analysis.py
├── tests/
│   ├── benzene.json
│   └── butadiene.json
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Prerequisites:

- Python 3.8 or higher
- NumPy

1. Clone the repository:

```bash
git clone https://github.com/heitor-sg5/huckel_solver.git
cd huckel_solver
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage
Run the program from the project root:

```bash
python main.py tests/benzene.json
```

The program will:
1. Parse the molecular input file
2. Cunstruct the Hamiltonian matrix
3. Solve for the orbital energies and coefficients
4. Compute derived π-electron properties
5. Print results

---

## Input

The input is provided as a JSON file describing the π system.

Example:

```bash
{
  "atoms": ["C", "C", "C", "C"],
  "bonds": [[0,1],[1,2],[2,3]],
  "electrons": 4,
  "alpha": 0.0,
  "beta": -1.0
}
```

Field descriptions:

| Field     | Description                                   |
| --------- | --------------------------------------------- |
| atoms     | List of atoms contributing π-orbitals         |
| bonds     | Pairs of atom indices defining π-interactions |
| electrons | Total number of π-electrons                   |
| alpha     | Molecular orbital energy                      |
| beta      | Resonance integral between bonded atoms       |
