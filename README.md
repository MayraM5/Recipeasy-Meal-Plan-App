# recipeasy - a meal planning application
Learn more about the developer: https://www.linkedin.com/in/mayra-mercado-/

## Project Description
_recipeasy_ is a fullstack web application for meal planning. Integration of the Spoonacular API allows users to search through thousands of recipes by cuisine or ingredient name, and add recipes to their favorites or to meal plan, as well as automatically get the grocery list for those recipes added to meal plan. _recipeasy_ allows users to create their own recipes, and uses Cloudinary API to allows user to upload their own pictures.

## Features
- **Login and Sign In**
<img src="https://media.giphy.com/media/WcKyjjJmyWhldVAxfC/giphy.gif">

- **View recipe details**
<img src="https://media.giphy.com/media/xO0jQtl4TEbE7OYOBT/giphy.gif">

- **Get grocery list**
<img src="https://media.giphy.com/media/SCLm4Im1znZVLHMF3i/giphy.gif">

- **Create recipe**
<img src="https://media.giphy.com/media/y0ydanHGuldJkzNpNE/giphy.gif">

- **Search recipes by cuisine or ingredient name**
- **Add recipe to favorites and meal plan**

## Installation
- $virtualenv env
- $source env/bin/activate
- $pip3 install -r requirements
- Get your own API keys for APIs referenced below and add them to your own secrets.sh file
- $source secrets.sh
- $createdb mealplanning
- $python3 server.py

### Get your own API keys!
- [Spoonacular API](https://spoonacular.com/food-api/console#Dashboard)
- [Cloudinary API](https://cloudinary.com/documentation/cloudinary_get_started)

## Tech Stack
Python | SQLAlchemy | PostgreSQL | Flask | Jinja | JavaScript | Ajax | Bootstrap | HTML | CSS

## For Version 2.0
- Password hashing
- Add Nutrition, Diet, and Taste details
- Add download/print recipe option
- Integrate Google Calendars API so that users can add meal plan to their Google Calendar
