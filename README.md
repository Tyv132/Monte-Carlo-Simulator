# Monte Carlo Simulator 

Montecarlo is a Python package that implements Monte Carlo simulations to compute the probability of certain outcomes. \
This package was created by Tyler Valentine for the Monte Carlo Simulator project at UVA School of Data Science. 

## Installation

Clone the Monte-Carlo-Simulator repository and run the following command in the directory to install montecarlo. 

```bash
pip setup.py -e . 
```

## Usage

The Die class allows for the creation of a "die" object, which contains multiple faces as specified upon instantiation. 

```python
from montecarlo import Die 

# creates a standard Die object with 6 faces with numeric values. 
faces = [1,2,3,4,5,6]
my_die = Die(faces)

# the faces can also be strings. 
faces = ['one', 'two', 'three', 'four', 'five', 'six']
my_die = Die(faces)
```




# Synopsis 

The module montecarlo contains three methods called Die, Game, and Analyzer. 


