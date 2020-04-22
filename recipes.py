# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:55:03 2020

@author: THE BEST TEAMMMMM evaaaa.... not
"""
import spoonacular as sp
api = sp.API("your_api_key_here")


#id is a number
def getrecipeinformation(ID):
    recipeInfo = api.analyze_recipe_instructions(ID, False)
    return recipeInfo.json()

def getrandomfoodjoke():
    foodJoke = api.get_a_random_food_joke()
    return foodJoke.json()

#tas refers to like desserts or vegetarian... Multiple seperate by comma String
def getrandomrecipes(tags, numRecipes):
    randomRecipe = api.get_a_random_food_joke(True, tags, numRecipes)
    return randomRecipe.json()

def searchrecipes(query):
    searchResults = api.search_recipes(query)
    return searchResults.json() 

def searchrecipesbyingredients(ingredients, fillIngredients=None, 
                              limitLicense=None, number=None, ranking=None ):
    searchResults = api.search_recipes_by_ingredients(ingredients, fillIngredients=None, 
                limitLicense=None, number=None, ranking=None)
    return searchResults.json() 

#id is a number
def summarizerecipe(ID):
    searchResults = api.summarize.recipes(ID)
    return searchResults.json() 
