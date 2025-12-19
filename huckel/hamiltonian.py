import numpy as np

def build_hamiltonian(data):
    n_atoms = len(data["atoms"])
    H = np.zeros((n_atoms, n_atoms), dtype=float)

    alpha = data["alpha"]
    beta = data["beta"]

    for i in range(n_atoms):
        H[i, i] = alpha

    for bond in data["bonds"]:
        i, j = bond
        H[i, j] = beta
        H[j, i] = beta

    return H