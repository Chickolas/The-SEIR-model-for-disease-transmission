# SEIR Model Simulation

<p align="center">
<img width="800" alt="r0_greater_than_1,_r09 90" src="https://github.com/user-attachments/assets/a770f5b4-2059-4da4-ac3f-7bb9c6c86b89" />
</p>

## Description

This project investigates disease spread using the **SEIR model** through two different approaches:

1. A **deterministic SEIR model**, solved as an initial value problem using coupled differential equations.
2. A **stochastic Monte Carlo SEIR model**, where individual agents move randomly across a 2D lattice and spread infection through local contact.

The deterministic model treats the population as continuous fractions: susceptible, exposed, infected and recovered. The Monte Carlo model treats the population as individual agents, each storing its own position and SEIR state.

The aim is to compare the smooth deterministic solution with a stochastic Brownian-motion analogue and investigate when outbreaks occur or die away.

## Project structure

```text
Test2/
│
├── part 1/
│   ├── seir_model.py
│   ├── run_seir_model.py
│   └── figures/
│
├── part 2/
│   ├── agent.py
│   ├── monte_carlo_seir.py
│   ├── run_monte_carlo_simulation.py
│   └── figures/
│
├── tests/
│   ├── test_monte_carlo.py
|   └── test_seir_model.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

This project uses Python 3 and the following packages:

```code
numpy
matplotlib
scipy
pytest
```

Install the required packages using:
```
python -m pip install -r requirements.txt
```
If pytest is not recognised directly in PowerShell, use:
```
python -m pytest
```
## Deterministic SEIR model

The deterministic SEIR model solves the reduced SEIR equations for the population fractions:
```
s = susceptible fraction
e = exposed fraction
i = infected fraction
r = recovered fraction
```
The transition parameters are:
```
beta  = infection rate
sigma = incubation rate
gamma = recovery rate
```
The basic reproduction factor is approximated by:
```
R0 = beta / gamma
```
when the initial susceptible fraction is close to 1.

The deterministic model is implemented in:
```
part 1/seir_model.py
```
This file uses scipy.integrate.solve_ivp to solve the coupled differential equations and matplotlib to plot the compartment populations against time.

To run Part 1:
```
python "part 1/run_seir_model.py"
```
The generated figures are saved in:
```
part 1/figures/
```

## Monte Carlo SEIR model

<p align="center">
  <img width="400" alt="lattice_snapshot_example_case" src="https://github.com/user-attachments/assets/47203fa2-d21a-4458-ab63-5cbbdebb07c2" />
  <img width="600" alt="seir_populations_example_case" src="https://github.com/user-attachments/assets/2e4aa673-7dc8-4453-8e3f-fac93dc22a71" />
</p>

The Monte Carlo model was implemented using two Python classes: **Agent** and **MonteCarlo**. The **Agent** class represents one individual and stores its lattice position and SEIR state. This allows each agent to move to a neighbouring lattice site, check if any nearest neighbours are infected, and update its disease state.

The **MonteCarlo** class manages the whole simulation. It creates the lattice, places agents randomly on empty lattice sites, runs the Monte Carlo steps, records the population counts, and produces the plots.

At each Monte Carlo step, the list of agents is shuffled to avoid update-order bias. Each agent then attempts to move randomly to one of the four adjacent sites. If the target site is empty, the agent moves and the lattice is updated; if the target site is occupied, the agent remains in place. Periodic boundary conditions are used so that agents leaving one side of the lattice re-enter from the opposite side.

The states were represented numerically as

```
- 0 = empty
- 1 = susceptible 
- 2 = exposed 
- 3 = infected 
- 4 = recovered 
```

After movement, the agent's SEIR state is updated. Susceptible agents check neighbouring sites for infected agents and become exposed with probability $\beta$ if an infected neighbour is present. Exposed agents become infected with probability $\sigma$, and infected agents recover with probability $\gamma$. After all agents are updated, the total numbers of susceptible, exposed, infected and recovered agents are counted and stored for plotting.

For the example above, I used the following parameters

```
- lattice size: $100 \times 100$;
- number of agents: 250;
- initial exposed probability: $p_{\mathrm{exposed}} = 0.05$;
- beta = 1.0
- sigma = 0.1
- gamma = 0.005
```

Unlike the deterministic model, this simulation uses direct contact to induce infection. A susceptible agent can only become exposed if it is adjacent to an infected agent.

From the main project folder:
```
python "part 2/run_monte_carlo_simulation.py"
```
This runs all Monte Carlo investigation cases.
Figures are saved to:
```
part 2/figures/
```

## Run Tests

From the main project folder:
```
python -m pytest
```
The tests check that:
**Part 1:**
- there are no negative population fractions
- the population is conserved

**Part 2:**
- the correct number of agents are initialised,
- the population is conserved,
- no new infections occur when beta = 0,
- exposed agents become infected when sigma = 1,
- infected agents recover when gamma = 1,
- the recorded arrays have the correct length.

## Git / Setup

Clone the repository:
```
git clone https://github.com/Chickolas/The-SEIR-model-for-disease-transmission
cd The-SEIR-model-for-disease-transmission
```
Install requirements:
```
python -m pip install -r requirements.txt
```
Run the deterministic model:
```
python "part 1/run_seir_model.py"
```
Run the Monte Carlo investigation:
```
python "part 2/run_monte_carlo_simulation.py"
```
Run tests:
```
python -m pytest
```

## Troubleshooting

**pytest** is not recognised

Use:
```
python -m pytest
```
If pytest is not installed:
```
python -m pip install pytest
```
**Figures are not appearing**

Make sure you are running the scripts from the main project folder.
```
python "part 2/run_monte_carlo_simulation.py"
```
**No infection spreads in the Monte Carlo model**

Check that beta is greater than zero and that the density is high enough for agents to encounter infected neighbours.

**Monte Carlo results change between runs**

The Monte Carlo model is stochastic. Use a fixed random seed **(initially set to 1234)** to make results reproducible.
