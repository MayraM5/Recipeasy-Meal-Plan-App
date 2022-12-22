# import os
# from random import choice, randint

# # Drop and recreate database
# os.system(f'dropdb mealplanning')
# os.system(f'createdb mealplanning')

# from model import db, connect_to_db
# import model
# import crud
# import serverd

# # Connect app to database
# connect_to_db(server.app)

# # Updates the database schema
# db.create_all()

# user1 = User(first_name="Maui", last_name="Doggie", email="maui@test.com", password="12345")
# user1 = crud.create_user(email, fname, lname, password)
# db.session.add(user1)

# user2 = User(first_name="Scott", last_name="Doggie", email="scott@test.com", password="12345")
# user2 = crud.create_user(email, fname, lname, password)
# db.session.add(user2)

# db.session.commit()
# print(User)
 