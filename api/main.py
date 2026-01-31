from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "mensagem": "Olá! Minha primeira API DevOps está viva! 🚀",
        "servidor": socket.gethostname(),
        "status": "sucesso"
    }

@app.get("/soma/{a}/{b}")
def somar(a: int, b: int):
    return {"resultado": a + b}
