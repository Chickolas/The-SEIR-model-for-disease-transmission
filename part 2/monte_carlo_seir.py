import numpy as np
from agent import Agent

# Numerical labels for each state
state_list = {
    "empty" : 0,
    "susceptible" : 1,
    "exposed" : 2,
    "infected" : 3,
    "recovered" : 4
}

class MonteCarlo():
    def __init__(self, lattice_size = 100, agent_count = 250, p_exposed = 0.05, beta = 1.0, sigma = 0.1, gamma = 0.005, periodic = True, seed = None):
        self.lattice_size = lattice_size
        self.agent_count = agent_count
        self.p_exposed = p_exposed
        self.beta = beta
        self.sigma = sigma
        self.gamma = gamma
        self.periodic = periodic

        if seed is not None:
            np.random.seed(seed)

        self.lattice = np.zeros((lattice_size, lattice_size), d_type=int)
        self.agents = []


    def get_lattice_attributes(self):
        return self.lattice, self.lattice_size, self.periodic

    def initialise_agents(self):
        sites = []
        
        for x in range(self.lattice_size):
            for y in range(self.lattice_size):
                sites.append((x, y))

        chosen_sites = np.random.choice(len(sites), size = self.n_agents, replace = False)

        for i in chosen_sites:
            x, y = sites[i]

            if np.random.random() < self.p_exposed:
                state = state_list["exposed"]
            else:
                state = state_list["susceptible"]

            agent = Agent(x, y, state)
            self.agents.append(agent)
            self.lattice[x, y] = state
