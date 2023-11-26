from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi import FastAPI

from src.config.database import create_db_and_tables
from src.routes.provas_routes import provas_router
from src.routes.resultados_routes import resultados_router

from flask import Flask, request, jsonify

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(provas_router)
app.include_router(resultados_router)


app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

app = Flask(__name__)

# Armazenar as respostas corretas
respostas_corretas = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']

@app.route('/avaliacao', methods=['POST'])
def avaliar_prova():
    dados = request.get_json()

    if 'respostas' not in dados:
        return jsonify({'error': 'As respostas não foram fornecidas'}), 400

    respostas_aluno = dados['respostas']

    if len(respostas_aluno) != len(respostas_corretas):
        return jsonify({'error': 'O número de respostas fornecidas está incorreto'}), 400

    pontuacao = sum(1 for resp_aluno, resp_correta in zip(respostas_aluno, respostas_corretas) if resp_aluno == resp_correta)

    return jsonify({'pontuacao': pontuacao, 'total_pontos': len(respostas_corretas)})

if __name__ == '__main__':
    app.run(debug=True)