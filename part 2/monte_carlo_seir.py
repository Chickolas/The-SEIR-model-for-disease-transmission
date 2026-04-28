import numpy as np
from agent import Agent
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

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
        self._lattice_size = lattice_size
        self.agent_count = agent_count
        self.p_exposed = p_exposed
        self.beta = beta
        self.sigma = sigma
        self.gamma = gamma
        self.periodic = periodic

        if seed is not None:
            np.random.seed(seed)

        self._lattice = np.zeros((lattice_size, lattice_size))
        self._agents = []

        self.S_record = []
        self.E_record = []
        self.I_record = []
        self.R_record = []

        self.initialise_agents()
    
    @property
    def get_lattice(self):
        return self._lattice
    @property
    def get_lattice_size(self):
        return self._lattice_size
    @property
    def get_periodic(self):
        return self.periodic
    @property
    def get_agents(self):
        return self._agents
    
    def set_lattice(self, y, x, state):
        self._lattice[y, x] = state
    def add_agent(self, agent):
        self._agents.append(agent)

    def initialise_agents(self):
        #Initialise every point on the lattice
        sites = []
        for x in range(self.get_lattice_size):
            for y in range(self.get_lattice_size):
                sites.append((y, x))

        #Randomly select sites on the lattice with the amount agent_count
        chosen_sites = np.random.choice(len(sites), size = self.agent_count, replace = False)

        for i in chosen_sites:
            y, x = sites[i]

            #Randomly assign the agent to be exposed or susceptible based off p value
            if np.random.random() < self.p_exposed:
                state = state_list["exposed"]
            else:
                state = state_list["susceptible"]

            #Class creation and appenditure to the array
            agent = Agent(y, x, state)
            self.add_agent(agent)
            self.set_lattice(y, x, state)

    def record_step(self):
        #Appends the current state of the lattice to an array
        states = []
        for agent in self.get_agents:
            states.append(agent.get_state)
        
        #Records each count of SEIR to their respective arrays
        self.S_record.append(states.count(state_list["susceptible"]))
        self.E_record.append(states.count(state_list["exposed"]))
        self.I_record.append(states.count(state_list["infected"]))
        self.R_record.append(states.count(state_list["recovered"]))

    def run(self, steps):
        self.record_step()
        #Runs the simultion for the given number of steps
        for i in range(steps):
            #Shuffles the agents randomly so the same one doesn't always start
            np.random.shuffle(self.get_agents)

            #Try to move the agent and check for a state change
            for agent in self.get_agents:
                agent.attempt_move(self.get_lattice, self.get_lattice_size, self.get_periodic,)
                agent.update_state(self.get_lattice, self.get_lattice_size, self.get_periodic, self.beta, self.sigma, self.gamma)

            #Record the step
            self.record_step()

    #Plot the graphs with the given parameters
    def seir_plot(self):
        #Creates an evenly spaced time interval
        steps = np.arange(len(self.S_record))

        #Plots the SEIR time series graph based of the records
        plt.figure(figsize=(8, 5))
        plt.plot(steps, self.S_record, label="Susceptible")
        plt.plot(steps, self.E_record, label="Exposed")
        plt.plot(steps, self.I_record, label="Infected")
        plt.plot(steps, self.R_record, label="Recovered")

        plt.xlabel("Monte Carlo step")
        plt.ylabel("Population")
        plt.title("Monte Carlo SEIR simulation")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def lattice_plot(self):
        #Creates the colourmap
        colours = ["white", "blue", "orange", "green", "red"]
        cmap = ListedColormap(colours)

        #Plots the last lattice state
        plt.figure(figsize=(6, 6))
        plt.imshow(
            self.get_lattice,
            cmap=cmap,
            origin="lower",
            vmin=0,
            vmax=4
        )

        plt.title("Monte Carlo SEIR lattice")
        plt.xlabel("x position")
        plt.ylabel("y position")
        labels = ["Susceptible", "Exposed", "Infected", "Recovered"]
        state_colours = ["blue", "orange", "green", "red"]
        
        for colour, label in zip(state_colours, labels):
            plt.scatter([], [], color=colour, label=label)

        plt.legend(loc="upper right")
        plt.tight_layout()
        plt.show()

