from monte_carlo_seir import MonteCarlo

if __name__ == "__main__":

    sim = MonteCarlo(
        lattice_size=100,
        agent_count=250,
        p_exposed=0.05,
        beta=1.0,
        sigma=0.1,
        gamma=0.005,
        periodic=True,
        seed=1234
    )

    sim.run(2000)
    sim.lattice_plot()
    sim.seir_plot()

