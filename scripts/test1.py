import pandas as pd

def clean(value) -> float:
    return float(value.replace('R$ ', '').replace('.', '').replace(',', '.'))

vendas = pd.read_csv('./data/vendas.csv')
pagamentos = pd.read_csv('./data/pagamentos.csv')

# ------- Tarefa 1 -------

vendas['Valor da Venda'] = vendas['Valor da Venda'].apply(clean)

vendas['Comissao'] = vendas['Valor da Venda'] * 0.10

vendas['Comissao_Gerente'] = vendas.apply(lambda row: row['Comissao'] * 0.10 if row['Comissao'] >= 1500 else 0, axis=1)
# ? nunca vau dar 1500

vendas['Canal_Online'] = vendas['Canal de Venda'] == 'Online'

vendas['Comissao_Marketing'] = vendas.apply(lambda row: row['Comissao'] * 0.20 if row['Canal_Online'] else 0, axis=1)

vendas['Valor_Pago'] = vendas['Comissao'] - vendas['Comissao_Gerente'] - vendas['Comissao_Marketing']

# Somar venda total dos vendedor com nomes duplicados

print(vendas[['Nome do Vendedor', 'Comissao', 'Comissao_Gerente', 'Comissao_Marketing', 'Valor_Pago']])

# ------- Tarefa 2 ------
