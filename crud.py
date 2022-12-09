'''CRUD operations functions'''
from model import db, User, FavoriteRecipe, MealPlan, GroceryItem, connect_to_db

def create_user(first_name, last_name, email, password):
    """Create and return a new user"""

    user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    
    return user

def get_user():
    """return a list of all users data"""
    
    return User.query.all()

def get_user_by_id(user_id):
    """return an user by the given user_id
    e. g
    """

    return User.query.get(user_id)

def get_user_by_email(email):
    """ return a user by their email. 
    e.g
        >>> get_user_by_email("test@test.com")
        >>> <User user_id=1 first_name=test last_name=test email=test@test.com>
    """

    return User.query.filter(User.email == email).first()
#    return User.query.filter(email == email).first()
    

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
