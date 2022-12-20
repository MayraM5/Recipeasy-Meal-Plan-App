import requests
import json
import crud


def practice():
    id = 511728

    url = 'https://api.spoonacular.com/recipes/511728/information?'
    params = {'apiKey' : '33f7af9664464e1fad151db6e46c6399',
                }
    print("*"*20)

    response = requests.get(url, params)
    data = response.json()
    
    print(data)

    # for ingredient in data["extendedIngredients"]:
    #     print(ingredient["name"])
    #     print(ingredient["unit"])
    #     print(ingredient["amount"])