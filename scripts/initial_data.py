import logging

from app.core.init_db import init_db
from app.core.session import engine
from sqlmodel import Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    # TODO: missing command to verify if database is alive
    # TODO: implement retry mechanism
    db = Session(engine)
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()