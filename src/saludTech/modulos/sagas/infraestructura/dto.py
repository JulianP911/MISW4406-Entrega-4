from saludTech.config.db import db
import uuid
import datetime


Base = db.declarative_base()

class SagaLog(db.Model):
    __tablename__ = "saga_log"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    id_saga = db.Column(db.String, default=lambda: str(uuid.uuid4()))
    paso = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)