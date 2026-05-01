from pydantic import BaseModel

class CursoBase(BaseModel):
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: float = 0

class CursoCreate(CursoBase):
    pass

class CursoOut(CursoBase):
    codigo: int