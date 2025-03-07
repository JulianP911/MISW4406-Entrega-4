from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
import datetime


Base = db.declarative_base()

class SagaLog(Base):
    __tablename__ = "saga_log"

    id_saga = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    paso = Column(Integer, nullable=False)
    estado = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)