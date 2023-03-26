#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # a place to track the current min amount of batches possible
    batches = 0
    # check that values of available ingredients are greater than the required ingredients
    #    if so get the floor division of the ingredients and the recipe
    #        if that is smaller than current batches value set batches to newest number
    for key in recipe.keys():
        if ingredients.get(key) == None:
            return 0
        possible_batches = ingredients.get(key) // recipe.get(key)
        if possible_batches == 0:
            return 0
        elif batches == 0:
            batches = possible_batches
        elif possible_batches < batches:
            batches = possible_batches

    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
