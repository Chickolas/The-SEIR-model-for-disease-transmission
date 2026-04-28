from monte_carlo_seir import MonteCarlo

def run_monte_carlo():
    cases = {
        "example_case": MonteCarlo(
            lattice_size=100,
            agent_count=250,
            p_exposed=0.05,
            beta=1.0,
            sigma=0.1,
            gamma=0.005,
            periodic=True,
            seed=1234
        ),

        "low_density_outbreak": MonteCarlo(
            lattice_size=100,
            agent_count=100,
            p_exposed=0.05,
            beta=0.5,
            sigma=0.1,
            gamma=0.05,
            periodic=True,
            seed=1234
        ),

        "high_density_outbreak": MonteCarlo(
            lattice_size=100,
            agent_count=1000,
            p_exposed=0.05,
            beta=1.0,
            sigma=0.1,
            gamma=0.005,
            periodic=True,
            seed=1234
        ),

        "fast_recovery_outbreak": MonteCarlo(
            lattice_size=100,
            agent_count=250,
            p_exposed=0.05,
            beta=1.0,
            sigma=0.1,
            gamma=0.1,
            periodic=True,
            seed=1234
        ),

        "slow_recovery_outbreak": MonteCarlo(
            lattice_size=100,
            agent_count=250,
            p_exposed=0.05,
            beta=1.0,
            sigma=0.1,
            gamma=0.002,
            periodic=True,
            seed=1234
        ),

        "slow_incubation": MonteCarlo(
            lattice_size=100,
            agent_count=250,
            p_exposed=0.05,
            beta=1.0,
            sigma=0.02,
            gamma=0.005,
            periodic=True,
            seed=1234
        ),

        "fast_incubation": MonteCarlo(
            lattice_size=100,
            agent_count=250,
            p_exposed=0.05,
            beta=1.0,
            sigma=0.3,
            gamma=0.005,
            periodic=True,
            seed=1234
        )
    }

    for name, sim in cases.items():
        print(f"\nRunning case: {name}")

        sim.run(2000)

        print(f"Initial S: {sim.S_record[0]}")
        print(f"Initial E: {sim.E_record[0]}")
        print(f"Peak infected: {max(sim.I_record)}")
        print(f"Final susceptible: {sim.S_record[-1]}")
        print(f"Final exposed: {sim.E_record[-1]}")
        print(f"Final infected: {sim.I_record[-1]}")
        print(f"Final recovered: {sim.R_record[-1]}")

        sim.lattice_plot(title=f"Lattice snapshot: {name}")
        sim.seir_plot(title=f"SEIR populations: {name}")

if __name__ == "__main__":
    MonteCarlo.delete_old_files()
    run_monte_carlo()

