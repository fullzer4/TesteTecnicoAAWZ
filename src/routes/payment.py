import csv
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from numpy import record
import pandas as pd

router = APIRouter()

def clean(value) -> float:
    return float(value.replace('R$ ', '').replace('.', '').replace(',', '.'))

@router.post("/payment")
async def payment(file: UploadFile = File(...)):
    if file.filename.endswith(".csv"):
        contents = await file.read()
        
        try:
            decoded_content = contents.decode('utf-8').splitlines()
            csv_reader = csv.DictReader(decoded_content)

            df = pd.DataFrame(csv_reader)
            
            df['Valor da Venda'] = df['Valor da Venda'].apply(clean)

            df['Comissao'] = df['Valor da Venda'] * 0.10

            df['Canal_Online'] = df['Canal de Venda'] == 'Online'

            df['Comissao_Marketing'] = df.apply(lambda row: row['Comissao'] * 0.20 if row['Canal_Online'] else 0, axis=1)

            vendas_agrupadas = df.groupby('Nome do Vendedor')[['Comissao', 'Comissao_Marketing']].sum().reset_index()

            vendas_agrupadas['Comissao_Gerente'] = vendas_agrupadas.apply(lambda row: row['Comissao'] * 0.10 if row['Comissao'] >= 1500 else 0, axis=1)

            vendas_agrupadas['Valor A Ser Pago'] = vendas_agrupadas['Comissao'] - vendas_agrupadas['Comissao_Gerente'] - vendas_agrupadas['Comissao_Marketing']

            data = vendas_agrupadas[['Nome do Vendedor', 'Comissao', 'Valor A Ser Pago']]
            
            return {"data": data.to_dict(orient="records")}
        
        except Exception:
            return JSONResponse(status_code=400, content={"error": "Erro ao processar o arquivo CSV"})

    else:
        return JSONResponse(status_code=400, content={"error": "Apenas arquivos .csv são permitidos"})
