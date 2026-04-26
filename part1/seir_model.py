import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def seir_eqns(time, y, beta, sigma, gamma):

    susceptible, exposed, infected, recovered = y

    #Apply the differential equations from the SEIR equations
    dSdt = -beta * infected * susceptible
    dEdt = beta * infected * susceptible - sigma * exposed
    dIdt = sigma * exposed - gamma * infected
    dRdt = gamma * infected

    return [dSdt, dEdt, dIdt, dRdt]

def seir_solver(beta, sigma, gamma, y0, time_end, points):

    #evaluates the integral 
    t_eval = np.linspace(0, time_end, points)
    sol = solve_ivp(
        seir_eqns,
        [0, time_end],
        y0,
        args=(beta, sigma, gamma),
        t_eval=t_eval
    )
    s ,e ,i ,r = sol.y
    t = sol.t

    #returns SEIR and time variables
    return s ,e ,i ,r, t

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

y0 = [0.99, 0.01, 0.0, 0.0]

#R0 growth vs decay
r0_cases = [
    {"name": "R0 > 1", "beta": 1.0, "sigma": 1.0, "gamma": 0.1, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "R0 < 1", "beta": 0.05, "sigma": 1.0, "gamma": 0.1, "y0": [0.99, 0.01, 0.0, 0.0]},
]

#Incubation rate changes
sigma_cases = [
    {"name": "sigma 0.2", "beta": 0.5, "sigma": 0.2, "gamma": 0.1, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "sigma 1.0", "beta": 0.5, "sigma": 1.0, "gamma": 0.1, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "sigma 2.0", "beta": 0.5, "sigma": 2.0, "gamma": 0.1, "y0": [0.99, 0.01, 0.0, 0.0]},
]

#Recovery rate changes
gamma_cases = [
    {"name": "gamma 0.05", "beta": 0.5, "sigma": 1.0, "gamma": 0.05, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "gamma 0.10", "beta": 0.5, "sigma": 1.0, "gamma": 0.10, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "gamma 0.30", "beta": 0.5, "sigma": 1.0, "gamma": 0.30, "y0": [0.99, 0.01, 0.0, 0.0]},
]

#Initial conditions study
initial_condition_cases = [
    {"name": "Small initial exposure (0.1%)", "beta": 0.5, "sigma": 1.0, "gamma": 0.1, "y0": [0.999, 0.001, 0.0, 0.0]},
    {"name": "medium initial exposure (1%)", "beta": 0.5, "sigma": 1.0, "gamma": 0.1, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "large initial exposure (5%)", "beta": 0.5, "sigma": 1.0, "gamma": 0.1, "y0": [0.95, 0.05, 0.0, 0.0]},
]
#For every given case, we solve the seir equations and plot them 
for case in r0_cases + sigma_cases + gamma_cases + initial_condition_cases:
    s ,e ,i ,r, t = seir_solver(case["beta"], case["sigma"], case["gamma"], case["y0"], 100, 1000)
    seir_plot(s ,e ,i ,r, t, case["name"])