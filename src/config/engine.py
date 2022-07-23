from sqlmodel import create_engine, SQLModel, Session, select

sqlite_file_name = "db.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    """Runs DDL group commands"""

    SQLModel.metadata.create_all(engine)


def get_dependencie():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
