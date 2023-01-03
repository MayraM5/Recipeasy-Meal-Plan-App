"""Server for meal planning app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify, url_for
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
import requests
import json
import os
import cloudinary.uploader
import cloudinary
import random
import string
import time


app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined


SPOON_API_KEY = os.environ["SPOON_API_KEY"]

CLOUD_NAME = "dhyrymmf4"
CLOUDINARY_SECRET= os.environ["CLOUDINARY_SECRET"],
CLOUDINARY_KEY= os.environ["CLOUDINARY_KEY"]

#Homepage
@app.route('/')
def homepage():
    """Show homepage template"""

    return render_template('login_form.html') 

#Log in
@app.route("/log-in", methods=["POST"])
def log_in():
    """Process user log-in."""

    input_email = request.form.get("email")
    input_password = request.form.get("password")

    #This return user_id, fname, lname, email by input_email
    user = crud.get_user_by_email(input_email)

    #if user in db and user password vs input password match ==> log in
    if input_email == "":
        return redirect('/')

    if user and user.password == input_password:
        flash(f'Welcome back, {user.first_name}! You are now logged in.')
        session['user_id'] = user.user_id
        return redirect('/home')
        
    else:
       # flash(f'User email and/or password is incorrect. Please try again.') ##NOT DISPLAYING => displaying after logged in
        return redirect('/')

#log-out
@app.route("/log-out")
def log_out():
    """ Process user log-out """

    del session['user_id']
    flash("You have been logged out!") #displaying on the wrong page!!!!!!!!!!

    return redirect('/')  #this works!

#Create an account
@app.route("/sign-up")
def show_sign_up():
    """Display the sign up page for a new user"""

    return render_template("signup_form.html")

@app.route("/register", methods=['POST'])
def register():
    """Create new user"""
        
    email = request.form.get("email")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        #This email is already registered.=> homepage to log in
        return redirect('/') #this works

    else:           
        user = crud.create_user(first_name, last_name, email, password)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.user_id
        flash(f'Welcome {user.first_name}! Your account was succesfully created.')
        return redirect("/home") #this works!


@app.route("/home")
def home():

    return render_template('home.html', SPOON_API_KEY=SPOON_API_KEY)

#Add recipe to favorites
@app.route("/api/fav-recipe", methods=['POST'])  #==> FLASH MSG NOT DISPLAY
def get_recipe_id():

    logged_in_user_id = session.get("user_id")
    recipe_id = request.json.get("recipe_Id")

    #Get user list favorite recipe ids
    fav_list = crud.get_favorite_recipe_ids(logged_in_user_id)
  
    #check if user is logged in:
    if logged_in_user_id is None:
        flash("You must log in to add to Favorites") 
        return redirect('/')
    
    else:
        #check if recipe id is in db
        if recipe_id in fav_list:
            flash(f"Its already added")
            return json.dumps({'fail': True}) 

        # #check if recipe id is in fav, if not add
        else:
            recipe_id_to_save = crud.create_fav(logged_in_user_id, (recipe_id))
            db.session.add(recipe_id_to_save)
            db.session.commit()
            flash("Great! This recipe has been added to Favorites")

            return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

#Display favorites
@app.route("/favorites")
def display_fav_recipes():

    logged_in_user_id = session.get("user_id")
    fav_list = crud.get_favorite_recipe_ids(logged_in_user_id)

    #Convert each element from list to string 
    ids = ','.join(str(id) for id in fav_list)

    #NEED TO HIDE APIKEY
    url = 'https://api.spoonacular.com/recipes/informationBulk?' 
    params = {'apiKey' : SPOON_API_KEY,
            'includeNutrition': False,
            'ids' : ids,
            }

    response = requests.get(url, params)
    data = response.json()
   # print(f'DATA RESPONSE {data}')
    fav_recipes = []

    for recipe in data:
        id = recipe["id"]
        title = recipe['title']
        try:
            image = recipe["image"]
        except KeyError:
            image = None

        element = {'id': id, 'title': title, 'image': image}

        fav_recipes.append(element)

    return render_template("favorites.html", favorite_recipes=fav_recipes)

#REMOVE RECIPE FROM FAVORITE RECIPES
@app.route("/remove-fav", methods=["POST"])
def remove_favorite():
    """Process to remove recipe from favorites."""

    logged_in_user_id = session.get("user_id")
    recipe_id = request.json.get("recipe_id")

    fav_to_delete = crud.get_fav_by_user_and_recipe(logged_in_user_id, recipe_id)

    db.session.delete(fav_to_delete)
    db.session.commit()

    return redirect("/favorites")

# @app.route("/add-meal", methods=["POST"])
# def add_fav_to_meal_plan():

#     logged_in_user_id = session.get("user_id")
#     recipe_id = request.json.get("recipe_id")


#==============DISPLAY RECIPE DETAILS=====================
@app.route("/recipe-details-<recipe_id>", methods=["GET","POST"]) 
def recipe_details(recipe_id):

    # recipe_id = request.json.get("recipe_Id")

    url = 'https://api.spoonacular.com/recipes/informationBulk?'
    params = {'apiKey' : SPOON_API_KEY,
                'ids' : recipe_id,
                }
    # print("*"*20)
    # print(recipe_id)

    response = requests.get(url, params)
    data = response.json()
    # print(f'data: {data}')

    for recipe in data:
        id = recipe["id"]
        title = recipe['title']
        image = recipe["image"]
        # try:
        #     instructions = recipe["instructions"].split(".")
        # except AttributeError:
        #     try:
        #         instructions = recipe['summary'].split(".")
        #     except (KeyError, AttributeError):
        #         instructions = None
        try:
            raw_instructions = recipe["instructions"]

            # if recipe["instructions"] is empty or None, use recipe["summary"]
        except KeyError:
            try:
                raw_instructions = recipe["summary"]
            except KeyError:
                raw_instructions = None
        #Remove extra tags
        tags_to_remove = ['<ol>', '</ol>', '<li>', '</li>', '<span>', '</span>', '<p>', '</p>']
        try:
            for tag in tags_to_remove:
                raw_instructions = raw_instructions.replace(tag, '')
            #Convert in list to display every step in a row
            instructions = raw_instructions.split('.')
        except AttributeError:
            instructions = None

        #Filter ingredients and add to list just what I need now
        ingredients = recipe['extendedIngredients']
        ingredients_list = []
        for item in ingredients:
            name = item['name']
            amount = item['amount']
            unit = item['unit']

            elements = {'name': name, 'amount' : amount, "unit" : unit}
            ingredients_list.append(elements)
    # print(f'instructions: {instructions}')

    return render_template("recipe_details.html", title=title, instructions=instructions, 
                            ingredients = ingredients_list, image = image)

#Add recipe to meal plan:
# @app.route("/api/meal-plan", methods=['POST'])  #==> FLASH MSG NOT DISPLAY
# def get_recipe():

#     logged_in_user = session.get("user_id")
#     recipe_id = request.json.get("meal_plan_Id")

#     #Get user meal plan recipe ids
#     meal_plan_list = crud.get_meal_plan_recipe_ids(logged_in_user)
    
#     #check if user is logged in:
#     if logged_in_user is None:
#         flash("You must log in to add to Favorites") 
#         return redirect('/')
    
#     else:
#         #check if recipe id is in db
#         if recipe_id in meal_plan_list:
#             flash(f"Its already added")
#             return json.dumps({'fail': True}) 

#         #check if recipe id is in meal plan, if not add
#         else:
#             user = crud.get_user_by_id(logged_in_user)
#             recipe_id = crud.create_meal_plan(user, (recipe_id))
#             db.session.add(recipe_id)
#             db.session.commit()
#             flash("Great! This recipe has been added to Favorites")

#             return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

#===============================================================================
#ADD RECIPE TO MP AND GROCERY ITEMS TO GROCERIES
@app.route("/api/meal-plan", methods=['POST'])  #==> FLASH MSG NOT DISPLAY
def get_recipe():

    logged_in_user_id = session.get("user_id")
    recipe_id = request.json.get("recipe_Id") 
    
    #Get user meal plan recipe ids
    meal_plan_list = crud.get_meal_plan_recipe_ids(logged_in_user_id)
    
    #check if user is logged in:
    if logged_in_user_id is None:
        flash("You must log in to add to Favorites") 
        return redirect('/')
    
    else:
        #check if recipe id is in db
        if recipe_id in meal_plan_list:
            flash(f"Its already added")
            return json.dumps({'fail': True}) 

        #check if recipe id is in meal plan, if not add
        else:
            meal_plan = crud.create_meal_plan(logged_in_user_id, (recipe_id))
            db.session.add(meal_plan)
            db.session.commit()
            flash("Great! This recipe has been added to Favorites")
            

            url = 'https://api.spoonacular.com/recipes/informationBulk?'
            params = {'apiKey' : SPOON_API_KEY,
                        'ids' : recipe_id,
                        }
            # print("*"*20)

            response = requests.get(url, params)
            data = response.json()
            #
            recipe_data = None
            #Find our recipe from list
            for recipe in data:
                if str(recipe["id"]) == recipe_id:
                    recipe_data = recipe

            for ingredient in recipe_data["extendedIngredients"]:
                ingredient_name =(ingredient["name"])
                unit = (ingredient["unit"])
                amount = (ingredient["amount"])
                category = (ingredient["aisle"])

                grocery_item = crud.create_grocery_item(logged_in_user_id, recipe_id, category, ingredient_name, amount, unit)
                
                db.session.add(grocery_item)
                db.session.commit()

            return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


# #Display meal plan
@app.route("/meal-plan")
def display_meal_plan():

    logged_in_user_id = session.get("user_id")
    meal_plan = crud.get_meal_plan_recipe_ids(logged_in_user_id)

    #Convert each element from list to string 
    ids = ','.join(str(id) for id in meal_plan)

    url = 'https://api.spoonacular.com/recipes/informationBulk?'
    params = {'apiKey' : SPOON_API_KEY,
            'includeNutrition': False,
            'ids' : ids,
            }

    response = requests.get(url, params)
    data = response.json()
   # print(f'DATA RESPONSE {data}')
    meal_plan_recipes = []

    for recipe in data:
        id = recipe["id"]
        title = recipe['title']
        try:
            image = recipe["image"]
        except KeyError:
            image = None

        element = {'id': id, 'title': title, 'image': image}

        meal_plan_recipes.append(element)

    return render_template("mealplan.html", meal_plan_recipes=meal_plan_recipes)

# #REMOVE RECIPE FROM MEAL PLAN & INGREDIENTS FROM DB
@app.route("/remove-meal-plan", methods=["POST"])
def delete_meal_plan():
    """Process to remove recipe from meal plan."""

    logged_in_user = session.get("user_id")
    recipe_id = request.json.get("recipe_id")
    #when user remove a recipe_id from the meal plan, 
    #it will also remove ingredients attached to that recipe
    #remove recipe from meal plan 
    mp_to_delete = crud.get_meal_plan_by_user_and_recipe(logged_in_user, recipe_id)
    db.session.delete(mp_to_delete)
    
    #remove ingredients
    grocery_items_to_delete = crud.get_grocery_item_by_user_and_recipe(logged_in_user, recipe_id)
    for item in grocery_items_to_delete:
        db.session.delete(item)

    db.session.commit()

    return redirect("/meal-plan")

# # @app.route("/meal-plan")
# # def get_meal_plan():

# #     return render_template("mealplan.html")

#Display grocery items total list:
@app.route("/groceries")
def display_grocery_items():
    """Process to display a list of grocery"""

    logged_in_user = session.get("user_id")
    total_grocery = crud.get_total_grocery_list(logged_in_user)

    return render_template("groceries.html", total_grocery=total_grocery) #, name=name, amount=amount, unit=unit)

#############NEW FEATURE ###########################################
@app.route("/myrecipes")
def my_recipes():

    logged_in_user = session.get("user_id")
    recipes_data = crud.get_my_recipes(logged_in_user)

    # my_recipes = []
    # for recipe in recipes_data:
    #     recipe_id = recipe["recipe_id"]
    #     title = recipe['title']
    #     # try:
    #     #     image = recipe["image"]
    #     # except KeyError:
    #     #     image = None

    #     element = {'recipe_id': recipe_id, 'title': title}

    #     my_recipes.append(element)

    return render_template("my_recipes.html", my_recipes=my_recipes)

    

@app.route('/render-page', methods=['POST'])
def render_page():
  return render_template('create_recipe.html')


@app.route('/create-recipe', methods=['POST'])
def create_recipe():

    logged_in_user_id = session.get("user_id")

    #Generate random recipe id with letter to avoid matching with API recipe ID
    recipe_id = (''.join(random.choices(string.ascii_letters, k=6)))

    # ## cloudinary is not working!!!!
    # my_file = request.files["my_file"]
    # my_file = request.files.get("my_file")

    # if my_file:
    #     result = cloudinary.uploader.upload(my_file.stream,
    #                 api_key=CLOUDINARY_KEY,
    #                 api_secret=CLOUDINARY_SECRET,
    #                 cloud_name=CLOUD_NAME)

    #     image = result['secure_url']
    # else:
    #     image = None

    # print(image)
    title = request.form['name']    
    instructions = request.form['instructions']

    #get ingredient by column
    ingredients = request.form.getlist('ingredient')
    units_list = request.form.getlist('unit')
    amounts = request.form.getlist('quantity')
    categories = request.form.getlist('category')

    #zip list to convert new list in a recipe ingredient data
    ingredient_data = list(zip(ingredients, amounts, units_list, categories))
    print(ingredient_data)
    for data in ingredient_data:
        ingredient_name = data[0]
        amount = data[1]
        units = data[2]
        category = data[3]

    # save the data to the database
        recipe = crud.create_my_recipe(logged_in_user_id, recipe_id, title, instructions, ingredient_name, amount, units, category)
        db.session.add(recipe)
        db.session.commit() 
    flash('Recipe saved successfully!')
    
    return render_template('my_recipes.html')


if __name__ == "__main__":
    connect_to_db(app, "mealplanning")
    app.run(host="0.0.0.0", port=5000, debug=True)