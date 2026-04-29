import numpy
from seir_model import seir_solver, seir_plot, calculate_R0, delete_old_files
from test_seir_model import test_non_negative, test_population_is_conserved

#R0 growth vs decay
r0_cases = [
    {"name": "R0 > 1", "beta": 1.0, "sigma": 1.0, "gamma": 0.1, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "R0 < 1", "beta": 0.05, "sigma": 1.0, "gamma": 0.1, "y0": [0.90, 0.05, 0.05, 0.0]},
]

#Incubation rate changes
sigma_cases = [
    {"name": "sigma 0.2", "beta": 0.5, "sigma": 0.2, "gamma": 0.1, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "sigma 1.0", "beta": 0.5, "sigma": 1.0, "gamma": 0.1, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "sigma 2.0", "beta": 0.5, "sigma": 2.0, "gamma": 0.1, "y0": [0.99, 0.01, 0.00, 0.0]},
]

#Recovery rate changes
gamma_cases = [
    {"name": "gamma 0.05", "beta": 0.5, "sigma": 1.0, "gamma": 0.05, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "gamma 0.10", "beta": 0.5, "sigma": 1.0, "gamma": 0.10, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "gamma 0.30", "beta": 0.5, "sigma": 1.0, "gamma": 0.30, "y0": [0.99, 0.01, 0.0, 0.0]},
]

#Initial conditions study
initial_condition_cases = [
    {"name": "small initial exposure (0.1%)", "beta": 0.5, "sigma": 1.0, "gamma": 0.1, "y0": [0.999, 0.001, 0.0, 0.0]},
    {"name": "medium initial exposure (1%)", "beta": 0.5, "sigma": 1.0, "gamma": 0.1, "y0": [0.99, 0.01, 0.0, 0.0]},
    {"name": "large initial exposure (5%)", "beta": 0.5, "sigma": 1.0, "gamma": 0.1, "y0": [0.95, 0.05, 0.0, 0.0]},
]

def main():
    #Deletes all old files in the figures folder
    delete_old_files()

    #Combines all the cases from above
    all_cases = r0_cases + sigma_cases + gamma_cases + initial_condition_cases

    #For every given case, we solve the seir equations and plot them 
    for case in all_cases:
        s ,e ,i ,r, t = seir_solver(case["beta"], case["sigma"], case["gamma"], case["y0"], 100, 1000)

        #Calculates the R0 value for the title
        R0 = calculate_R0(case["beta"], case["gamma"], case["y0"][0])
        title = f"{case['name']}, R0={R0:.2f}"

        #Plots the graph
        seir_plot(s ,e ,i ,r, t, title)

#Only runs if this file is the main 
if __name__ == "__main__":
    main()