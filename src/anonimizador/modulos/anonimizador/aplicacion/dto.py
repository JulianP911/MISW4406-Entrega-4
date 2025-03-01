from dataclasses import dataclass, field
from anonimizador.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ImagenMedicaDTO(DTO):
    id: str = field(default=None)
    url: str = field(default=None)