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

 