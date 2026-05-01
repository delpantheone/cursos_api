from repositories.memory import db
from domain.aluno import Aluno
from domain.curso import Curso
from typing import ValuesView

class ErrosValidacao(Exception):
    def __init__(self, messages: list[str]) -> None:
        self.messages = messages

def criar_aluno(nome: str, email: str) -> Aluno:
    aluno = Aluno(db.next_aluno_id, nome, email)
    db.alunos_por_id[aluno.id] = aluno
    db.next_aluno_id += 1
    return aluno

def listar_alunos() -> ValuesView[Aluno]:
    return db.alunos_por_id.values()

def criar_curso(titulo: str, preco: float, tipo: int, desconto_percentual: float) -> Curso:
    curso = Curso(db.next_curso_codigo, titulo, preco, tipo, desconto_percentual)
    db.cursos_por_codigo[curso.codigo] = curso
    db.next_curso_codigo += 1
    return curso

def listar_cursos() -> ValuesView[Curso]:
    return db.cursos_por_codigo.values()

def buscar_curso(codigo: int) -> Curso:
    if not (curso := db.cursos_por_codigo.get(codigo)):
        raise ErrosValidacao([f"O curso com o código {codigo} não foi encontrado no sistema"])
    return curso

def atualizar_preco(codigo: int, novo_preco: float) -> Curso:
    curso = buscar_curso(codigo)
    curso.preco = novo_preco
    return curso

def buscar_preco_curso(codigo: int) -> float:
    if not (curso := buscar_curso(codigo)):
        raise ErrosValidacao([f"O curso com o código {codigo} não foi encontrado no sistema"])
    return curso.preco_final()