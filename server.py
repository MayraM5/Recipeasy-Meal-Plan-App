"""Server for meal planning app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
import requests


app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

#Homepage
@app.route('/')
def homepage():
    """Show homepage template"""

    return render_template('homepage.html') 

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
        return redirect('/user')
        
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

# #Create an account
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
        return redirect("/user") #this works!

@app.route("/user")
def user():

    return render_template('dashboard.html')

# @app.route("/user")
# def user():

#     return render_template('/user_details.html')

# @app.route("/dashboard", methods=['POST']) ## return a json y taket the jason from js file to fetch data ohh pero de search fuction, maybe I can get it from html
# def search_recipe():
#     """Random recipes choices""" 

#     url = "https://api.spoonacular.com/recipes/complexSearch?"
#     apiKey = "33f7af9664464e1fad151db6e46c6399"
#     seacrh_recipe = request.form.get("seacrh_recipe")

#     r = requests.get(f'{url}apiKey={apiKey}&cuisine=${seacrh_recipe}')
#     data = r.json()

#     return data
@app.route("/fav_recipe")
def fav_recipe():


    pass



if __name__ == "__main__":
    connect_to_db(app, "mealplanning")
    app.run(host="0.0.0.0", port=5002, debug=True)
