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





def get_favorites_by_user(user_id):
    """Return favorite recipes by user"""

    user_favs_list = [<FavoriteRecipe user_id=1 recipe_id=12, <FavoriteRecipe user_id=1 recipe_id=82, 
<FavoriteRecipe user_id=1 recipe_id=112, <FavoriteRecipe user_id=1 recipe_id=None, 
<FavoriteRecipe user_id=1 recipe_id=None, <FavoriteRecipe user_id=1 recipe_id=639606, 
<FavoriteRecipe user_id=1 recipe_id=639606, <FavoriteRecipe user_id=1 recipe_id=645646, 
<FavoriteRecipe user_id=1 recipe_id=639606, <FavoriteRecipe user_id=1 recipe_id=649195, 
<FavoriteRecipe user_id=1 recipe_id=660843, <FavoriteRecipe user_id=1 recipe_id=None, 
<FavoriteRecipe user_id=1 recipe_id=649225, <FavoriteRecipe user_id=1 recipe_id=715769, 
<FavoriteRecipe user_id=1 recipe_id=715424, <FavoriteRecipe user_id=1 recipe_id=1096161, 
<FavoriteRecipe user_id=1 recipe_id=716426, <FavoriteRecipe user_id=1 recipe_id=715769, 
<FavoriteRecipe user_id=1 recipe_id=795751, <FavoriteRecipe user_id=1 recipe_id=795751, 
<FavoriteRecipe user_id=1 recipe_id=651977, <FavoriteRecipe user_id=1 recipe_id=715533,
 <FavoriteRecipe user_id=1 recipe_id=715533]
    


def get_favorite_recipe_ids(user_id):
    """Return list of recipe id by user"""

    user_fav = get_favorites_by_user(user_id)

    fav_recipe_id_list =[]

    for item in user_fav:
        fav_recipe_id_list.append(item)
    
    return fav_recipe_id_list