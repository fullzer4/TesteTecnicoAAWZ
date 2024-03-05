import io
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import docx2txt
import re

router = APIRouter()

def extrair_socios_e_cotas(texto):
    regex_nome = r'(\d+)\. (.+?),'
    regex_cotas = r'detentor(?:a|) de (\d+) cot(?:a|as)'

    nomes = re.findall(regex_nome, texto)
    cotas = re.findall(regex_cotas, texto)

    nomes_filtrados = [nome[1] for nome in nomes if not nome[1].startswith("Sócio")]

    quadro_societario = [{"nome": nome.strip(), "cotas": int(cota)} for nome, cota in zip(nomes_filtrados, cotas)]

    return quadro_societario

@router.post("/partnership")
async def partnership(file: UploadFile = File(...)):
    if file.filename.endswith(".docx"):
        contents = await file.read()
        texto_contrato = docx2txt.process(io.BytesIO(contents))

        quadro_societario = extrair_socios_e_cotas(texto_contrato)
        
        return quadro_societario
    else:
        return JSONResponse(status_code=400, content={"error": "Only .docx files allowed"})

