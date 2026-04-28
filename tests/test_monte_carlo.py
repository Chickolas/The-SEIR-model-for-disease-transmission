import sys
from pathlib import Path
import numpy as np
sys.path.append(str(Path(__file__).resolve().parents[1] / "part 2"))

from monte_carlo_seir import MonteCarlo, state_list

def test_correct_number_of_agents_initialised():
    sim = MonteCarlo(
        lattice_size=20,
        agent_count=50,
        p_exposed=0.1,
        beta=1.0,
        sigma=0.1,
        gamma=0.01,
        periodic=True,
        seed=1
    )
    #Tests that the correct number or agents is initialised properly
    assert len(sim.get_agents) == 50
    assert np.count_nonzero(sim.get_lattice) == 50


def test_population_is_conserved():
    sim = MonteCarlo(
        lattice_size=30,
        agent_count=100,
        p_exposed=0.1,
        beta=1.0,
        sigma=0.1,
        gamma=0.01,
        periodic=True,
        seed=2
    )

    sim.run(100)

    for S, E, I, R in zip(
        sim.S_record,
        sim.E_record,
        sim.I_record,
        sim.R_record
    ):
        #Tests that SEIR adds up to the starting number of agents
        assert S + E + I + R == 100


def test_beta_zero_prevents_new_infections():
    sim = MonteCarlo(
        lattice_size=30,
        agent_count=100,
        p_exposed=0.1,
        beta=0.0,
        sigma=0.1,
        gamma=0.01,
        periodic=True,
        seed=3
    )

    sim.run(200)

    #With beta=0 no more susceptible should become exposed to the virus
    initial_susceptible = sim.S_record[0]
    final_non_susceptible = (
        sim.E_record[-1] + sim.I_record[-1] + sim.R_record[-1]
    )

    #Checks no more agents become infected
    assert final_non_susceptible <= 100 - initial_susceptible


def test_sigma_removes_exposed():
    sim = MonteCarlo(
        lattice_size=30,
        agent_count=100,
        p_exposed=0.2,
        beta=0.0,
        sigma=1.0,
        gamma=0.0,
        periodic=True,
        seed=4
    )

    sim.run(1)
    #Checks that agents can randomly move from exposed to infected
    assert sim.E_record[-1] == 0
    assert sim.I_record[-1] > 0


def test_gamma_removes_infected():
    sim = MonteCarlo(
        lattice_size=30,
        agent_count=100,
        p_exposed=0.2,
        beta=0.0,
        sigma=1.0,
        gamma=1.0,
        periodic=True,
        seed=5
    )

    sim.run(3)

    #Checks that agents can randomly move from Infected to Recovered
    assert sim.E_record[-1] == 0
    assert sim.I_record[-1] == 0
    assert sim.R_record[-1] > 0


def test_starting_state_is_captured():
    sim = MonteCarlo(
        lattice_size=20,
        agent_count=50,
        p_exposed=0.1,
        beta=1.0,
        sigma=0.1,
        gamma=0.01,
        periodic=True,
        seed=6
    )

    sim.run(25)

    #Checks that the initial starting state is recorded
    assert len(sim.S_record) == 26
    assert len(sim.E_record) == 26
    assert len(sim.I_record) == 26
    assert len(sim.R_record) == 26