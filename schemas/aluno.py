from pydantic import BaseModel, EmailStr

class AlunoBase(BaseModel):
    nome: str
    email: EmailStr

class AlunoCreate(AlunoBase):
    pass

class AlunoOut(AlunoBase):
    id: int