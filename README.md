# Monte Carlo Simulator 

Montecarlo is a Python package that implements Monte Carlo simulations to compute the probability of certain outcomes. \
This package was created by Tyler Valentine for the Monte Carlo Simulator project at UVA School of Data Science. 

## Installation

Clone the Monte-Carlo-Simulator repository and run the following command in the directory to install montecarlo. 

```bash
pip setup.py -e . 
```

## Usage

### Die 

The Die class allows for the creation of a "die" object, which contains multiple faces as specified when instantiated. 

```python
from montecarlo import Die 

# creates a standard Die object with 6 faces with numeric values. 
faces = [1,2,3,4,5,6]
my_die = Die(faces)

# the faces can also be strings. 
faces = ['one', 'two', 'three', 'four', 'five', 'six']
my_die = Die(faces)
```
By default, the weights for each face on the die are set to 1.0. \
These weights can be changed using the "change_weight" method. 

```python
from montecarlo import Die 

# changes the face "6" to have a weight of 5.0. 
my_die.change_weight(6, 5.0) 
```
The "roll" method can be used to choose "n" random faces from the faces on the die according to the probability weights for each face.

```python
from montecarlo import Die 

# choose 5 random values from the die. 
my_die.roll(5)
```
The "show" method can show the faces and corresponding probability weights for a die. 
```python
from montecarlo import Die 

# display my_die 
my_die.show()
```
|    |   Weight |
|---:|---------:|
|  1 |      1.0 |
|  2 |      1.0 |
|  3 |      1.0 |
|  4 |      1.0 |
|  5 |      1.0 |
|  6 |      5.0 |



# Synopsis 

The module montecarlo contains three methods called Die, Game, and Analyzer. 


