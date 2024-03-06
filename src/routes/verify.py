import io
import pandas as pd
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np

router = APIRouter()

def clean(value) -> float:
    return float(value.replace('R$ ', '').replace('.', '').replace(',', '.'))

def is_csv(filename: str) -> bool:
    return filename.lower().endswith('.csv')

@router.post("/verify")
async def verify(csv1: UploadFile = File(...), csv2: UploadFile = File(...)):
    try:
        if not is_csv(csv1.filename) or not is_csv(csv2.filename):
            return JSONResponse(status_code=400, content={"error": "Apenas arquivos .csv são permitidos"})

        csv1_contents = await csv1.read()
        csv2_contents = await csv2.read()

        vendas = pd.read_csv(io.StringIO(csv1_contents.decode('utf-8')))
        pagamentos = pd.read_csv(io.StringIO(csv2_contents.decode('utf-8')))

        vendas['Valor da Venda'] = vendas['Valor da Venda'].apply(clean)
        vendas['Comissao'] = vendas['Valor da Venda'] * 0.10
        vendas['Canal_Online'] = vendas['Canal de Venda'] == 'Online'
        vendas['Comissao_Marketing'] = vendas.apply(lambda row: row['Comissao'] * 0.20 if row['Canal_Online'] else 0, axis=1)
        vendas_agrupadas = vendas.groupby('Nome do Vendedor')[['Comissao', 'Comissao_Marketing']].sum().reset_index()
        vendas_agrupadas['Comissao_Gerente'] = vendas_agrupadas.apply(lambda row: row['Comissao'] * 0.10 if row['Comissao'] >= 1500 else 0, axis=1)
        vendas_agrupadas['Valor A Ser Pago'] = vendas_agrupadas['Comissao'] - vendas_agrupadas['Comissao_Gerente'] - vendas_agrupadas['Comissao_Marketing']
        pagamentos['Comissão'] = pagamentos['Comissão'].apply(clean)
        pagamentos_comparacao = pd.merge(pagamentos, vendas_agrupadas, on='Nome do Vendedor', how='left')
        pagamentos_incorretos = pagamentos_comparacao[pagamentos_comparacao['Comissão'] != pagamentos_comparacao['Valor A Ser Pago']]

        for column in pagamentos_incorretos.select_dtypes(include=[np.number]).columns:
            pagamentos_incorretos[column] = pagamentos_incorretos[column].astype(float)

        return {"data": pagamentos_incorretos.to_dict(orient="records")}

    except Exception as e:
        return JSONResponse(status_code=400, content={"error": f"Erro ao processar os arquivos CSV: {str(e)}"})

