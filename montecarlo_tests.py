import unittest
import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal
from montecarlo import Die, Game, Analyzer

class MontecarloTestSuite(unittest.TestCase):
    '''
    Tests the classes containted in the module "montecarlo". 
    '''
    def test_1_change_weight(self):
        '''
        Tests the Die.change_weight() function.
        '''
        # create die instance
        die = Die([1,2,3,4,5,6])
        # change weight
        die.change_weight(1,3)
        # check
        actual = die.show()
        expected = pd.DataFrame({'Weight': [3.0,1.0,1.0,1.0,1.0,1.0]}, \
                                   index = [1,2,3,4,5,6])
        pd.testing.assert_frame_equal(actual, expected) 

    def test_2_roll(self):
        '''
        Tests the Die.roll() function. 
        '''
        # create die instance
        die = Die([1,2,3,4,5,6])
        # roll
        roll = die.roll()
        # check
        actual = 1 <= roll[0] <= 6
        message = "Test value is not True."
        self.assertTrue(actual, message)

    def test_3_show(self):
        '''
        Tests the Die.show() function. 
        '''
        # create die instance
        die = Die([1,2,3,4,5,6])
        # check 
        actual = die.show()
        expected = pd.DataFrame({'Weight': [1.0,1.0,1.0,1.0,1.0,1.0]}, index = [1,2,3,4,5,6])
        pd.testing.assert_frame_equal(actual, expected)

# GAME TESTS 
    def test_4_play(self):
        '''
        Tests the Game.play() function. 
        '''
        # create game instance
        die1 = Die([1,2,3,4,5,6])
        die2 = Die([1,2,3,4,5,6])
        game = Game([die1, die2])
        # play
        game.play(3)
        result = game.show()
        # check 
        actual = np.shape(result.values)
        expected = (3,2) 
        self.assertEqual(actual, expected)

    def test_5_show(self): 
        '''
        Tests the Game.show() function. 
        '''
        # create game instance
        die1 = Die([1,2,3,4,5,6])
        die2 = Die([1,2,3,4,5,6])
        game = Game([die1, die2])
        game.play(5)
        result = game.show()
        # check 
        actual = np.shape(result.values)
        expected = (5,2)
        self.assertEqual(actual, expected)

# ANALYZER TESTS 
    def test_6_jackpot(self):
        '''
        Tests the Analyzer.jackpot() function. 
        '''
        # create analyzer instance 
        die1 = Die([1,2,3,4,5,6])
        die2 = Die([1,2,3,4,5,6])
        game = Game([die1, die2])
        game.play(50)
        analyzer = Analyzer(game)
        # find jackpots 
        analyzer.jackpot()
        jackpots = analyzer.jackpots
        list = jackpots.values.tolist()
        # check 
        actual = 0
        for i in range(0,len(list)):        
            if all(x == list[i][0] for x in list[i]) == True:
                actual += 1 
        expected = len(list)
        self.assertEqual(actual, expected) 

    def test_7_combo(self):
        '''
        Tests the Analyzer.combo() function.
        '''
        # create analyzer instance
        die1 = Die([1,2,3,4,5,6])
        die2 = Die([1,2,3,4,5,6])
        game = Game([die1, die2])
        game.play(50)
        analyzer = Analyzer(game) 
        # find combos
        analyzer.combo()
        combos = analyzer.combos
        list = combos.index.tolist()
        # check 
        actual = sorted(set(item for item in list))
        expected = sorted(list)
        self.assertEqual(actual, expected) 

    def test_8_face_count(self):
        '''
        Tests the Analyzer.face_count() function. 
        '''
        # create analyzer instance
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        game = Game([die1, die2])
        game.play(10)
        analyzer = Analyzer(game)
        # find face_count
        analyzer.face_count()
        list = analyzer.face_counts.values
        # check
        actual = 0 
        for i in range(0,len(list)):        
            if sum(list[i]) == 2:
                actual += 1 
        expected = len(list)
        self.assertEqual(actual, expected) 

if __name__ == '__main__':
    unittest.main(verbosity=3)