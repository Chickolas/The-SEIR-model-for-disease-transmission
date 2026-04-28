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
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    #Getters for all attributes
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_state(self):
        return self.state
    
    #Setters for all attributes
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def set_state(self, state):
        self.state = state

    def attempt_move(self, lattice, lattice_size, periodic):
        #Picks a random movement option from the list
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        dx,dy = moves[np.randint(len(moves))]

        #Gets the new location of the agent
        next_x = self.get_x() + dx
        next_y = self.get_y() + dy

        #If periodic wrap around to the other side
        if periodic:
            next_x = next_x % lattice_size
            next_y = next_y % lattice_size
        else: 
            #If the agent tries to moves off screen stay in the same position
            if next_x < 0 or next_x >= lattice_size or next_y < 0 or next_y >= lattice_size:
                return
    
        #If the new location is inoccupied
        if lattice[next_x, next_y] == state_list["empty"]:
            #Move the agent to the new location
            lattice[self.get_x(), self.get_y()] = None
            self.set_x(next_x)
            self.set_y(next_y)
            lattice[self.get_x(), self.get_y()] = self.state