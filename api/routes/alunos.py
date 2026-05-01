from fastapi import APIRouter, HTTPException, status
from services.cursos_service import (
    # ErrosValidacao,
    criar_aluno,
    listar_alunos,
)

from schemas.aluno import AlunoCreate, AlunoOut

router = APIRouter(prefix="/alunos", tags=["alunos"])

@router.post("", response_model=AlunoOut, status_code=status.HTTP_201_CREATED)
def criar(payload: AlunoCreate):
    try:
        return criar_aluno(**payload.model_dump())
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))

@router.get("", response_model=list[AlunoOut])
def listar():
    try:
        return listar_alunos()
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))