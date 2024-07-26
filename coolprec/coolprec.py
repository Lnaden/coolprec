"""Provide the primary functions."""

import numpy as np


def calculate_distance(vector_a, vector_b):
    # This function calculates the distance between two points given as numpy arrays.
    delta_vector = vector_a - vector_b
    dist = np.linalg.norm(delta_vector)
    return dist


def build_bond_list(coords, max_bond=1.5, min_bond=0):
    if min_bond < 0:
        raise ValueError("Bonds have to be positive")
    bonds = {}
    num_atoms = len(coords)
    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coords[atom1], coords[atom2])
            if min_bond < distance < max_bond:
                bonds[(atom1, atom2)] = distance
    return bonds


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
