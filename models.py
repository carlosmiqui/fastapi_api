from enum import Enum
from pydantic import BaseModel
from typing import Optional


class NomeGrupo(str, Enum):
    """
    Enumeração que representa os nomes dos grupos.

    Atributos:
        operacoes (str): Retorna o nome do grupo de operações matemáticas simples.
        teste (str): Retorna o nome do grupo de teste.
    """
    llm = "LLM"

class RelatoConversa(BaseModel):
    data_conversa: str  # Formato: "AAAA-MM-DD HH:MM:SS"
    identidade_cliente: str
    identidade_atendente: str
    resumo_assunto: str
    valor_orcamento: float
    forma_pagamento: str  # Removido Enum para permitir texto livre
    informacoes_organizadas: list[str]
    instrucoes_proximo_passo: str
    
class EstrategiaConversao(BaseModel):
    estrategia: str
    
class TranscricaoAudio(BaseModel):
    texto_transcrito: str
    
    
    