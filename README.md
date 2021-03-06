# Squirrel: A Switching Hyperparameter Optimizer

Forked version of the "Switching Squirrel" that includes a local installation and a run file.

From the original authors:

Motivated by the fact that different optimizers work well on different problems, our approach switches between different optimizers. Since the team names on the competition's leaderboard were randomly generated, consisting of an adjective and an animal with the same initial letter, we called our approach the Switching Squirrel, short, Squirrel.

In our Squirrel framework, we switched between the following components: 
1. An initial design (for known hyperparameter spaces: found by meta-learning; otherwise: selected by differential evolution) (3 batches);
2. Optimization using Bayesian optimization by integrating the SMAC optimizer with a portfolio of different triplets of surrogate model, acquisition function, and output space transformation (8 batches); and
3. Optimization using Differential Evolution with parameter adaptation (5 batches)  

## Results 
The Squirrel **ranked 3rd** with a **score of 92.551** on [offical learderboard](https://bbochallenge.com/leaderboard), and also won **1st place** in [alternate leaderboard](https://bbochallenge.com/altleaderboard) (with a score of **94.845476** and the organizers' bootstrap analysis showing a 100% confidence in this 1st place ranking). 

## Run Squirrel locally

Installation:

```
python setup.py develop
```

## Setting the Search Space

To optimize an objective, you'll need to pass a config dict which uses AutoML's `ConfigSpace` API.

Example Configuration:

```
config = {
    'x': {'type': 'int', 'space': 'linear', 'range': (0, 10)},
    'y': {'type': 'int', 'space': 'linear', 'range': (0, 10)},
    'z': {'type': 'real', 'space': 'bilog', 'range': (-1, 1)},
    'a': {'type': 'real', 'space': 'logit', 'range': (1e-9, 1e-6)},
    'b': {'type': 'bool'},
    'c': {'type': 'cat', 'values': ['aa', 'bb', 'cc']},
}
```

## Run Locally

Use the example file:

```
python run.py
```

Use custom objective/config:

```
import squirrel.optimizer as so

def objective(a, b):
    return a + b

optimizer = so.SwitchingOptimizer(config)

for _ in range(N_OPTIM_ITER):
    suggestions = optimizer.suggest(n_suggestions=N_SUGGESTIONS)
    optimizer.observe(suggestions, [objective(**suggestion) for suggestion in suggestions])

```
