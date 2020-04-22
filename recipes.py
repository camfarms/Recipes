# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:55:03 2020

@author: THE BEST TEAMMMMM evaaaa.... not
"""
import spoonacular as sp
api = sp.API("your_api_key_here")


def searchrecipesbyingredients(ingredients, fillIngredients=None, 
                              limitLicense=None, number=None, ranking=None ):
    searchResults = api.search_recipes_by_ingredients(ingredients, fillIngredients=None, 
                limitLicense=None, number=None, ranking=None )
    data = searchResults.json()
    return data
    

def getfoodjoke():
    foodJoke = api.get_a_random_food_joke()
    return foodJoke.json()