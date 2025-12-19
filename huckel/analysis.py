import numpy as np
from huckel.solver import frontier_orbitals

def total_pi_energy(energies, n_occupied):
    return 2 * np.sum(energies[:n_occupied])

def electron_density(orbitals, n_occupied):
    rho = 2 * np.sum(np.abs(orbitals[:, :n_occupied])**2, axis=1)
    return rho

def analyze(energies, orbitals, n_occupied):
    total_energy = total_pi_energy(energies, n_occupied)
    rho = electron_density(orbitals, n_occupied)
    frontier = frontier_orbitals(energies, n_occupied)

    results = {
        "total_pi_energy": total_energy,
        "electron_density": rho,
        "HOMO_energy": frontier["HOMO_energy"],
        "LUMO_energy": frontier["LUMO_energy"],
        "HOMO_LUMO_gap": frontier["HOMO_LUMO_gap"]
    }

    return results