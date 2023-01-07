'''CRUD operations functions'''
from model import db, User, FavoriteRecipe, MealPlan, GroceryItem, Recipe, RecipeIngredient, connect_to_db


def create_user(first_name, last_name, email, password):
    """Create and return a new user"""

    user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    
    return user


def get_user_by_email(email):
    """Return a user by their email."""

    return User.query.filter(User.email == email).first()


def create_fav(user_id, recipe_id):
    """Create a favorite recipe."""

    fav_recipe = FavoriteRecipe(user_id=user_id, recipe_id=recipe_id)

    return fav_recipe


def get_favorites_by_user(user_id):
    """Return favorite recipes by user."""

    user_favs_list = FavoriteRecipe.query.filter(FavoriteRecipe.user_id == user_id).all()
    
    return user_favs_list


def get_favorite_recipe_ids(user_id):
    """Return recipes id by user."""

    user_fav = get_favorites_by_user(user_id)

    fav_recipe_id_list =[]

    for item in user_fav:
        fav_info = item.recipe_id

        fav_recipe_id_list.append(fav_info)
    
    return fav_recipe_id_list


def get_fav_by_user_and_recipe(user_id, recipe_id):
    """Return favorite obj of user & recipe_id."""

    fav_to_delete = FavoriteRecipe.query.filter(FavoriteRecipe.user_id == user_id, 
                    FavoriteRecipe.recipe_id == recipe_id).one()

    return fav_to_delete


def get_meal_plan_by_user(user_id):
    """Return meal plan recipes by user."""

    user_meal_plan_list = MealPlan.query.filter(MealPlan.user_id == user_id).all()
    
    return user_meal_plan_list


def get_meal_plan_recipe_ids(user_id):
    """Return meal plan recipes id by user."""

    user_meal_plan = get_meal_plan_by_user(user_id)

    meal_plan_id_list =[]

    for item in user_meal_plan:
        meal_plan_info = item.recipe_id

        meal_plan_id_list.append(meal_plan_info)
    
    return meal_plan_id_list    


def create_meal_plan(user_id, recipe_id):
    """Create meal plan."""

    meal_plan = MealPlan(user_id=user_id, recipe_id=recipe_id)

    return meal_plan


def get_meal_plan_by_user_and_recipe(user_id, recipe_id):
    """Return meal plan obj of user & recipe_id."""

    meal_plan_to_delete = MealPlan.query.filter(MealPlan.user_id == user_id, 
                            MealPlan.recipe_id == recipe_id).one()

    return meal_plan_to_delete


def create_grocery_item(user_id, recipe_id, category, ingredient_name, amount, units):
    """Create grocery items."""
    
    grocery_item = GroceryItem(user_id=user_id, recipe_id=recipe_id, category=category,
                    ingredient_name=ingredient_name, amount=amount, units=units)
    
    return grocery_item


def get_grocery_item_by_user_and_recipe(user_id, recipe_id):
    """Return grocery item obj of user & recipe."""

    grocery_items_to_delete = GroceryItem.query.filter(GroceryItem.user_id == user_id, 
                                GroceryItem.recipe_id == recipe_id).all()

    return grocery_items_to_delete


def get_grocery_items_by_user(user_id):
    """Return grocery items by user id."""

    grocery_items = db.session.query(GroceryItem.user_id == user_id, GroceryItem.category, GroceryItem.ingredient_name, 
                    db.func.sum(GroceryItem.amount), GroceryItem.units).group_by(GroceryItem.user_id, 
                    GroceryItem.category, GroceryItem.ingredient_name, GroceryItem.units).all()

    return grocery_items

####################NEW FEATURE ######################
def create_my_recipe(user_id, recipe_id, title, image, instructions, servings):
    """Create favorite recipes"""

    new_recipe = Recipe(user_id=user_id, recipe_id=recipe_id, title=title, image=image, instructions=instructions, servings=servings)

    return new_recipe

def create_recipe_ingredient(recipe_id, ingredient_name, amount, units, category):

    recipe_ingredient = RecipeIngredient(recipe_id=recipe_id, ingredient_name=ingredient_name, amount=amount, units=units, category=category)

    return recipe_ingredient


def get_recipes_by_user(user_id):
    """Get all recipes created by user."""

    my_recipes = Recipe.query.filter(Recipe.user_id == user_id).all()

    return my_recipes


def get_recipe_by_user_and_recipeid(user_id, recipe_id):
    """Get recipe id and user id."""

    my_recipes = Recipe.query.filter(Recipe.user_id==user_id, Recipe.recipe_id==recipe_id).one()

    return my_recipes


def get_recipe_data(user_id, recipe_id):
    """Get recipes created by user from database"""
    
    my_recipes = Recipe.query.filter(Recipe.user_id==user_id, Recipe.recipe_id==recipe_id).all()

    return my_recipes


def get_recipe_ingredients(recipe_id):
    """Get ingredients for recipe created by user from database"""

    recipe_ingredient = RecipeIngredient.query.filter(RecipeIngredient.recipe_id == recipe_id).all()

    return recipe_ingredient




if __name__ == '__main__':
    from server import app
    connect_to_db(app, 'mealplanning')

