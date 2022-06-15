from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# El engine permite a SQLAlchemy comunicarse con la base da datos
engine = create_engine("sqlite:///database/noticias.db", connect_args={"check_same_thread":False})# conexion simultanea web

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()