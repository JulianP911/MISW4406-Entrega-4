from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
import datetime

from saludTech.seedwork.dominio.repositorios import SagaLogRepositorio
from .dto import SagaLog

Base = declarative_base()

class SagaLogSQLRepositorio(SagaLogRepositorio):
    def __init__(self, db_url="sqlite:///saga_log.db"):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def guardar_estado(self, id_saga: uuid.UUID, paso: int, estado: str, timestamp: datetime.datetime = None):
        session = self.Session()
        saga_log = SagaLog(
            id_saga=str(id_saga),
            paso=paso,
            estado=estado,
            timestamp=timestamp or datetime.datetime.utcnow()
        )
        session.add(saga_log)
        session.commit()
        session.close()

    def obtener_estado(self, id_saga: uuid.UUID):
        session = self.Session()
        logs = session.query(SagaLog).filter_by(id_saga=str(id_saga)).order_by(SagaLog.paso).all()
        session.close()
        return logs