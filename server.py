"""Server for meal planning app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)

app.secret_key = "lavidaesbella"
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

    #if user in db:
    if user:
        if input_password == user.password:
            session["user_id"] = user.user_id
           
            return redirect("/user") #this works!

        else:
            #incorrect password:
            return redirect("/") #this works!

    elif not user:
        #not in db => sign up
        return redirect("/") #thisdoes not works!!

#log-out
@app.route("/log-out")
def log_out():
    """ Process user log-out """

    del session['user_id']
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
        #This email is already registered.=> homepage to log in
        return redirect("/user") #this works!

@app.route("/user")
def user():

    return render_template('user_details.html')


if __name__ == "__main__":
    connect_to_db(app, "mealplanning")
    app.run(host="0.0.0.0", port=5000, debug=True)
