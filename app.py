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

# response = requests.get(url, params)
# data = response.json()
# results = data['results']

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
#    # results = cuisine['results']