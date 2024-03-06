import docx2txt
import re

def extrair_socios_e_cotas(texto):
    regex_nome = r'(\d+)\. (.+?),'
    regex_cotas = r'detentor(?:a|) de (\d+) cot(?:a|as)'

    nomes = re.findall(regex_nome, texto)
    cotas = re.findall(regex_cotas, texto)

    nomes_filtrados = [nome[1] for nome in nomes if not nome[1].startswith("Sócio")]

    quadro_societario = [(nome.strip(), int(cota)) for nome, cota in zip(nomes_filtrados, cotas)]

    return quadro_societario

texto_contrato = docx2txt.process("./data/partnership.docx")

quadro_societario = extrair_socios_e_cotas(texto_contrato)

print(quadro_societario)
