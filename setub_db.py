from app import app
from models import db

# Ensure you import all the models that you want to create tables for
from models import User, Task

# Use the app context to create the tables
with app.app_context():
    db.create_all()
    print("Database tables created.")
