#!/usr/bin/python

import math

# max = 0
# loop for each value for key
#   temp = available / recipe
#   if temp == 0, return 0
#   if temp < max, max = temp
#   else, max = temp


def recipe_batches(recipe, ingredients):
    batches = []
    for k in recipe:
        if k not in ingredients :
            return 0
        batch = math.floor(ingredients[k] / recipe[k])
        if batch == 0:
            return 0
        else:
            batches.append(batch)        
    return min(batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
