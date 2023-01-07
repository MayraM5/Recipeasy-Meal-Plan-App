"""Models for meal planning app. """

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(20))

    favorite_recipes = db.relationship("FavoriteRecipe", back_populates="users")
    meal_plans = db.relationship("MealPlan", back_populates="users")
    grocery_items = db.relationship("GroceryItem", back_populates="users")
    recipes = db.relationship("Recipe", back_populates="users")

   
    def __repr__(self):
        return f'<User user_id={self.user_id} first_name={self.first_name} last_name={self.last_name} email={self.email}>'

class FavoriteRecipe(db.Model):
    """A favorite recipe"""

    __tablename__ = "favorite_recipes"

    favorite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipe_id = db.Column(db.Integer, nullable=False)

    users = db.relationship("User", back_populates="favorite_recipes")

    def __repr__(self):
        return f'<FavoriteRecipe user_id={self.user_id} recipe_id={self.recipe_id}>'
    
class MealPlan(db.Model):
    """A meal plan for the week"""

    __tablename__ = "meal_plans"

    meal_plan_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    recipe_id = db.Column(db.String, nullable=False)

    users = db.relationship("User", back_populates="meal_plans")
    
    def __repr__(self):
        return f'<MealPlan user_id={self.user_id} recipe_id={self.recipe_id}>' 

class GroceryItem(db.Model):
    """A grocery item """ 

    __tablename__ = "grocery_items"

    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipe_id = db.Column(db.String)
    ingredient_name = db.Column(db.String(50))
    amount = db.Column(db.Float) #Ingredient quantity
    units = db.Column(db.String(30)) #unit of measure
    category = db.Column(db.String(35))
    
    users = db.relationship("User", back_populates="grocery_items")

    def __repr__(self):
        return f'<Grocery user_id={self.user_id} recipe_id={self.recipe_id} category={self.category} ingredient_name={self.ingredient_name} amount={self.amount} units={self.units}>'

class Recipe(db.Model):
    """A recipe """ 

    __tablename__ = "recipes"

    recipe_id = db.Column(db.String, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String)
    image = db.Column(db.String)
    servings = db.Column(db.Integer)
    instructions = db.Column(db.String)

    users = db.relationship("User", back_populates="recipes")
    recipe_ingredients = db.relationship("RecipeIngredient", back_populates="recipes")

    def __repr__(self):
        return f'<Recipe user_id={self.user_id} recipe_id={self.recipe_id} title={self.title} image={self.image} instructions={self.instructions}>'


class RecipeIngredient(db.Model):
    """A Recipe Ingredient"""

    __tablename__ = "recipe_ingredients"

    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_id = db.Column(db.String, db.ForeignKey('recipes.recipe_id'))
    ingredient_name = db.Column(db.String(50))
    amount = db.Column(db.Float) #Ingredient quantity
    units = db.Column(db.String(30)) #unit of measure
    category = db.Column(db.String(35))

    recipes = db.relationship("Recipe", back_populates="recipe_ingredients")

    def __repr__(self):
        return f'<RecipeIngredient recipe_id={self.recipe_id} category={self.category} ingredient_name={self.ingredient_name} amount={self.amount} units={self.units}>'


def connect_to_db(flask_app, mealplanning):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{mealplanning}"
    flask_app.config["SQLALCHEMY_ECHO"] = True
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")  


if __name__ == "__main__":
    from server import app
    connect_to_db(app, 'mealplanning')
