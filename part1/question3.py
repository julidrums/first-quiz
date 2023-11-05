################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

class MagicalOven:
    def __init__(self):
        self.ingredients = []
        self.temperature = None

    def add(self, item):
        self.ingredients.append(item)

    def freeze(self):
        self.temperature = "frozen"

    def boil(self):
        self.temperature = "boiled"

    def wait(self):
        if self.temperature:
            self.combine_ingredients()
            self.temperature = None

    def combine_ingredients(self):
        if self.temperature == "frozen":
            return "gold"
        elif self.temperature == "boiled":
            return "pizza"
        else:
            return "Unknown"

    def get_output(self):
        if self.temperature:
            result = self.combine_ingredients()
            self.temperature = None
            return result
        else:
            return "Unknown"

def make_oven():
    return MagicalOven()

def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()
