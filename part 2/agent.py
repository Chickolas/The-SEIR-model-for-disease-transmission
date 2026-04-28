import numpy as np

#State labels
state_list = {
    "empty" : 0,
    "susceptible" : 1,
    "exposed" : 2,
    "infected" : 3,
    "recovered" : 4
}

class Agent:
    #Initialises the position and state of the agent
    def __init__(self, y, x, state):
        self._x = x
        self._y = y
        self._state = state

    #Getters for all attributes
    @property
    def get_x(self):
        return self._x
    @property
    def get_y(self):
        return self._y
    @property
    def get_state(self):
        return self._state
    
    #Setters for all attributes
    def set_x(self, x):
        self._x = x
    def set_y(self, y):
        self._y = y
    def set_state(self, state):
        self._state = state

    def attempt_move(self, lattice, lattice_size, periodic):
        #Picks a random movement option from the list
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        dx, dy = moves[np.random.randint(len(moves))]

        #Gets the new location of the agent
        next_x = self.get_x + dx
        next_y = self.get_y + dy

        #If periodic wrap around to the other side
        if periodic:
            next_x = next_x % lattice_size
            next_y = next_y % lattice_size
        else: 
            #If the agent tries to moves off screen stay in the same position
            if next_x < 0 or next_x >= lattice_size or next_y < 0 or next_y >= lattice_size:
                return
    
        #If the new location is unoccupied
        if lattice[next_y, next_x] == state_list["empty"]:
            #Move the agent to the new location
            lattice[self.get_y, self.get_x] = state_list["empty"]
            self.set_x(next_x)
            self.set_y(next_y)
            lattice[self.get_y, self.get_x] = self.get_state

    def check_neighbour_infected(self, lattice, lattice_size, periodic):
        #Iterates through every location adjacent to the agent
        neighbours = [(1,0), (0,1), (-1,0), (0,-1)]
        for dx,dy in neighbours:
            neighbour_x = self.get_x + dx
            neighbour_y = self.get_y + dy

            if periodic:
                neighbour_x = neighbour_x % lattice_size
                neighbour_y = neighbour_y % lattice_size
            else:
                if neighbour_x < 0 or neighbour_x >= lattice_size or neighbour_y < 0 or neighbour_y >= lattice_size:
                    continue
            
            #Checks if the neighbour is infected and returns true
            if lattice[neighbour_y, neighbour_x] == state_list["infected"]:
                return True
        
        #If none of the adjacent squares have an infected agent return false 
        return False
    
    def update_state(self, lattice, lattice_size, periodic, beta, sigma, gamma, p_reinfection):
        #Checks if the agent is susceptible to the virus
        if self.get_state == state_list["susceptible"]:
            #Checks whether any adjacent neighbour has been infected by the virus
            if self.check_neighbour_infected(lattice, lattice_size, periodic):
                #Randomly cause the agent to be exposed based off beta
                if np.random.random() < beta:
                    self.set_state(state_list["exposed"])

        #Checks if the agent has been exposed to the virus
        elif self.get_state == state_list["exposed"]:
            #Randomly cause the agent to become infected with the virus based off sigma
            if np.random.random() < sigma:
                self.set_state(state_list["infected"])

        #Checks if the agent has already been infected by the virus
        elif self.get_state == state_list["infected"]:
            #Randomly cause the agent to recover based off gamma
            if np.random.random() < gamma:
                self.set_state(state_list["recovered"])

        #Added custom reinfection rate
        elif self.get_state == state_list["recovered"]:
            #Checks whether any adjacent neighbour has been infected by the virus
            if self.check_neighbour_infected(lattice, lattice_size, periodic):
                #Randomly cause the agent to recover based off the reinfection rate
                if np.random.random() < p_reinfection:
                    self.set_state(state_list["exposed"])


        #Updates the agent's state in the global lattice
        lattice[self.get_y, self.get_x] = self.get_state