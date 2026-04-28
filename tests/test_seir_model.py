import sys
from pathlib import Path
import numpy as np
sys.path.append(str(Path(__file__).resolve().parents[1] / "part 1"))

from monte_carlo_seir import MonteCarlo, state_list
from seir_model import seir_solver

def test_population_is_conserved():
    s, e, i, r, t = seir_solver(
        beta=1.0,
        sigma=1.0,
        gamma=0.1,
        y0=[0.99, 0.01, 0.0, 0.0],
        time_end=100,
        points=1000
    )

    #Tests that all the values in seir add to 1
    total = s + e + i + r

    assert np.allclose(total, 1.0, atol=1e-6)

def test_non_negative():
    s, e, i, r, t = seir_solver(
        beta=1.0,
        sigma=1.0,
        gamma=0.1,
        y0=[0.99, 0.01, 0.0, 0.0],
        time_end=100,
        points=1000
    )

    #Tests that all the values retrieved from seir_solver are positive
    assert np.min(s) >= -1e-5
    assert np.min(e) >= -1e-5
    assert np.min(i) >= -1e-5
    assert np.min(r) >= -1e-5

