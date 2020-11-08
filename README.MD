[![Build Status](https://travis-ci.com/speshori/Stats_Calculator_App_IS601.svg?branch=main)](https://travis-ci.com/speshori/Stats_Calculator_App_IS601)

# Stats Calculator 
By: Samir Peshori, Olanrewaju Oyebade

# Stats Calculator Object

## Properties:
  Result from a given function of the stats calculator

## Methods from stats_calculator class
  ### Random Functions
  #### random_num_int_generator -> generates random int w/o seed
  #### random_num_float_generator -> generates random float w/o seed
  #### random_num_seed_int_generator -> generates a random int with a seed between a range of two numbers
  #### random_num_seed_float_generator -> generates a random float with a seed between a range of two numbers
  #### list_seed_int_generator -> generates a list of N random ints w a seef between a range of numbers
  #### list_seed_float_generator -> generates a list of N random floats w a seef between a range of numbers
  #### random_item_generator -> select random item from a list
  #### random_seed_item_generator -> select random seeded item from a list
  #### select_range_generator -> select N number of items from a list w/o seed
  #### select_seed_range_generator -> select N number of items from a list w seed
  
  ### Descriptive Statistics Functions (List used for examples: [0, 1, 2, 3, 3])
  #### mean -> return mean of a list by utilizing basic functions (add, divide) from calculator class
  Equation: sum of the terms/# of terms  Answer: 1.8
  #### median -> return median of a list by utilizing basic functions (add, subtract) from calculator class
  Equation: n+1/2 (index)  Answer: 2
  #### mode -> return mode of a list 
  Equation: most frequent number. Answer: 3
  #### variance -> return variance of a list by utilizing basic functions (add, subtract, square, divide) from calculator class
  Equation: the sum of the difference of the value of one observation and the mean of all observations squared divided by number of observations minus one.  Answer: 1.7
  #### standard deviation -> return standard deviation of a list by utilizing basic functions (squareroot) from calculator class and functions from the stats_calculator class (variance)
  Equation: squareroot of the variance.  Answer: 1.304
  #### z-score -> return z-scores for each item of a list by utilizing basic functions (subtract, divide) from calculator class and functions from the stats_calculator class (standard deviation, mean)
  Equation: difference of the number and the mean of the set of numbers and that divided by the standard deviation of the set.  Answer: [-1.38, -0.613, 0.153, 0.92, 0.92]
