from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    # Load configuration
    """
        - Creates a Flask application instance and loads configuration settings from a Config class defined in a config.py file.    
    """
    app.config.from_object('config.Config')

    # Initialize extensions
    """
    This comment suggests where you would initialize Flask extensions like Flask-SQLAlchemy, Flask-Login, etc., though they aren't implemented in this snippet.
    """

    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    """
    Registers a blueprint from app.routes. 
    Blueprints help organize routes in Flask applications, making the codebase more modular. main_bp likely contains the main routes for your application.
    """

    # Load AI model
    # from app.models.model_loader import load_model
    # app.model = load_model()
    """
    Loads a machine learning model using a custom function and attaches it directly to the app instance,
     making it accessible throughout the application.
    """
    return app

"""
    Returns the configured Flask application instance.
    This is a well-structured Flask application setup using the application factory pattern,
    which is considered a best practice for Flask apps,
    especially for larger applications that may need different configurations for development, testing, and production environments.
"""