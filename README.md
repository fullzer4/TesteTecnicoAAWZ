<div align="center">

  # Teste Técnico AAWZ

  <img src="./log.png"><br>

  [![Python Tests](https://github.com/fullzer4/TesteTecnicoAAWZ/actions/workflows/tests.yml/badge.svg)](https://github.com/fullzer4/TesteTecnicoAAWZ/actions/workflows/tests.yml)
  
</div>

<div align="left">

  ## Documentação

  Neste teste técnico, foram desenvolvidos os scripts solicitados para o cálculo de comissões, validação de pagamentos e análise de contratos de Partnership. Além disso, foi criado um backend com testes automatizados para verificar as rotas.

  <h3>Scripts</h3>

  Para executar as automações criadas, siga os passos abaixo:

  -  Instale as dependências do projeto:
  
  ```bash
    pip install -r requuirements.txt
  ```

  - Executar a Etapa 1:

  ```bash
    python ./scripts/test1.py
  ```

  - Executar a Etapa 2:

 ```bash
  python ./scripts/test2.py
 ```

  ### Backend

  Existem duas formas de executar o backend, que possui as seguintes rotas:

  - `/payment` - método POST (para calcular o pagamento das comissões a serem pagas através de arquivos .csv)
    Retorna um json com:
    ```
      ['data': [{'Nome do Vendedor': 'Ana Costa', 'Comissao': 450.0, 'Valor A Ser Pago': 450.0}, ...]]
    ```
    
  - `/partnership` - método POST (para extrair o nome de cada sócio e o número de cotas através de arquivos .docx)
    Retorna um json com:
    ```
      ['data': [{'nome': 'João Silva', 'cotas': 20}, {'nome': 'Maria Souza', 'cotas': 15}, ...]]
    ```
    
  - `/verify` - método POST (para verificar o pagamento efetuado das comissões através de dois arquivos .csv)
    Retorna um json com:
    ```
      ['data': [{'Nome do Vendedor': 'João Silva', 'Valor Pago': 100.0, 'Valor Correto': 210.0}, ...]]
    ```

  Como testar de forma automatizada

  - Opção 1: via Uvicorn
  ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --port 8000 --reload

    # em outro terminal

    source venv/bin/activate
    pytest
  ```

  - Opção 2: via Docker
  ```bash
    docker build -t fastapi .
    docker run -d -p 8000:8000 fastapi

    pytest 
  ```

  Para esta opção, é necessário ter o pytest instalado. Caso não tenha, basta executar:

  ```bash
     pip install pytest
  ```

  Como testar as rotas manualmente para verificar as saídas em JSON:

  ```bash
    python ./test/manual/verify.py
    python ./test/manual/partnership.py
    python ./test/manual/payment.py
  ```
   
  
</div>
