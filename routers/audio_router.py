from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from models import NomeGrupo, TranscricaoAudio
from utils import obter_logger_e_configuracao, transcrever_audio
from typing import Annotated

logger = obter_logger_e_configuracao()

router = APIRouter()

FORMATOS_SUPORTADOS = ["m4v", "mp3", "mp4", "mpeg"]

@router.post(
    "/V1/transcrever_audio",
    summary="Transcreve um arquivo de áudio para texto.",
    description="""
    Recebe um arquivo de áudio e retorna o texto transcrito.
    FORMATOS_SUPORTADOS = ["m4v", "mp3", "mp4", "mpeg"]
   """,
   tags=[NomeGrupo.llm],
    response_model=TranscricaoAudio,
)
async def transcrever_audio_endpoint(
    audio_file: Annotated[UploadFile, File(description="Arquivo de áudio para transcrição")]
):
    """
    Endpoint para transcrição de áudio.

    Recebe um arquivo de áudio e retorna o texto transcrito.

    FORMATOS_SUPORTADOS = ["flac", "m4a", "mp3", "mp4", "mpeg", "mpga", "oga", "ogg", "wav", "webm"]
    """
    logger.info(f"Arquivo de áudio recebido: {audio_file.filename}")
    try:
        texto_transcrito = await transcrever_audio(audio_file)
        logger.info(f"Áudio transcrito com sucesso: {texto_transcrito}")
        return TranscricaoAudio(texto_transcrito=texto_transcrito)
    except Exception as e:
        logger.error(f"Erro ao transcrever áudio: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    