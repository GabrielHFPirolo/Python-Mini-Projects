from dataclasses import dataclass
from tag import Categoria
@dataclass
class Transação:
  valor: float
  descrição: str
  categoria: Categoria