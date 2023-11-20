# APS 01 - API REST com Postgres

Integrantes: 
- Alberto Zamarchi
- Lorenzo Battistoni
- Matheus Eduardo

## Dependecias do Projeto

''' shell
poetry add fastapi
poetry add sqlmodel
poetry add uvicorn
poetry add psycopg2-binary

'''

##Iniciando o servidor de HTTP

'''shell
uvicorn src.server:app -- reload
'''