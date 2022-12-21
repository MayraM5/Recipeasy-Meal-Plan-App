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

def create_fav(user_id, recipe_id):
    """Create favorite recipes"""

    fav_recipe = FavoriteRecipe(user_id=user_id, recipe_id=recipe_id)

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

    fav_to_delete = FavoriteRecipe.query.filter(FavoriteRecipe.user_id == user_id, 
                    FavoriteRecipe.recipe_id == recipe_id).one()

    return fav_to_delete

def get_meal_plan_by_user(user_id):
    """Return meal plan recipes by user"""

    user_meal_plan_list = MealPlan.query.filter(MealPlan.user_id == user_id).all()
    
    return user_meal_plan_list

def get_meal_plan_recipe_ids(user_id):
    """Return list of recipe id by user"""

    user_meal_plan = get_meal_plan_by_user(user_id)

    meal_plan_id_list =[]

    for item in user_meal_plan:
        meal_plan_info = item.recipe_id

        meal_plan_id_list.append(meal_plan_info)
    
    return meal_plan_id_list    

def create_meal_plan(user_id, recipe_id):
    """Create meal plan"""

    meal_plan = MealPlan(user_id=user_id, recipe_id=recipe_id)

    return meal_plan

def get_meal_plan_by_user_and_recipe(user_id, recipe_id):
    """Return meal plan obj of user & recipe_id"""

    meal_plan_to_delete = MealPlan.query.filter(MealPlan.user_id == user_id, 
                            MealPlan.recipe_id == recipe_id).one()

    return meal_plan_to_delete

#create groceries
def create_grocery_item(user_id, recipe_id, ingredient_name, amount, units):
    """Create grocery items"""
    
    grocery_item = GroceryItem(user_id=user_id, recipe_id=recipe_id, 
                    ingredient_name=ingredient_name, amount=amount, units=units)
    
    return grocery_item

#get rows where user_id = user_id & recipe_id = recipe_id:
def get_grocery_item_by_user_and_recipe(user_id, recipe_id):
    """Return grocery item obj of user & recipe"""

    grocery_items_to_delete = GroceryItem.query.filter(GroceryItem.user_id == user_id, 
                                GroceryItem.recipe_id == recipe_id).all()

    return grocery_items_to_delete

#Get rows where user_id = user_id and grouped by ingredient_name, units and sum(amount)
def get_grocery_items_by_user(user_id):
    """Return list of tuples grocery_items group by ingredient_name, units & sum(amount)"""

    grocery_items = db.session.query(GroceryItem.user_id == user_id, GroceryItem.ingredient_name, 
                            db.func.sum(GroceryItem.amount), GroceryItem.units).group_by(GroceryItem.user_id, 
                            GroceryItem.ingredient_name, GroceryItem.units).all()

    return grocery_items

def get_total_grocery_list(user_id):

    results = get_grocery_items_by_user(user_id)

    total_list = []
    for item in results:
        grocery_item = {"name" :  item[1], "amount": item[2], "unit" : item[3]}
     
        total_list.append(grocery_item)

    return (total_list)

        

## select rows and group by SQL => select user_id, ingredient_name, sum(amount), units 
# from grocery_items group by ingredient_name, user_id, units
#result = GroceryItem.query.with_entities(GroceryItem.user_id, GroceryItem.ingredient_name, GroceryItem.amount, GroceryItem.units).all()
#g = GroceryItem.query.filter(GroceryItem.user_id == 1).all()
#FIRST NEEd to get user_id, ingredient name, amount, and units by user_id

#then group by ingredient name, units and sum amount
#THIS GROUP BY INGREDIENT NAME, UNITS AND SUM AMOUNT
# x = db.session.query(GroceryItem.user_id, GroceryItem.ingredient_name, db.func.sum(GroceryItem.amount), GroceryItem.units).group_by(GroceryItem.user_id, GroceryItem.ingredient_name, GroceryItem.units).all()


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
