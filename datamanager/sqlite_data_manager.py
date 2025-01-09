from flask_sqlalchemy import SQLAlchemy
from datamanager.data_manager import DataManagerInterface

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.db = SQLAlchemy(db_file_name)