
# To-Do List Application

## Overview

The To-Do List Application is a simple web app built with Flask that allows users to manage their tasks. Users can add, update, and delete tasks. The application features user authentication and a clean, responsive UI.

## Features

- User authentication (registration and login).
- Add, update, and delete tasks.
- Responsive design.

## Prerequisites

- Python 3.6 or higher
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Login

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gouthamyadavalli/todo-app.git
   cd todo-app

2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3. Configure the `config.py` file:
    ```python
    class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```
4. Initialise the database:
    ```
    flask shell
    from app import db
    db.create_all()
    exit()

4. Run the application:
    ```bash
    flask run
    ```
5. Open your browser and navigate to `http://127.0.0.1:5000/` to use the Weather Dashboard.

## Usage
 - Task Management: Register and log in to start managing your tasks.

![Login UI](./static/login.png)

![Login UI](./static/sample-ui.png)

