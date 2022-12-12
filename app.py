import requests
import json

# search_word = "Greek"

# url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey=33f7af9664464e1fad151db6e46c6399&cuisine=${search_word}&number=10"

# data = '{"key": "value"}'

# headers = {
#     "Content-Type": "application/json",
#     "apikey" : "33f7af9664464e1fad151db6e46c6399"
#     }
# response = requests.get(url=url, data={}, headers=headers)
# cuisine = response.json()
# results = cuisine['results']
# #print(results)

# for recipe in results:
#     print(recipe["image"])
#     print(recipe['title'])


url = "https://api.spoonacular.com/recipes/complexSearch?"
apiKey = "33f7af9664464e1fad151db6e46c6399"
cuisine = "Italian"
number = 10

r = requests.get(f'{url}apiKey={apiKey}&cuisine=${cuisine}&number={number}')
data = r.json()
print(data)

# for i in data:
#     print(data["results"][i]['title'])

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