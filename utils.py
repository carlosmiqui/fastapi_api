import logging
from fastapi import HTTPException
from groq import Groq
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from models import RelatoConversa, EstrategiaConversao
import re
import json

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def obter_logger_e_configuracao():
    """
    Configura o logger padrão para o nível de informação e formato especificado.

    Retorna:
        logging.Logger: Um objeto de logger com as configurações padrões.
    """
    logging.basicConfig(
        level=logging.INFO, format="[%(levelname)s] %(asctime)s - %(message)s"
    )
    logger = logging.getLogger("fastapi")
    return logger

def commom_verificacao_api_token(api_token: str):
    """
    Verifica se o token da API fornecido é válido.

    Args:
        api_token (str): O token da API a ser verificado.

    Raises:
        HTTPException: Se o token da API for inválido, uma exceção HTTP 401 é levantada com a mensagem "Token inválido".
    """
    if api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")

def executar_prompt_groq(prompt: str) -> str:
    """
    Executa um prompt na API Groq e retorna a resposta.

    Args:
        prompt (str): O prompt a ser executado.

    Returns:
        str: A resposta da API Groq.
    """
    client = Groq(api_key=GROQ_API_KEY)

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao executar prompt na Groq: {e}")

def processar_relato(relato: str) -> RelatoConversa:
    """
    Processa um relato de conversa e retorna um objeto JSON formatado.

    Args:
        relato (str): O relato de conversa em texto.

    Returns:
        RelatoConversa: Um objeto Pydantic contendo as informações extraídas do relato.
    """
    logger = logging.getLogger("fastapi")
    data_conversa = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Garantir que o relato seja tratado como uma string
    relato_str = str(relato)

    prompt = f"""
    Analise o seguinte relato de conversa de um cliente de clínica odontológica e extraia as seguintes informações:

    - Data da conversa (AAAA-MM-DD HH:MM:SS): {data_conversa}
    - Identidade do cliente:
    - Identidade do dentista/assistente:
    - Resumo do assunto (cotação de facetas, ortodontia, limpeza, etc.):
    - Valor do orçamento (em R$):
    - Forma de pagamento do orçamento:
    - Informações organizadas sobre o assunto (em bullet points):
    - Instruções sobre o próximo passo (seguir em 7 dias, 30 dias, 6 meses, etc.):

    Relato:
    {relato_str}

    Formate a resposta em um objeto JSON seguindo a estrutura:
    {{
        "data_conversa": "AAAA-MM-DD HH:MM:SS",
        "identidade_cliente": "Nome do Cliente",
        "identidade_atendente": "Nome do Atendente",
        "resumo_assunto": "Assunto",
        "valor_orcamento": 0.00,
        "forma_pagamento": "Forma de Pagamento",
        "informacoes_organizadas": ["Bulletpoint 1", "Bulletpoint 2", ...],
        "instrucoes_proximo_passo": "Instruções"
    }}
    """
    logger.info(f"Prompt enviado para a Groq: {prompt}")
    resposta_groq = executar_prompt_groq(prompt)
    logger.info(f"Resposta da Groq: {resposta_groq}")

    try:
        # Extrair o JSON da resposta da Groq usando regex
        json_match = re.search(r'\{.*\}', resposta_groq, re.DOTALL)
        if json_match:
            resposta_json = json_match.group(0)
            try:
                relato_processado = RelatoConversa.parse_raw(resposta_json)
                return relato_processado
            except Exception as e:
                logger.error(f"Erro ao deserializar JSON: {e}")
                raise HTTPException(
                    status_code=500, detail=f"Erro ao deserializar JSON: {e}"
                )
        else:
            raise ValueError("JSON não encontrado na resposta da Groq")
    except Exception as e:
        logger.error(f"Erro ao processar resposta da Groq: {e}")
        raise HTTPException(
            status_code=500, detail=f"Erro ao processar resposta da Groq: {e}"
        )
        
        
def gerar_estrategia_conversao(relato: RelatoConversa) -> EstrategiaConversao:
    """
    Gera uma estratégia de conversão personalizada para o cliente a partir dos dados do relato.

    Args:
        relato (RelatoConversa): Os dados do relato do cliente.

    Returns:
        EstrategiaConversao: Um objeto Pydantic contendo a estratégia de conversão gerada.
    """
    logger = logging.getLogger("fastapi")

    # Calcular datas para os próximos contatos
    hoje = datetime.now()
    primeiro_contato = hoje + timedelta(days=3)
    segundo_contato = hoje + timedelta(days=10)
    terceiro_contato = hoje + timedelta(days=30)

    prompt = f"""
    Com base nos seguintes dados do relato de um cliente de clínica odontológica, gere uma estratégia de conversão detalhada e personalizada, com datas e instruções claras para a assistente do consultório:

    - Data da conversa: {relato.data_conversa}
    - Identidade do cliente: {relato.identidade_cliente}
    - Resumo do assunto: {relato.resumo_assunto}
    - Valor do orçamento: {relato.valor_orcamento}
    - Forma de pagamento do orçamento: {relato.forma_pagamento}
    - Informações organizadas sobre o assunto: {relato.informacoes_organizadas}
    - Instruções sobre o próximo passo: {relato.instrucoes_proximo_passo}

    A estratégia deve incluir:
    - Um resumo conciso dos interesses e necessidades do cliente.
    - Datas específicas para os próximos contatos (primeiro contato em 3 dias, segundo contato em 10 dias, terceiro contato em 30 dias).
    - Instruções detalhadas sobre o que dizer e como abordar o cliente em cada contato, com o objetivo de agendar uma consulta ou procedimento.
    - Sugestões sobre como personalizar a comunicação para aumentar as chances de conversão.

    Formate a resposta como um texto claro e objetivo, fácil de seguir pela assistente.
    """
    logger.info(f"Prompt enviado para a Groq para gerar a estratégia: {prompt}")
    resposta_groq = executar_prompt_groq(prompt)
    logger.info(f"Resposta da Groq para a estratégia: {resposta_groq}")

    estrategia = EstrategiaConversao(estrategia=resposta_groq)
    return estrategia

