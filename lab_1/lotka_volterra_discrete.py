import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'


def lotka_volterra_discrete(preys, predators, alpha, beta, gamma, delta, carrying_cap, num_steps):
    prey_population = [preys]
    predator_population = [predators]

    for _ in range(num_steps):
        next_preys = preys + (alpha * preys*(1-preys/carrying_cap)) - (1-(1/(beta * predators+1)))*preys
        next_predators = predators + (delta * preys * predators - gamma * predators)

        preys = next_preys
        predators = next_predators

        prey_population.append(preys)
        predator_population.append(predators)

    return prey_population, predator_population


# Parameters
prey_birth_rate = 5  # r
predation_rate = 1   # b
predator_death_rate = 1   # d
predator_birth_rate = 1  # Reproduction rate of predators # c
env_carrying_cap = 5
nsteps = 1000

# Initial populations
initial_preys = 1
initial_predators = 1

# Simulate the model
prey_populations, predator_populations = lotka_volterra_discrete(initial_preys, initial_predators,
                                                                 prey_birth_rate, predation_rate,
                                                                 predator_death_rate, predator_birth_rate,
                                                                 env_carrying_cap, nsteps)
sim_time = [i for i in range(len(prey_populations))]
df_sim = pd.DataFrame({'time': sim_time,
                       'prey': prey_populations,
                       'predator': predator_populations})

fig = px.line(df_sim, x='time', y=['prey', 'predator'], title='My first population model')
fig.update_layout(xaxis_title='Time',
                  yaxis_title='State variable')

fig.show()

ph_sp = px.line(df_sim, x = 'prey' , y='predator', title='My first Population Phase Space')
ph_sp.update_layout(xaxis_title='x',
                  yaxis_title='y')

ph_sp.show()
