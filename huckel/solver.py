import numpy as np

def solve_huckel(H):
    energies, orbitals = np.linalg.eigh(H)

    idx = np.argsort(energies)
    energies = energies[idx]
    orbitals = orbitals[:, idx]

    return energies, orbitals

def occupied_orbitals(energies, n_electrons):
    if n_electrons % 2 != 0:
        raise ValueError("Odd number of electrons not supported in simple Hückel theory.")
    return n_electrons // 2

def frontier_orbitals(energies, n_occupied):
    HOMO_index = n_occupied - 1
    LUMO_index = n_occupied
    HOMO_energy = energies[HOMO_index]
    LUMO_energy = energies[LUMO_index]
    gap = LUMO_energy - HOMO_energy

    return {
        "HOMO_index": HOMO_index,
        "LUMO_index": LUMO_index,
        "HOMO_energy": HOMO_energy,
        "LUMO_energy": LUMO_energy,
        "HOMO_LUMO_gap": gap
    }