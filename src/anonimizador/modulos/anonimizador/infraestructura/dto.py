from anonimizador.config.db import db
from sqlalchemy.dialects.postgresql import UUID

import uuid

Base = db.declarative_base()

class ImagenMedica(db.Model):
    __tablename__ = "imagen_medica"
    id = db.Column(
        "id", db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True
    )
    url = db.Column(db.String(255), nullable=False)
    fecha_recepcion = db.Column(db.String(255), nullable=False)
    accion = db.Column(db.String(255), nullable=False)
