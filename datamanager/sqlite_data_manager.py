from flask_sqlalchemy import SQLAlchemy
from datamanager.data_manager import DataManagerInterface
from datamanager.data_models import db

class SQLiteDataManager(DataManagerInterface):
    """
       Implementation of DataManagerInterface to interact with the SQLite database using SQLAlchemy.
       """

    def __init__(self, app):
        """
        Initialize the SQLiteDataManager with the Flask app instance.
        Args:
            app: The Flask application instance.
        """
        db.init_app(app)
        self.db = db