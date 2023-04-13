from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:19570744@localhost/tasksapp", echo=True)