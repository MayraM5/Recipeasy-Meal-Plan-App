import requests
import json

# url_work = 'https://api.spoonacular.com/recipes/complexSearch?apiKey=33f7af9664464e1fad151db6e46c6399&cuisine=$italian'
# url = "https://api.spoonacular.com/recipes/complexSearch?"
# params = { 'apiKey' : '33f7af9664464e1fad151db6e46c6399',
#             'fillIngredients' : True,
#             'instructionsRequired' : True,
#             'cuisine' : True,
#             'number' : 2
#         }

# url = 'https://api.spoonacular.com/recipes/informationBulk?'
# params = {'apiKey' : '33f7af9664464e1fad151db6e46c6399',
#             'includeNutrition': False,
#             'ids' : '649195, 715424, 716426'
#             }

# response = requests.get(url, params)
# data = response.json()
# results = []

# for recipe in data:
#     id = recipe["id"]
#     title = recipe['title']
#     image = recipe["image"]
#     cuisine = recipe["cuisines"]

#     element = {'id': id, 'title': title, 'image': image, 'cuisines': cuisine}

#     results.append(element)

# print(results)

# for recipe in results:
#     print(recipe['title'])
#     print(recipe['image'])



#-----------------------TRYING TO GET DATA FROM Python, it works on app.py file not here
#     search_recipe = request.form.get("search_recipe")

#     url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey=33f7af9664464e1fad151db6e46c6399&cuisine=${search_recipe}&number=10"

#     data = '{"key": "value"}'

#     headers = {
#         "Content-Type": "application/json",
#         "apikey" : "33f7af9664464e1fad151db6e46c6399"
#         }
#     response = requests.get(url=url, data={}, headers=headers)
#     cuisine = response.json()
# #    # results = cuisine['results']



# def play_api():

#     url = 'https://api.spoonacular.com/recipes/informationBulk?'
#     params = {'apiKey' : 'a2bcd060e3b446968f90d3b2639acae4',
#                 'ids' : 795751,
#                 }

#     response = requests.get(url, params)
#     data = response.json()
#   #  print(data[0]['id'])
#     instructions_recipe = []

#     for recipe in data:
#         id = recipe["id"]
#         title = recipe['title']
#         image = recipe["image"]
#         instructions = recipe["instructions"].split(".")

#         element = {'id': id, 'title': title, 'image': image, "instructions" : instructions}

#         instructions_recipe.append(element) 

#         ingredients = recipe['extendedIngredients']
#         ingredients_list = []
#         for item in ingredients:
#             name = item['name']
#             amount = item['amount']
#             unit = item['unit']

#             elements = {'name': name, 'amount' : amount, "unit" : unit}
#             ingredients_list.append(elements)

#         for key in instructions_recipe:
#             for item in instructions:
#                 print(item)

#     return f'This are the instructions: {instructions_recipe}...... this are ingredients: {ingredients_list}'



        

# #     #return(instructions_recipe)
# # def play_api():
# #     url ='https://api.spoonacular.com/recipes/715497/information?&apiKey=a2bcd060e3b446968f90d3b2639acae4'

# #     response = requests.get(url)
# #     data = response.json()
# #     print(data)
# #     print('*'*20)
  

# #     instructions_recipe = []

# #     for recipe in data:
# #         id = recipe["id"]
# #         title = recipe['title']
# #         image = recipe["image"]
# #         instructions = recipe["instructions"]

# #         element = {'id': id, 'title': title, 'image': image, "instructions" : instructions}
# #         instructions_recipe.append(element) 

# #     for recipe in data:
# #         ingredients = recipe['extendedIngredients']
        
# #         ingredients_list = []
# #         for item in ingredients:
# #             name = item['name']
# #             amount = item['amount']
# #             unit = item['unit']

# #             elements = {'name': name, 'amount' : amount, "unit" : unit}
# #             ingredients_list.append(elements)
# #     print(instructions_recipe)
# #     print('*'*20)
# #     print(ingredients_list)