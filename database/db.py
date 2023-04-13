from sqlalchemy import create_engine
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

engine = create_engine(os.environ.get("ENV_URL"), echo=True)