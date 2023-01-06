"""Server for meal planning app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
import requests
import json
import os
import random
import cloudinary.uploader

app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined


SPOON_API_KEY = os.environ["SPOON_API_KEY"]

CLOUD_NAME = "dhyrymmf4"
CLOUDINARY_SECRET= os.environ["CLOUDINARY_SECRET"]
CLOUDINARY_KEY= os.environ["CLOUDINARY_KEY"]

#Homepage
@app.route('/')
def homepage():
    """Display login template."""

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

#log-out
@app.route("/log-out")
def log_out():
    """Process user log-out."""

    del session['user_id']
    flash("You have been logged out!", 'alert alert-success') 

    return redirect('/')  

#Create an account
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

@app.route("/home")
def home():
    """Display homepage."""

    return render_template('home.html', SPOON_API_KEY=SPOON_API_KEY)

#Add recipe to favorites
@app.route("/api/fav-recipe", methods=['POST']) 
def add_recipe_to_favorites():
    """Process to add recipe to favorites."""

    logged_in_user_id = session.get("user_id")
    recipe_id = request.json.get("recipe_Id")
    print(logged_in_user_id)

    #Get user list favorite recipe ids
    fav_list = crud.get_favorite_recipe_ids(logged_in_user_id)
  
    #check if user is logged in:
    if logged_in_user_id is None:
        flash("You must log in to add to Favorites") 
        return redirect('/')
    
    else:
        #check if recipe id is in db
        if recipe_id in fav_list:
            return jsonify({'status': 'error', 'reason': 'duplicate'}), 400

        # #check if recipe id is in fav, if not add
        else:
            recipe_id_to_save = crud.create_fav(logged_in_user_id, (recipe_id))
            db.session.add(recipe_id_to_save)
            db.session.commit()

            return jsonify({'status': 'success'})

#Display favorites
@app.route("/favorites")
def get_fav_recipes():
    """Process user's favorite recipes."""

    logged_in_user_id = session.get("user_id")
    fav_list = crud.get_favorite_recipe_ids(logged_in_user_id)

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

#REMOVE RECIPE FROM FAVORITES
@app.route("/remove-fav", methods=["POST"])
def remove_recipe_from_favorites():
    """Process to remove recipe from favorites."""

    logged_in_user_id = session.get("user_id")
    recipe_id = request.json.get("recipe_id")

    fav_to_delete = crud.get_fav_by_user_and_recipe(logged_in_user_id, recipe_id)

    db.session.delete(fav_to_delete)
    db.session.commit()

    return redirect("/favorites")


#==============DISPLAY RECIPE DETAILS=====================
@app.route("/recipe-details-<recipe_id>", methods=["GET","POST"]) 
def get_recipe_details(recipe_id):
    """Process recipe details by recipe id."""
    
    logged_in_user_id = session.get("user_id")
    #check if recipe is in database (created by user)
    if recipe_id.startswith('cook'):

        recipe_data = crud.get_recipe_data(logged_in_user_id, recipe_id)

        for recipe in recipe_data:
            title = recipe.title
            image = recipe.image
            instructions = recipe.instructions.split('.')
            servings = recipe.servings
            
        recipe_ingredients = crud.get_recipe_ingredients(recipe_id)
        ingredients_list = []
        for ingredient in recipe_ingredients:
            name = ingredient.ingredient_name
            amount = ingredient.amount
            unit = ingredient.units
            
            elements = {'name': name, 'amount' : amount, "unit" : unit}
            ingredients_list.append(elements)

        return render_template("recipe_details.html", title=title, instructions=instructions, 
                        ingredients = ingredients_list, image=image, servings=servings)
    
    #Spoonacular recipe
    else:
        url = 'https://api.spoonacular.com/recipes/informationBulk?'
        params = {'apiKey' : SPOON_API_KEY,
                    'ids' : recipe_id,
                    }

        response = requests.get(url, params)
        data = response.json()

        for recipe in data:
            id = recipe["id"]
            title = recipe['title']
            image = recipe["image"]
            servings = recipe["servings"]

            try:
                raw_instructions = recipe["instructions"]

                # if recipe["instructions"] is empty or None, use recipe["summary"]
            except KeyError:
                try:
                    raw_instructions = recipe["summary"]
                except KeyError:
                    raw_instructions = None
     
            #Remove extra tags
            tags_to_remove = ['<ol>', '</ol>', '</li>', '<span>', '</span>', '<p>', '</p>']
            try:
                for tag in tags_to_remove:
                    raw_instructions = raw_instructions.replace(tag, '')
                #Convert in list to display every step in a row
                temp = raw_instructions.split('<li>')
                if len(temp) > 1:
                    instructions = temp
                else:
                    # Backup method if no <li>
                    instructions = raw_instructions.split('.')

                # instructions = raw_instructions.split('<li>')

                for index, instruction in enumerate(instructions):
                    if instruction == "":
                        instructions.pop(index)
                
                # for index in range(0, len(instructions)):
                #     if instructions[index] == "":
                #         instructions.pop(index)

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
    
        return render_template("recipe_details.html", title=title, instructions=instructions, 
                                ingredients = ingredients_list, servings = servings, image = image)


#ADD RECIPE TO MP AND GROCERY ITEMS TO GROCERIES
@app.route("/api/meal-plan", methods=['POST'])  #==> FLASH MSG NOT DISPLAY
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
        
        #retrieve data from db
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


# #Display meal plan
@app.route("/meal-plan")
def meal_plan_by_user():
    """Process meal plan by user."""

    logged_in_user_id = session.get("user_id")
    meal_plan = crud.get_meal_plan_recipe_ids(logged_in_user_id)
    meal_plan_recipes = []

    for recipe_id in meal_plan:
        #retrieve data from db
        if recipe_id.startswith('cook'):

            recipe_data = crud.get_recipe_data(logged_in_user_id, recipe_id)

            for recipe in recipe_data:
                id = recipe.recipe_id
                title = recipe.title
                image = recipe.image

                element = {'id': id, 'title': title, 'image': image}

                meal_plan_recipes.append(element)
            # print(meal_plan_data)

        else:
            #retrieve data from api
            url = 'https://api.spoonacular.com/recipes/informationBulk?'
            params = {'apiKey' : SPOON_API_KEY,
                    'includeNutrition': False,
                    'ids' : recipe_id,
                    }

            response = requests.get(url, params)
            data = response.json()
           # print(f'DATA RESPONSE {data}') 
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
def del_recipe_from_mp():
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

#Display grocery shopping list:
@app.route("/groceries")
def get_grocery_items():
    """Process grocery items."""

    logged_in_user = session.get("user_id")
    total_grocery = crud.get_total_grocery_list(logged_in_user)

    return render_template("groceries.html", total_grocery=total_grocery) #, name=name, amount=amount, unit=unit)

#############NEW FEATURE ####################################
@app.route("/my-cookbook")
def get_recipes():
    """Process recipes created by user."""

    logged_in_user = session.get("user_id")
    recipes = crud.get_my_recipes(logged_in_user)

    return render_template("my_recipes.html", recipes=recipes)


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
        recipe_id = "cook" + (''.join(str(random.randint(0, 9)) for _ in range(5)))
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

#REMOVE RECIPE FROM COOKBOOK
@app.route("/remove-recipe", methods=["POST"])
def remove_recipe():
    """Process to remove recipe created by user from Cookbook."""

    logged_in_user_id = session.get("user_id")
    recipe_id = request.json.get("recipe_id")
    
    recipe_to_delete = crud.get_recipe_by_user_and_recipeid(logged_in_user_id, str(recipe_id))
    
    ingredients_to_delete = crud.get_recipe_ingredients(recipe_id)
    
    for item in ingredients_to_delete:
        db.session.delete(item)
   
    db.session.delete(recipe_to_delete)
    db.session.commit()

    return redirect("/my-cookbook")



if __name__ == "__main__":
    connect_to_db(app, "mealplanning")
    app.run(host="0.0.0.0", port=5001, debug=True)