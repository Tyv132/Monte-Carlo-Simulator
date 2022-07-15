# Monte Carlo Simulator 

Montecarlo is a Python package that implements Monte Carlo simulations to compute the probability of certain outcomes. This package was created by Tyler Valentine for the Monte Carlo Simulator project at UVA School of Data Science. 

## Installation

Clone the Monte-Carlo-Simulator repository and run the following command in the directory to install montecarlo. 

```bash
pip setup.py -e . 
```
Montecarlo requires prior installation of the following packages: 
[NumPy](https://numpy.org/install/) \
[Pandas](https://pandas.pydata.org/getting_started.html)


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

The Game class will create a Game object of dice that can be rolled multiple times. 
```python
from montecarlo import Game

# creates a Game object with two dice of the from die1
dice = [die1, die1]
game1 = Game(dice, 10)
```
The "play" method will roll the dice "n" times. 
```python
# rolls the dice 10 times 
game1.play(10)
```
The "show" method will show the results of the game as either a "wide" or "narrow" table. 
```python
# display the result of the game as a wide table
game1.show(form = "wide")
```
|   Die  |   0 | 1     |
|-------:|----:|:------|
|   Roll |     |       |
|      0 |   6 | 6     |
|      1 |   1 | 5     |
|      2 |   4 | 1     |
|      3 |   4 | 4     |
|      4 |   1 | 1     |

### Analyzer
The Analyzer class will count the total number of times all dice revealed the same face and show all unique combinations of faces. 
```python
from montecarlo import Analyzer

# creates an Analyzer object from game1
analyzer1 = Analyzer(game1)
```
The "jackpot" method will show the number of times all dice showed the same face for the same roll number.
```python
# prints the number of jackpots.
analyzer1.jackpot()

# shows a dataframe with the faces and roll number for each jackpot
analyzer1.jackpots
```
|   Die  |   0 |   1 |
|-------:|----:|----:|
|   Roll |     |     |
|      0 |   6 |   6 |
|      3 |   4 |   4 |
|      4 |   1 |   1 |

To show the unique combinations of results and their counts, the combo method can be used. 
```python
# finds the distinct combinations of results and their counts.
analyzer1.combo()

# shows a dataframe with the combinations and the count number for each combo.
analyzer1.combos
```
|        |     |Counts|
|-------:|----:|----: |
|      0 |   1 |      |
|      1 |   1 |   1  |
|        |   4 |   1  |
|        |   5 |   1  |
|      4 |   4 |   1  |
|      6 |   6 |   1  |

The "face_count" method will display how many times a given face is shown for each roll. 
```python
# call the face_count function
analyzer1.face_count()

# display the face counts
analyzer1.face_counts
```
|    |   1 |   2 |   3 |   4 |   5 |   6 |
|---:|----:|----:|----:|----:|----:|----:|
|  0 |   0 |   0 |   0 |   0 |   0 |   2 |
|  1 |   1 |   0 |   0 |   0 |   1 |   0 |
|  2 |   1 |   0 |   0 |   1 |   0 |   0 |
|  3 |   0 |   0 |   0 |   2 |   0 |   0 |
|  4 |   2 |   0 |   0 |   0 |   0 |   0 |

## API Description
### Die class 
```
Creates a die with n faces and weights, which can be rolled to select a face.
Default value: 1.0 (float)
```
Methods:
- init(faces)
```
Input: faces (ndarray, str or floats)
```
- change_weight(face, new_weight)
```
Changes the weight of a face on the die to be the value "new_weight".
Input: face (ndarray or list -str, int, or float), new_weight (float)
```
- roll(n)
```
Choose "n" random faces on the die.
Input: n (int)
Default value: 1 (int)
Returns: n number of random faces on the die (list)
```
- show()
```
Show the current die, including the faces and their corresponding weights.
Returns: Die (dataframe)
```

### Game Class
```
Plays a game which consists of rolling one or more dice one or more times.
```
Methods:
- init(dice)
```
Input: dice (list of Die objects)
```
- play(n)
```
Chooses a random face on each die "n" times and saves the results.
Input: n (integer)
```
- show()
```
Shows the outcome of the most recent play as a dataframe in either "wide" or "narrow" form.
Input: form ("wide" or "narrow" strings)
Default value: "wide" (string)
Returns: outcome (dataframe)
```
### Analyzer Class
```
Takes the results of a game and returns the number of jackpots, the combinations of "faces", and the "face" counts for each roll.
```
Methods:
- init(dice)
```
Input: dice (list of Die objects)
```
- jackpot()
```
Computes how many times the game resulted in all faces being identical.
Attribute: analyzer.jackpots (dataframe)
```
- combo()
```
Computes the distinct combinations of faces rolled, along with their counts.
Attribute: analyzer.combos (dataframe)
```
- face_count()
```
Computes how many times a given "face" is rolled in each game
Attribute: analyzer.face_counts (dataframe)
```

## Manifest 
```
montecarlo package
    init.py
    montecarlo.py
.gitignore
LICENSE
README.md
montecarlo_demo.ipynb
montecarlo_tests.py
montecarlo_tests.txt
setup.py 
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License 
[MIT](https://choosealicense.com/licenses/mit/)

