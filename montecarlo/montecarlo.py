import random
import numpy as np
import pandas as pd

class Die: 
    '''
    Creates a die with n faces and weights, which can be rolled to select a face.
    Default value: 1.0 (float)     
    '''
    def __init__(self, faces):
        '''
        Input: faces (ndarray, str or floats) 
        '''
        weight = {'Weight': [1.0]*len(faces)}                                  # initializes all weights = 1
        self.__die = pd.DataFrame(weight, index = faces)                       # creates a private DataFrame for the die

    def change_weight(self, face, new_weight):
        '''
        Changes the weight of a face on the die to be the value "new_weight".
        Input: face (ndarray or list -str, int, or float), new_weight (float)
        '''
        if face in self.__die.index:
            try: 
                self.__die.loc[face] = float(new_weight)                       # changes the weight at the index "face"
            except:
                raise ValueError('The new weight must be of type float.')      # raises an error if the weight cannot be converted to a float
        else:
            raise ValueError('This face is not on the die.')                   # raises an error if the input is not a "face" on the die
    
    def roll(self, n = 1):
        '''
        Choose "n" random faces on the die.
        Input: n (int)
        Default value: 1 (int)
        Returns: n number of random faces on the die (list)
        '''      
        # chooses "n" random "faces" from the die according to the weights                                                              
        return random.choices(self.__die.index, k = n, weights = self.__die.Weight)                   

    def show(self):
        '''
        Show the current die, including the faces and their corresponding weights.
        Returns: Die (dataframe)
        '''
        return self.__die

class Game:
    '''
    Plays a game which consists of rolling one or more dice one or more times.
    '''
    def __init__(self, dice):
        '''
        Input: dice (list of Die objects)
        '''
        self.dice = dice 

    def play(self, n):
        '''
        Chooses a random face on each die "n" times and saves the results.
        Input: n (integer)
        '''
        results = []
        for n in range(n):
            roll = [Die.roll(die)[0] for die in self.dice]                     # calls the "roll" function and creates a list
            results.append(roll)                                               # of the results from "n" rolls for each die

        # save results to a private dataframe
        __columns = list(range(0,len(self.dice)))                              # defines the column names
        self.__outcome = pd.DataFrame(results, columns = __columns)            # creates a dataframe from the list of results
        self.__outcome.index = list(range(0,len(self.__outcome)))              # defines the index for the dataframe 
        self.__outcome.index.name = 'Roll'                                     # names the row index "Roll"
        self.__outcome.columns.name = 'Die'                                    # names the column index "Die"

    def show(self, form = "wide"):
        '''
        Shows the outcome of the most recent play as a dataframe in either "wide" or "narrow" form.
        Input: form ("wide" or "narrow" strings)
        Default value: "wide" (string)
        Returns: outcome (dataframe)
        '''
        if form == "wide":
            return self.__outcome                                              # returns the dataframe in wide form 
        elif form == "narrow":
            return self.__outcome.stack().to_frame("Face rolled")              # returns the dataframe in narrow form 
        else:
            raise ValueError('The form must be "wide" or "narrow"')            # raises an error if the form input is invalid

class Analyzer: 
    '''
    Takes the results of a game and returns the number of jackpots, 
    the combinations of "faces", and the "face" counts for each roll. 
    '''
    def __init__(self, game):
        '''
        Input: dice (list of Die objects)
        '''
        self.__game = game                                                     # defines game object                         
        self.__outcome = game.show()                                           # defines outcome of game 
    
    def jackpot(self): 
        '''
        Computes how many times the game resulted in all faces being identical.
        Attribute: analyzer.jackpots (dataframe)
        '''
        self.jackpots = self.__outcome.copy()                                  # creates a copy of the outcome dataframe
        count = 0                                                              # initializes the jackpot count to be zero

        for row in range(0, len(self.jackpots)):                               # steps through each row in the outcome dataframe
            if len(set(self.jackpots.loc[row])) != 1:                          # if all of the "faces" are not equal,
                self.jackpots = self.jackpots.drop([row])                      # that row is dropped from the dataframe
            else:
                count += 1                                                     # otherwise, add 1 jackpot to the total count
        return count                                                           # display the total number of jackpots

    def combo(self):
        '''
        Computes the distinct combinations of faces rolled, along with their counts.
        Attribute: analyzer.combos (dataframe) 
        '''
        # sorts the columns and saves the combinations and their counts  
        combos = self.__outcome.copy() 
        self.combos = combos.apply(lambda x: pd.Series(sorted(x)),1).value_counts().to_frame('Counts')           
                                                                      
    def face_count(self):
        '''
        Computes how many times a given "face" is rolled in each game
        Attribute: analyzer.face_counts (dataframe)
        '''
        faces = self.__game.dice[0].show().index.values.tolist()               # defines the list of "faces"
        self.face_counts = pd.DataFrame(columns = faces)                       # creates a dataframe with the "faces" as columns
        for row in range(0, len(self.__outcome)):                              # for each row in the outcome dataframe,
            add_row = self.__outcome.loc[row].value_counts().to_frame().T      # defines a row with the count of unique "faces"
            self.face_counts = pd.concat([self.face_counts, add_row], axis=0)  # adds the defined row to the face_counts dataframe
        self.face_counts = self.face_counts.fillna(0)                          # changes the face_counts NaN values to be zero