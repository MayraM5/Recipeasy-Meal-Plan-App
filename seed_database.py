# import os
# # Drop and recreate database
# os.system(f'dropdb mealplanning')
# os.system(f'createdb mealplanning')

# from model import db, connect_to_db
# import server

# # Connect app to database
# connect_to_db(server.app)

# # Updates the database schema
# db.create_all()
# import crud

# user1 = User(first_name="Maui", last_name="Doggie", email="maui@test.com", password="12345")
# user1 = crud.create_user(email, first_name, last_name, password)
# db.session.add(user1)
# db.session.commit()
# print(User)
 