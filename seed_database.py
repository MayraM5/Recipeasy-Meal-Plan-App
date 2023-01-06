import os
import crud
import model
import server

# Drop and recreate database
os.system('dropdb mealplanning')
os.system('createdb mealplanning')

# Connect app to database
model.connect_to_db(server.app, "mealplanning")
model.db.create_all()


user = crud.create_user(first_name="Mary", last_name="Test", email="mary@test.com", password="12345")
# user = crud.create_user(email, first_name, last_name, password)
model.db.session.add(user)
model.db.session.commit()

 # Updates the database schema
model.db.create_all()