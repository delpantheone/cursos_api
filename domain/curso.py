from dataclasses import dataclass

@dataclass
class Curso:
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: float = 0

    def preco_final(self) -> float:
        desconto = self.preco * (self.desconto_percentual / 100)
        return 0 if self.tipo == 1 or (self.preco - desconto) < 0 else self.preco - desconto