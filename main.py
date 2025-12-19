import sys
from huckel.parser import load_input
from huckel.hamiltonian import build_hamiltonian
from huckel.solver import solve_huckel, occupied_orbitals
from huckel.analysis import analyze
import numpy as np

def main(file_path):
    data = load_input(file_path)
    print(f"Loaded molecule with {len(data['atoms'])} atoms and {len(data['bonds'])} bonds.")
    print(f"Number of π electrons: {data['electrons']}\n")

    H = build_hamiltonian(data)
    print("Hückel Hamiltonian matrix (H):")
    print(H, "\n")

    energies, orbitals = solve_huckel(H)
    print("Orbital energies (β units, ascending):")
    print(np.round(energies, 3), "\n")

    n_occ = occupied_orbitals(energies, data['electrons'])
    print(f"Number of occupied orbitals: {n_occ}\n")

    results = analyze(energies, orbitals, n_occ)

    print("=== Analysis Summary ===")
    print(f"Total π-electron energy: {results['total_pi_energy']:.3f}")
    print(f"HOMO energy: {results['HOMO_energy']:.3f}")
    print(f"LUMO energy: {results['LUMO_energy']:.3f}")
    print(f"HOMO-LUMO gap: {results['HOMO_LUMO_gap']:.3f}")
    print(f"Electron density per atom: {np.round(results['electron_density'], 3)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Command to use: python main.py <path_to_input_json>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)