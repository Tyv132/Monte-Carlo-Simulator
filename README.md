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
faces1 = [1,2,3,4,5,6]
die1 = Die(faces)

# the faces can also be strings. 
faces2 = ['one', 'two', 'three', 'four', 'five', 'six']
die2 = Die(faces)
```
By default, the weights for each face on the die are set to 1.0. \
These weights can be changed using the "change_weight" method. 

```python
# changes the face "6" to have a weight of 5.0. 
die1.change_weight(6, 5.0) 
```
The "roll" method can be used to choose "n" random faces from the faces on the die according to the probability weights for each face.

```python
from montecarlo import Die 

# choose 5 random values from the die. 
die1.roll(5)
```
The "show" method can show the faces and corresponding probability weights for a die. 
```python
from montecarlo import Die 

# display die_1
die1.show()
```
|    |   Weight |    
|---:|---------:|
|  1 |      1.0 |
|  2 |      1.0 |
|  3 |      1.0 |
|  4 |      1.0 |
|  5 |      1.0 |
|  6 |      5.0 |

### Game 

The Game class will create a Game object of dice that can be rolled multiple times. \
```python
from montecarlo import Game

# creates a Game object 
dice = [die1, die2]
game1 = Game(dice, 10)
```
The "play" method will roll the dice "n" times. 
```python
# rolls the dice 10 times 
game1.play(10)
```
The "show" method will show the results of the game. 
```python
# display the result of the game
game1.show()
```
|   Roll |   0 | 1     |
|-------:|----:|:------|
|      0 |   1 | two   |
|      1 |   6 | three |
|      2 |   1 | four  |
|      3 |   3 | four  |
|      4 |   5 | two   |


# Synopsis 

The module montecarlo contains three methods called Die, Game, and Analyzer. 


