import sys

from sqlalchemy.engine import create_engine

sys.path.append("../")


one_engine = create_engine('mysql+mysqlconnector://one:1905@127.0.0.1/one_db', pool_size=50, max_overflow=100)



