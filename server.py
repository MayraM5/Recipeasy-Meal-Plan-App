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

    if session.get("user_id"):
        return redirect("/user_details.html") ### create use ================
    else:
        return render_template('homepage.html') 
    # return render_template('homepage.html') 

#Log in
@app.route("/log-in", methods=["POST"])
def log_in():
    """Process user log-in."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    #If email in db, check if password entered match with password on db
    # if user:
    #     if password == user.password:
    #         session["user_id"] = user.user_id

    #         return render_template("/user_details.html")

    #     else:
    #         flash("Invalid password, please try again.")
    #         return redirect("/")

    # else:
    #     flash("Your are not signed up yet")
    #     return redirect("/signup")

    if not user or user.password != password:
        flash("The email or password was incorrect")
        return redirect("/sign-up") #tHIS DON WORK ============

    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back!, {user.email}!")
        
        return render_template("user_details.html") #this works!

#Log out:
# @app.route('/log-out')
# def logout():
# 	""" Log user out"""
#     pass
#     #### HOW TO LOG OUT ??============================
    
#     return redirect('/')

#Create an account
@app.route("/sign-up", methods=['POST'])
def sign_up():
    """ Process user sign up"""
    
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        flash("This email is already registered. Please log in.")
        return redirect("/")

    else:
        user = crud.create_user(first_name, last_name, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Yay! Your account has been created! Please log in.")

    return render_template('/user_details.html')


if __name__ == "__main__":
    connect_to_db(app, "mealplanning")
    app.run(host="0.0.0.0", port=5002, debug=True)
