import sys
import os
# Ajustando o caminho para importar os módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlmodel import SQLModel, create_engine
from .model import *

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo = True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()