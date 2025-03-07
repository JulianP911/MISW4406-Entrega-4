from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
import datetime
from saludTech.config.db import db

from saludTech.seedwork.dominio.repositorios import SagaLogRepositorio
from .dto import SagaLog

Base = db.declarative_base()

class SagaLogSQLRepositorio(SagaLogRepositorio):

    def guardar_estado(self, id_saga: uuid.UUID, paso: int, estado: str, timestamp: datetime.datetime = None):
       
        saga_log = SagaLog(
            id_saga=str(id_saga),
            paso=paso,
            estado=estado,
            timestamp=timestamp or datetime.datetime.utcnow()
        )
        db.session.add(saga_log)
        db.session.commit()
        db.session.close()

    def obtener_estado(self, id_saga: uuid.UUID):
        
        logs = db.session.query(SagaLog).filter_by(id_saga=str(id_saga)).order_by(SagaLog.paso).all()
        db.session.close()
        return logs