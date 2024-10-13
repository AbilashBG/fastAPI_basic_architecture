from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL database connection URL
# DATABASE_URL = "mysql+pymysql://root:Abi@2000@localhost/task_db"
DATABASE_URL = "mysql+pymysql://root:Abi%402000@localhost/task_db"


# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models to inherit
Base = declarative_base()

# Dependency to get the DB session in the routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# notes and explanation ==========================================>

'''DATABASE_URL holds the connection string to your MySQL database.

mysql:// is the protocol for MySQL databases.

root:Abi@2000 is your username and password.

@localhost/task_db points to your local MySQL database task_db.

create_engine creates the connection between FastAPI and MySQL.

SessionLocal is a factory that allows us to interact with the database in different parts of our app.

Base is used to create the database tables for your models.'''

# <======================================================================>