from dataclasses import dataclass, field
from modelosIA.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ImagenAnonimizadaValidadDTO(DTO):
    id: str = field(default=None)
    url: str = field(default=None)
    validate: bool = field(default=None)