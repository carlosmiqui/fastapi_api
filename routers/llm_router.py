from fastapi import APIRouter, Depends, HTTPException
from models import NomeGrupo, RelatoConversa, EstrategiaConversao
from utils import obter_logger_e_configuracao, processar_relato, gerar_estrategia_conversao
from pydantic import BaseModel, Field


logger = obter_logger_e_configuracao()

router = APIRouter()

class RelatoInput(BaseModel):
    relato: str = Field(
        ...,
        description="Relato da conversa (texto formatado, sem limite de formatação)",
        max_length=10000  # Aumentar o limite de caracteres
    )

@router.post(
    "/processar_relato",
    summary="Processa um relato de conversa e retorna um objeto JSON formatado.",
    description="Recebe um relato de conversa em texto, extrai informações relevantes e retorna um objeto JSON para ser importado em um banco de dados.",
    tags=[NomeGrupo.llm],
    response_model=RelatoConversa,
)
async def processar_relato_endpoint(relato_input: RelatoInput):
    logger.info(f"Relato recebido: {relato_input.relato}")
    try:
        relato_processado = processar_relato(relato_input.relato)
        logger.info(f"Relato processado com sucesso: {relato_processado}")
        return relato_processado
    except Exception as e:
        logger.error(f"Erro ao processar relato: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    

@router.post(
    "/gerar_estrategia",
    summary="Gera uma estratégia de conversão a partir dos dados do relato.",
    description="Recebe um objeto JSON com os dados do relato e gera uma estratégia de conversão personalizada para o cliente.",
    tags=[NomeGrupo.llm],
    response_model=EstrategiaConversao,
)
async def gerar_estrategia_endpoint(relato: RelatoConversa):
    logger.info(f"Dados do relato recebidos: {relato}")
    try:
        estrategia = gerar_estrategia_conversao(relato)
        logger.info(f"Estratégia de conversão gerada com sucesso: {estrategia}")
        return estrategia
    except Exception as e:
        logger.error(f"Erro ao gerar estratégia de conversão: {e}")