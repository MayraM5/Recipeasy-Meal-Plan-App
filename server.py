"""Server for meal planning app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
import requests
import json


app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

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
        flash(f'User email and/or password is incorrect. Please try again.')
        return redirect('/')        

#log-out
@app.route("/log-out")
def log_out():
    """ Process user log-out """

    del session['user_id']
    flash("You have been logged out!")

    return redirect('/')  #this works!

#Create an account
@app.route("/sign-up")
def show_sign_up():
    """Show the sign up page for a new user"""

    return render_template("signup_form.html")

@app.route("/register", methods=['POST'])
def register():
    """ Create new user"""
        
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
def user():

    return render_template('home.html')

@app.route("/api/fav-recipe", methods=['POST'])
def get_recipe_id():

    logged_in_user = session.get("user_id")
    recipe_id = request.json.get("meal_Id")

    #Get user list favorite recipe ids
    fav_list = crud.get_favorite_recipe_ids(logged_in_user)
    
    #check if user is logged in:
    if logged_in_user is None:
         #     flash("You must log in to add to Favorites") ##Need to fix flash msg It is not showing flash msg
        return redirect('/')
    
    else:
        #check if recipe id is in db
        if recipe_id in fav_list:
            print("Its already added")
            return("Its already added") #==> flash msg not working

        #check if recipe id is in fav, if not add
        else:
            user = crud.get_user_by_id(logged_in_user)
            recipe_id = crud.create_fav(user, (recipe_id))
            db.session.add(recipe_id)
            db.session.commit()
            print("added")

            return("This recipe has been added to Favorites")##It is not showing flash msg

@app.route("/fav-recipe")
def get_favorite_recipes():

    return redirect("/favorites")

@app.route("/favorites")
def display_fav_recipes():

    logged_in_user = session.get("user_id")
    fav_list = crud.get_favorite_recipe_ids(logged_in_user)

    #Convert each element from list to string 
    ids = ','.join(str(id) for id in fav_list)

    url = 'https://api.spoonacular.com/recipes/informationBulk?'
    params = {'apiKey' : '33f7af9664464e1fad151db6e46c6399',
            'includeNutrition': False,
            'ids' : ids,
            }

    response = requests.get(url, params)
    data = response.json()
    print(f'DATA RESPONSE {data}')
    results = []

    for recipe in data:
        id = recipe["id"]
        title = recipe['title']
        image = recipe["image"]
        cuisine = recipe["cuisines"]

        element = {'id': id, 'title': title, 'image': image, 'cuisines': cuisine}

        results.append(element)
    
    print(f'results: {results}')

    return render_template("favorites.html", favorite_recipes=results)


@app.route("/meal-plan")
def get_meal_plan():

    return render_template("mealplan.html")





if __name__ == "__main__":
    connect_to_db(app, "mealplanning")
    app.run(host="0.0.0.0", port=5000, debug=True)
