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

