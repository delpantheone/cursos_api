from fastapi import APIRouter, HTTPException, status
from services.cursos_service import (
    ErrosValidacao,
    criar_curso,
    listar_cursos,
    buscar_curso,
    atualizar_preco,
    buscar_preco_curso
)

from schemas.curso import CursoCreate, CursoOut

router = APIRouter(prefix="/cursos", tags=["cursos"])

@router.post("", response_model=CursoOut, status_code=status.HTTP_201_CREATED)
def criar(payload: CursoCreate):
    try:
        return criar_curso(**payload.model_dump())
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))

@router.get("", response_model=list[CursoOut])
def listar():
    try:
        return listar_cursos()
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))

@router.get("/{codigo}", response_model=CursoOut)
def obter(codigo: int):
    try:
        return buscar_curso(codigo)
    except ErrosValidacao as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, e.messages)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))

@router.put("/{codigo}/preco", response_model=CursoOut)
def alterar(codigo: int, novo_preco: float):
    try:
        return atualizar_preco(codigo, novo_preco)
    except ErrosValidacao as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, e.messages)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))

@router.get("/{codigo}/preco-final", response_model=float)
def obter_preco(codigo: int):
    try:
        return buscar_preco_curso(codigo)
    except ErrosValidacao as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, e.messages)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))