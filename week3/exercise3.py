"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    """


      check = False

      lower = not("enter the lower bound")
      while check is False:
        try:
          upper = int(raw_input("enter the upper bound"))
          if upper > (lower+1):
            print("you need to guess" + 
                  "between {} and {}".format(lower, upper))
            check = True
          elif upper == (lower+1):
            print("numbers too close")
          else:
            print("{} is not higher than {}, try again".format(upper, lower))
      
        except:
          print("not an integer")


      actual = random.randint(lower, upper)
      guessed = False

      while not guessed:
        try:
          guessed == int(raw_input("have a guess: "))
          if guessed == actual:
            print("{} was the answer!".format(actual))
            guessed = True
          elif guessed <= lower:
            print("no, {} is too low to be valid".format(guessed))
          elif guessed >= upper :
            print("no, {} is too high to be valid".format(guessed))
          elif guessed > actual:
            print("guess lower!")
          elif guessed < actual:
            print("guess higher!")
        except:
          print("not an integer")

      return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!
"""

if __name__ == "__main__":
    print(advancedGuessingGame())
