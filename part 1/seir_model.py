import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def seir_eqns(time, y, beta, sigma, gamma):

    #Unpacks the current SEIR fractions
    susceptible, exposed, infected, recovered = y

    #Apply the differential equations from the SEIR equations
    dSdt = -beta * infected * susceptible
    dEdt = beta * infected * susceptible - sigma * exposed
    dIdt = sigma * exposed - gamma * infected
    dRdt = gamma * infected

    return [dSdt, dEdt, dIdt, dRdt]

def seir_solver(beta, sigma, gamma, y0, time_end, points):

    #Creates time values to store the solution
    t_eval = np.linspace(0, time_end, points)

    #Numerically solve the SEIR equations
    sol = solve_ivp(
        seir_eqns,
        [0, time_end],
        y0,
        args=(beta, sigma, gamma),
        t_eval=t_eval
    )
    
    if not sol.success:
        raise RuntimeError(f"ODE solver failed: {sol.message}")
    
    s ,e ,i ,r = sol.y
    t = sol.t

    #returns SEIR and time variables
    return s ,e ,i ,r, t

#Plot the graphs with the given parameters
def seir_plot(s ,e ,i ,r ,t, name):
    plt.figure(figsize=(8, 5))
    plt.plot(t, s, label="Susceptible")
    plt.plot(t, e, label="Exposed")
    plt.plot(t, i, label="Infected")
    plt.plot(t, r, label="Recovered")
    plt.xlabel("Time (days)")
    plt.ylabel("Fraction of population")
    plt.title(f"SEIR model with {name}")
    plt.legend()
    plt.grid(True)
    plt.show()

#Calculates R0 to add to the graphs
def calculate_R0(beta, gamma, s0):
    return (beta / gamma) * s0