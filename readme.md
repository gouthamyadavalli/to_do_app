# Weather Dashboard

## Overview

The Weather Dashboard is a Flask-based web application that allows users to check the current weather conditions for any city. The application uses the OpenWeatherMap API to fetch weather data and presents it in a user-friendly interface with animations and a responsive design.

## Features

- Search for current weather conditions by city name.
- Display temperature, weather description, and icon.
- Animated and responsive UI.
- Built using Flask, HTML, CSS.

## Prerequisites

- Python 3.6 or higher
- Flask
- OpenWeatherMap API Key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-dashboard.git
   cd weather-dashboard
2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3. Add your OpenWeatherMap API key in the `config.py` file:
    ```python
    API_KEY = 'your_openweathermap_api_key_here'
    ```
4. Run the application:
    ```bash
    flask run
    ```
5. Open your browser and navigate to `http://127.0.0.1:5000/` to use the Weather Dashboard.

## Usage
 - Enter a city name into the input field and click "Search" to view the current weather conditions for that city.

