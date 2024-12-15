# Setting up the project

- create virtual environment
    poetry env use python
    poetry shell
    poetry install

- environment variables
    copy .env.example and rename to .env

- alembic config
    copy alembic.ini.example and rename to alembic.ini
    modify "sqlalchemy.url" in this format "postgresql+psycopg://postgres:password@localhost:5432/postgres"

- start postgres server
    docker compose up -d postgres

- run migrations
    alembic upgrade head

- run server
    python src/main.py
