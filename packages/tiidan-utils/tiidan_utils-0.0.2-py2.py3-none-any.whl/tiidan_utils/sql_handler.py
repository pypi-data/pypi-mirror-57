import logging
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

log = logging.getLogger(__name__)


class SqlException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class SqlHandler:
    Session = None
    engine = None

    def __init__(self, config=None):
        if config is not None:
            self.config(config)

    def config(self, config):
        log.debug("setting db connection to: {}".format(config["host"]))
        self.engine = create_engine(URL(**config), paramstyle="pyformat")
        self.Session = sessionmaker(bind=self.engine, autocommit=True)

    def raw(self, query, bindings):
        session = self.Session()
        try:
            res = session.execute(query, bindings)
        except SQLAlchemyError as err:
            log.debug(err)
            log.error("encountered error while processing query: {}".format(err))
            raise SqlException("encountered error while processing query.")
        finally:
            session.close()
        return res

    def df(self, query, params=None, **kwargs):
        return pd.read_sql(query, self.engine, params=params, **kwargs)

    def first(self, query, params=None):
        res = self.raw(query, params).first()
        return None if res is None else res[0]
