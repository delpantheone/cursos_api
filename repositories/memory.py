from dataclasses import dataclass, field
from domain.aluno import Aluno
from domain.curso import Curso

@dataclass
class MemoryDB:
    alunos_por_id: dict[int, Aluno] = field(default_factory=dict[int, Aluno])
    cursos_por_codigo: dict[int, Curso] = field(default_factory=dict[int, Curso])
    next_aluno_id: int = 0
    next_curso_codigo: int = 0

db = MemoryDB()