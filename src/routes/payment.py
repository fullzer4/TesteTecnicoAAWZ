import csv
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
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
            df['Comissao_Gerente'] = df.apply(lambda row: row['Comissao'] * 0.10 if float(row['Comissao']) >= 1500 else 0, axis=1)
            df['Canal_Online'] = df['Canal de Venda'] == 'Online'
            df['Comissao_Marketing'] = df.apply(lambda row: row['Comissao'] * 0.20 if row['Canal_Online'] else 0, axis=1)
            df['Valor_Pago'] = df['Comissao'] - df['Comissao_Gerente'] - df['Comissao_Marketing']
            
            data = df[['Nome do Vendedor', 'Comissao', 'Valor_Pago']].to_dict()
            
            return {"processed_data": data}
        
        except Exception:
            return JSONResponse(status_code=400, content={"error": "Erro ao processar o arquivo CSV"})

    else:
        return JSONResponse(status_code=400, content={"error": "Apenas arquivos .csv são permitidos"})
