"""
Unit and regression test for the coolprec package.
"""

# Import package, test suite, and other packages as needed
import pytest
import coolprec
import numpy as np


@pytest.fixture
def methane_molecule():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([
        [1,    1, 1],
        [2.4,  1, 1],
        [-0.4, 1, 1],
        [1,    1, 2.4],
        [1,    1, -0.4],
    ])
    return symbols, coordinates


def test_build_bond_list_simple(methane_molecule):
    _, coordinates = methane_molecule
    bonds = coolprec.build_bond_list(coordinates)
    assert len(bonds) == 4
    for bond_length in bonds.values():
        assert pytest.approx(bond_length) == 1.4


def test_build_bond_bad_min(methane_molecule):
    _, coordinates = methane_molecule
    with pytest.raises(ValueError):
        coolprec.build_bond_list(coordinates, min_bond=-1)


from scipy.spatial.distance import cdist

@pytest.fixture
def distances(methane_molecule):
    coords = methane_molecule[-1]
    distances = cdist(coords, coords)
    return distances


bad_min = pytest.param(-1, marks=pytest.mark.xfail(raises=ValueError))


@pytest.fixture(params=['euclidean', "cityblock"])
def multi_distance_metrics(methane_molecule, request):
    metric = request.param
    if metric == 'cityblock':
        pytest.xfail("I've gone mad with power!")
    coordinates = methane_molecule[-1]
    distances = cdist(coordinates, coordinates, metric=metric)
    return distances


@pytest.mark.parametrize("min_bond", [0, 1/6, 1/3, .5, bad_min])
@pytest.mark.parametrize("max_bond", [1, 2, 3, 4])
def test_multi_bond(methane_molecule, multi_distance_metrics, min_bond, max_bond):
    coordinates = methane_molecule[-1]
    theoretical_bonds = np.sum(
        (max_bond > multi_distance_metrics) & (multi_distance_metrics > min_bond)) / 2
    bonds = coolprec.build_bond_list(coordinates,
                                     max_bond=max_bond,
                                     min_bond=min_bond)

    assert len(bonds) == theoretical_bonds


