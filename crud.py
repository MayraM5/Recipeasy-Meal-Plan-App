'''CRUD operations functions'''
from model import db, User, FavoriteRecipe, MealPlan, GroceryItem, connect_to_db

def create_user(first_name, last_name, email, password):
    """Create and return a new user"""

    user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    
    return user

def get_user():
    """Return a list of all users data"""
    
    return User.query.all()

def get_user_by_id(user_id):
    """Return an user by the given user_id"""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by their email. 
        e.g
        >>> get_user_by_email("test@test.com")
        >>> <User user_id=1 first_name=test last_name=test email=test@test.com>
    """

    return User.query.filter(User.email == email).first()
#    return User.query.filter(email == email).first()

def create_fav(users, recipe_id):
    """Create favorite recipes"""

    fav_recipe = FavoriteRecipe(users=users, recipe_id=recipe_id)

    return fav_recipe

def get_favorites_by_user(user_id):
    """Return favorite recipes by user"""

    user_favs_list = FavoriteRecipe.query.filter(FavoriteRecipe.user_id == user_id).all()
    
    return user_favs_list

def get_favorite_recipe_ids(user_id):
    """Return list of recipe id by user"""

    user_fav = get_favorites_by_user(user_id)

    fav_recipe_id_list =[]

    for item in user_fav:
        fav_info = item.recipe_id

        fav_recipe_id_list.append(fav_info)
    
    return fav_recipe_id_list

    #dict:
    # for item in user_fav:
    #     fav_info = {'user_id' : item.user_id, 
    #                 'recipe_id' : item.recipe_id
    #                 }

    #     fav_recipe_id_list.append(fav_info)
    
    # return fav_recipe_id_list

def get_fav_by_user_and_recipe(user_id, recipe_id):
    """Return favorite obj of user & recipe_id"""

    fav_to_delete = FavoriteRecipe.query.filter(FavoriteRecipe.user_id == user_id, FavoriteRecipe.recipe_id == recipe_id).one()

    return fav_to_delete

def get_neal_plan_by_user(user_id):
    """Return favorite recipes by user"""

    user_meal_plan_list = MealPlan.query.filter(MealPlan.user_id == user_id).all()
    
    return user_meal_plan_list

def get_meal_plan_recipe_ids(user_id):
    """Return list of recipe id by user"""

    user_meal_plan = get_neal_plan_by_user(user_id)

    meal_plan_id_list =[]

    for item in user_meal_plan:
        meal_plan_info = item.recipe_id

        meal_plan_id_list.append(meal_plan_info)
    
    return meal_plan_id_list    

def create_meal_plan(users, recipe_id):
    """Create meal plan"""

    meal_plan = MealPlan(users=users, recipe_id=recipe_id)

    return meal_plan

def get_meal_plan_by_user_and_recipe(user_id, recipe_id):
    """Return meal plan obj of user & recipe_id"""

    meal_plan_to_delete = MealPlan.query.filter(MealPlan.user_id == user_id, MealPlan.recipe_id == recipe_id).one()

    return meal_plan_to_delete


if __name__ == '__main__':
    from server import app
    connect_to_db(app, "mealplanning")

# Create	Insert => create /add new rows/reecord to db
# Read	Select => display data ex see recipe / see fav recipe
# Update	Update => mod existing data
# Delete	Delete => remove record from table

# Create	Post
# Read	Get
# Update	Put
# Delete	Delete
