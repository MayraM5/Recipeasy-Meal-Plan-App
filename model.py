"""Models for meal planning app. """

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

# class User(db.Model):
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
    #recipe_name = db.Column(db.String(30))

    users = db.relationship("User", back_populates="favorite_recipes")

    def __repr__(self):
        return f'<FavoriteRecipe user_id={self.user_id} recipe_id={self.recipe_id}>'
        # return f'<FavoriteRecipe favorite_id={self.favorite_id} fav_recipe_name={self.fav_recipe_name}>'

class MealPlan(db.Model):
    """A meal plan for the week"""

    __tablename__ = "meal_plans"

    meal_plan_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    recipe_id = db.Column(db.Integer, nullable=False)

    users = db.relationship("User", back_populates="meal_plans")
    # grocery_items = db.relationship("GroceryItem", back_populates="meal_plans")
    
    def __repr__(self):
        return f'<MealPlan user_id={self.user_id} recipe_id={self.recipe_id}>' 

class GroceryItem(db.Model):
    """A grocery item """ 

    __tablename__ = "grocery_items"

    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipe_id = db.Column(db.Integer) # db.ForeignKey('meal_plans.recipe_id'))
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


#DATABASE INFO FOR TESTING PURPOSE:
# user1 = User(first_name="Maui", last_name="Doggie", email="maui@test.com", password="12345")
# user2 = User(first_name="Scott", last_name="Smith", email="scott@test.com", password="56789")
# user3 = User(first_name="Anna", last_name="Dodson", email="anna@test.com", password="36985")

# db.session.add(user1)
# db.session.commit()

# fav1 = FavoriteRecipe(recipe_id=12, recipe_name="Veggie quesadilla")
# fav2 = FavoriteRecipe(recipe_id=82, recipe_name="Pizza")
# fav3 = FavoriteRecipe(recipe_id=112, recipe_name="pasta")
# fav4 = FavoriteRecipe(recipe_id=12, recipe_name="Veggie quesadilla")

# user1.favorite_recipes.append(fav)
# db.session.commit()


# mp1 = MealPlan(recipe_id=82, recipe_name="Pizza", instruction="Blah blah and blah")
# mp2 = MealPlan(recipe_id=112, recipe_name="Pasta", instruction="Blah blah and add a lot cheese!")

# user1.meal_plans.append(mp1)
# db.session.commit()

# gi1 = GroceryItem(ingredient_name="parmensan cheese", quantity=4, units="Oz")
# gi2 = GroceryItem(ingredient_name="grape tomatoes", quantity=2, units="pints")
# gi3 = GroceryItem(ingredient_name="linguine pasta", quantity=10, units="Oz")

# gi4 = GroceryItem(ingredient_name="Parmensan cheese", quantity=8, units="Oz") 
# gi5 = GroceryItem(ingredient_name="naan", quantity=4, units="unit")

# mp1.grocery_items.append(gi1)
# mp1.grocery_items.append(gi1)


# a_name = Class.query.all()

