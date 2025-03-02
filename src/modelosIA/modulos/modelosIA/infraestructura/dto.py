from modelosIA.config.db import db
from sqlalchemy.dialects.postgresql import UUID

import uuid

Base = db.declarative_base()

class Dataframe(db.Model):
    __tablename__ = "dataframe"
    id = db.Column(
        "id", db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True
    )
    url = db.Column(db.String(255), nullable=False)
    dataframe = db.Column(db.String(1024), nullable=False)
