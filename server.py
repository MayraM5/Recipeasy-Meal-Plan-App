"""Server for meal planning app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
from functools import wraps
from jinja2 import StrictUndefined
import requests
import crud
import json
import os
import random
import cloudinary.uploader
import helpers


app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined


SPOON_API_KEY = os.environ["SPOON_API_KEY"]

CLOUD_NAME = "dhyrymmf4"
CLOUDINARY_SECRET= os.environ["CLOUDINARY_SECRET"]
CLOUDINARY_KEY= os.environ["CLOUDINARY_KEY"]


#=======================INITAL PAGE============================#
@app.route('/')
def homepage():
    """Display login template."""

    return render_template('login_form.html') 

#========================LOG IN================================#
@app.route("/log-in", methods=["POST"])
def log_in():
    """Process user log-in."""

    input_email = request.form.get("email")
    input_password = request.form.get("password")

    #This return user_id, fname, lname, email by input_email
    user = crud.get_user_by_email(input_email)
    
    #if user in db and user password vs input password match ==> log in
    if input_email == "":
        flash("Please enter an email and password to log in", 'alert alert-danger')
        return redirect('/')
    
    elif not user or input_password != user.password:
        flash("The email or password you entered is incorrect.", 'alert alert-danger')
        return redirect('/')

    elif user and user.password == input_password:
        flash(f"Welcome back, {user.first_name}!", 'alert alert-success')
        session['user_id'] = user.user_id
        return redirect('/home')
        
    else:
        return redirect('/')

#=======================LOG OUT================================#
@app.route("/log-out")
def log_out():
    """Process user log-out."""

    del session['user_id']
    flash("You have been logged out!", 'alert alert-success') 

    return redirect('/')  

#=====================CREATE AN ACCOUNT========================#
@app.route("/sign-up")
def show_sign_up():
    """Display sign up template for a new user."""

    return render_template("signup_form.html")


@app.route("/register", methods=['POST'])
def register():
    """Create new user."""
        
    email = request.form.get("email")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        flash('This email is already registered. Please log in', 'alert alert-danger')
        return redirect('/')

    else:           
        user = crud.create_user(first_name, last_name, email, password)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.user_id
        flash(f'Welcome {user.first_name}! Your account was succesfully created.', 'alert alert-success')
        return redirect("/home")

#=====================HOMEPAGE=================================#
@app.route("/home")
def home():
    """Display homepage."""

    logged_in_user_id = session.get("user_id")

    if logged_in_user_id == None:
        return render_template('404.html'), 404

    else:

        url = 'https://api.spoonacular.com/recipes/random' 
        params = {'apiKey' : SPOON_API_KEY,
            'limitLicense': True,
            'tags': 'vegan',
            'number' : 12, #number of recipe to return
            }

        response = requests.get(url, params)
        data = response.json()
        recipe_data = data['recipes']

        random_recipes = []
        for recipe in recipe_data:
            id = recipe["id"]
            title = recipe['title']
            try:
                image = recipe["image"]
            except KeyError:
                image = None

            element = {'id': id, 'title': title, 'image': image}

            random_recipes.append(element)

        return render_template('home.html', random_recipes=random_recipes, SPOON_API_KEY=SPOON_API_KEY)

#=====================ADD RECIPES TO FAVORITES=================#
@app.route("/api/fav-recipe", methods=['POST']) 
def add_recipe_to_favorites():
    """Process to add recipe to favorites."""

    logged_in_user_id = session.get("user_id")
    recipe_id = request.json.get("recipe_Id")
   
    #Get user list of favorite recipe ids
    fav_list = crud.get_favorite_recipe_ids(logged_in_user_id)

    try:
        recipe_id = str(recipe_id)
    except:
        pass
    #check if recipe id is in db    
    if recipe_id in fav_list:
        return jsonify({'status': 'error', 'reason': 'duplicate'}), 400

    #if recipe id no in fav => add it
    else:
        recipe_id_to_save = crud.create_fav(logged_in_user_id, (recipe_id))
        db.session.add(recipe_id_to_save)
        db.session.commit()

        return jsonify({'status': 'success'})

#=========================DISPLAY FAVORITES===================#
@app.route("/favorites")
def get_fav_recipes():
    """Process user's favorite recipes."""

    logged_in_user_id = session.get("user_id")
    fav_list = crud.get_favorite_recipe_ids(logged_in_user_id)

    if logged_in_user_id == None:
        return render_template('404.html'), 404
 
    else:        
        #Convert each element from list to string 
        ids = ','.join(str(id) for id in fav_list)

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

#Remove recipes from fav==>Change to delete method (future)===#
@app.route("/remove-fav", methods=["POST"])
def remove_recipe_from_favorites():
    """Process to remove recipe from favorites."""

    logged_in_user_id = session.get("user_id")
    recipe_id = request.json.get("recipe_id")

    fav_to_delete = crud.get_fav_by_user_and_recipe(logged_in_user_id, recipe_id)
    
    db.session.delete(fav_to_delete)
    db.session.commit()

    return redirect("/favorites")

#========================DISPLAY RECIPE DETAILS===============#
@app.route("/recipe-details-<recipe_id>", methods=["GET","POST"]) 
def get_recipe_details(recipe_id):
    """Process recipe details by recipe id."""
    
    logged_in_user_id = session.get("user_id")
    #check if recipe is in database (created by user)
    if recipe_id.startswith('cook'):

        db_recipe = helpers.get_database_recipe(logged_in_user_id, recipe_id)
        return render_template("recipe_details.html", recipe=db_recipe)

    else:
        spoon_recipe = helpers.get_spoonacular_recipe(recipe_id)
        return render_template("recipe_details.html", recipe=spoon_recipe)

#=========ADD RECIPE TO MP AND GROCERY ITEMS TO GROCERIES=====#
@app.route("/api/meal-plan", methods=['POST'])  
def add_recipe_to_meal_plan():
    """Process to add recipe to meal_plans and items to grocery_items. """

    logged_in_user_id = session.get("user_id")
    recipe_id = request.json.get("recipe_Id") 

    #Get user meal plan recipe ids
    meal_plan_list = crud.get_meal_plan_recipe_ids(logged_in_user_id)

    try:
        recipe_id = str(recipe_id)
    except:
        pass

    if recipe_id in meal_plan_list:
        return jsonify({'status': 'error', 'reason': 'duplicate'}), 400

    else:
        meal_plan = crud.create_meal_plan(logged_in_user_id, (recipe_id))
        db.session.add(meal_plan)
        db.session.commit()
        
        #get ingredients for recipe created by user from database
        if recipe_id.startswith('cook'):
            ingredient_data = crud.get_recipe_ingredients(recipe_id)
            for ingredient in ingredient_data:
                ingredient_name = ingredient.ingredient_name
                unit = ingredient.units
                amount = ingredient.amount
                category = ingredient.category

                grocery_item = crud.create_grocery_item(logged_in_user_id, recipe_id, category, ingredient_name, amount, unit)
                db.session.add(grocery_item)
                db.session.commit()

            return jsonify({'status': 'success'})

        #get ingredients from spoonacular api
        else:
            url = 'https://api.spoonacular.com/recipes/informationBulk?'
            params = {'apiKey' : SPOON_API_KEY,
                        'ids' : recipe_id,
                        }

            response = requests.get(url, params)
            data = response.json()
            #print(data)
            recipe_data = None
            #Find our recipe from list
            for recipe in data:
                if str(recipe["id"]) == recipe_id:
                    recipe_data = recipe    
            # print(recipe_data)
            for ingredient in recipe_data["extendedIngredients"]:
                #  print(recipe_data['extendedIngredients'])
                ingredient_name =(ingredient["name"])
                unit = (ingredient["unit"])
                amount = (ingredient["amount"])
                category = (ingredient["aisle"])

                grocery_item = crud.create_grocery_item(logged_in_user_id, recipe_id, category, ingredient_name, amount, unit)
                db.session.add(grocery_item)
                db.session.commit()

            return jsonify({'status': 'success'})

#=======================DISPLAY MEAN PLAN=====================#
@app.route("/meal-plan")
def meal_plan_by_user():
    """Process meal plan by user."""

    logged_in_user_id = session.get("user_id")
    meal_plan = crud.get_meal_plan_recipe_ids(logged_in_user_id)
    meal_plan_recipes = []

    if logged_in_user_id == None:
        return render_template('404.html'), 404
    
    else:        

        for recipe_id in meal_plan:
            #retrieve data from db
            if recipe_id.startswith('cook'):
                db_recipe = helpers.get_database_recipe(logged_in_user_id, recipe_id)
                meal_plan_recipes.append(db_recipe)

            else:
                spoon_recipe = helpers.get_spoonacular_recipe(recipe_id)
                meal_plan_recipes.append(spoon_recipe)

        return render_template("mealplan.html", meal_plan_recipes=meal_plan_recipes)

#===REMOVE RECIPE FROM MEAL PLAN & INGREDIENTS FROM GROCERY===#
@app.route("/remove-meal-plan", methods=["POST"])
def del_recipe_from_mp():
    """Process to remove recipe from meal plan."""

    logged_in_user = session.get("user_id")
    recipe_id = request.json.get("recipe_id")

    #remove recipe from meal plans
    mp_to_delete = crud.get_meal_plan_by_user_and_recipe(logged_in_user, recipe_id)
    db.session.delete(mp_to_delete)
    
    #remove ingredients from grocery items 
    grocery_items_to_delete = crud.get_grocery_item_by_user_and_recipe(logged_in_user, recipe_id)
    for item in grocery_items_to_delete:
        db.session.delete(item)

    db.session.commit()

    return redirect("/meal-plan")

#=========================DISPLAY GROCERY ITEMS===============#
@app.route("/groceries")
def get_grocery_items():
    """Get total of grocery items."""

    logged_in_user_id = session.get("user_id")
    total_grocery = helpers.get_total_grocery_list(logged_in_user_id)

    if logged_in_user_id == None:
        return render_template('404.html'), 404
    
    else:
        return render_template("groceries.html", total_grocery=total_grocery)

#=======================COOKBOOK FEATURE======================#
@app.route("/my-cookbook")
def get_recipes():
    """Process recipes created by user."""

    logged_in_user_id = session.get("user_id")
    recipes = crud.get_recipes_by_user(logged_in_user_id)

    if logged_in_user_id == None:
        return render_template('404.html'), 404
    
    else:
        return render_template("users_recipes.html", recipes=recipes)

#=======================CREATE RECIPE=========================#
@app.route('/create_recipe', methods=['POST'])
def render_page():
    """Process to render page to create_recipe."""

    return render_template('create_recipe.html')

@app.route('/create-recipe', methods=['POST'])
def create_recipe():
    """Process to create user's recipe."""

    try:
        logged_in_user_id = session.get("user_id")
        #Generate random recipe id with letter to avoid matching with API recipe ID
        recipe_id = "cook" + (''.join(str(random.randint(0, 9)) for num in range(5)))
        title = request.form['name']    
        instructions = request.form['instructions']
        servings = request.form['servings']
        
        #image
        my_file = request.files["my_file"]
        if my_file:
            result = cloudinary.uploader.upload(my_file,
                        api_key=CLOUDINARY_KEY,
                        api_secret=CLOUDINARY_SECRET,
                        cloud_name=CLOUD_NAME)

            image = result['secure_url']
        else:
            image = None

        # save to db
        new_recipe = crud.create_my_recipe(logged_in_user_id, recipe_id, title, image, instructions, servings)
        db.session.add(new_recipe)
        db.session.commit() 

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
            recipe_ingredient = crud.create_recipe_ingredient(recipe_id, ingredient_name, amount, units, category)
            db.session.add(recipe_ingredient)
            db.session.commit() 
    except Exception as e:
        flash("Error creating recipe: " + str(e), "please try again", 'alert alert-danger')
    
    else:
        flash("Recipe created successfully!", 'alert alert-success')
    
    return redirect("/my-cookbook")

#===================REMOVE RECIPE FROM COOKBOOK===============#
@app.route("/remove-recipe", methods=["POST"])
def remove_recipe():
    """Process to remove recipe created by user from Cookbook."""

    logged_in_user_id = session.get("user_id")
    recipe_id = request.json.get("recipe_id")

    #Remove recipe from CookBook
    recipe_to_delete = crud.get_recipe_by_user_and_recipeid(logged_in_user_id, str(recipe_id))
    ingredients_to_delete = crud.get_recipe_ingredients(recipe_id)
    for item in ingredients_to_delete:
        db.session.delete(item)

    #Check if recipe is in Meal Plan, if so process to delete recipe from Meal Plan
    try:
        mp_to_delete = crud.get_meal_plan_by_user_and_recipe(logged_in_user_id, recipe_id)
        grocery_items_to_delete = crud.get_grocery_item_by_user_and_recipe(logged_in_user_id, recipe_id)
        for item in grocery_items_to_delete:
            db.session.delete(item)
        db.session.delete(mp_to_delete)

    except:
        pass

    db.session.delete(recipe_to_delete)
    db.session.commit()

    return redirect("/my-cookbook")
    # return jsonify({'status': 'success'})

if __name__ == "__main__":
    connect_to_db(app, "mealplanning")
    app.run(host="0.0.0.0", port=5000, debug=True)