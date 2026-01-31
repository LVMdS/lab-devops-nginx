from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base
import os

# 1. Configuração do Banco de Dados
# O Python pega esses valores das Variáveis de Ambiente do Docker
DB_USER = os.getenv("DB_USER", "usuario_padrao")
DB_PASS = os.getenv("DB_PASSWORD", "senha_padrao")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "invidious") # Usando o banco existente

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

# 2. Conectando
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 3. Criando a Tabela (Modelo)
class Tarefa(Base):
    __tablename__ = "minhas_tarefas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    status = Column(String, default="Pendente")

# Cria a tabela no banco se ela não existir
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Função para pegar uma sessão do banco a cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo de dados para receber no POST (Validação)
class TarefaSchema(BaseModel):
    titulo: str

# --- ROTAS DA API ---

@app.get("/")
def home():
    return {"mensagem": "API conectada ao Banco de Dados! 🐘"}

@app.post("/tarefas/")
def criar_tarefa(tarefa: TarefaSchema, db: Session = Depends(get_db)):
    nova_tarefa = Tarefa(titulo=tarefa.titulo)
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

@app.get("/tarefas/")
def listar_tarefas(db: Session = Depends(get_db)):
    return db.query(Tarefa).all()
