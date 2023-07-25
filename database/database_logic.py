from sqlalchemy.engine import create_engine
from settings import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS
from models.models import user

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

mock = {
    'operation': user.insert(),
    'values': {"id": "test_3", "email": "test_3", "username": "test_3", "password": "test_3"}
}


def execute_query(query):
    with engine.connect() as connection:
        connection.execute(query)
        connection.commit()


execute_query(mock)
