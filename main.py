from fastapi import FastAPI

from api.routes.cursos import router as curso_router
from api.routes.alunos import router as aluno_router

app = FastAPI(description="API Online")

app.include_router(curso_router)
app.include_router(aluno_router)