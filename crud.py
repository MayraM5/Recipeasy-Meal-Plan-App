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
    """return an user by the given user_id"""

    return User.query.get(user_id)

def get_user_by_email(email):
    """ return a user by the given email"""

    return User.query.filter(User.email == email).first()
    

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


# def create_movie(title, overview, release_date, poster_path):

#     movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

#     return movie

# def get_movies():

#     return Movie.query.all()

# def get_movie_by_id(movie_id):

#     return Movie.query.get(movie_id)    


# def create_rating(user, movie, score):
#     """Create and return a new rating"""

#     # rating = Rating (user=user.user_id, movie=movie.movie_id, score=score)
#     rating = Rating (user=user, movie=movie, score=score)

#     return rating

# def update_rating(rating_id, new_score):
#     """ Update a rating given rating_id and the updated score. """
#     rating = Rating.query.get(rating_id)
#     rating.score = new_score

# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app)