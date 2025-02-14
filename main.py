from fastapi import FastAPI, Depends
from utils import commom_verificacao_api_token
from routers import llm_router
from fastapi.middleware.cors import CORSMiddleware

description = """
    API FastAPI - Trabalho Final contendo endpoints com uso de LLM
"""


app = FastAPI(
    title="API FastAPI - Trabalho Final",
    description="""
    API desenvolvida durante as aulas de API - FastAPI, 
    contendo endpoints de exemplo de uso com LLM, 
    API para extrair informações de relatos de conversas com clientes e 
    formatá-las para importação em um banco de dados.
    """,
    version="0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Carlos Miqui",
        "url": "http://github.com/carlosmiqui/",
        "email": "carlosmiqui@discente.ufg.br",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    dependencies=[Depends(commom_verificacao_api_token)]
) #dependencias globais - usar API_TOKEN - para todos os endpoints



# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (útil para desenvolvimento)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os headers
)

app.include_router(llm_router.router)