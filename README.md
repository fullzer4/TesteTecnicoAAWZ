<div align="center">

  # Teste Tecnico AAWZ

  <img src="./log.png"><br>

  [![Python application](https://github.com/fullzer4/TesteTecnicoAAWZ/actions/workflows/tests.yml/badge.svg)](https://github.com/fullzer4/TesteTecnicoAAWZ/actions/workflows/tests.yml)
  
</div>

<div align="left">

  ## Documentacao

  Neste teste tecnico fiz os scripts pedidos ...(texto) e tambem fiz um backend com testes automatizados para testar as rotas

  <h3>Scripts</h3>

  Para executar as automacoes criadas siga os passos abaixo:

  -  Instale as dependencias do projeto
  
  ```bash
    pip install -r requuirements.txt
  ```

  - Rodar a etapa 1

  ```bash
    python ./scripts/test1.py
  ```

  - Rodar a etapa 2

 ```
  python ./scripts/test2.py
 ```

  ### Backend

  Temos 2 formas de rodar o backend onde tem as rotas:

  - /payment - method POST ( para calcular o pagamento das comissoes a serem pagas atraves de .csv)
  - /partnership - method POST ( para extrair o nome de cada socio e o numero de cotas atraves de .docx )
  - /verify - method POST ( para verificar o pagamento efetuado das comissoes atraves de .csv e json ) 
  
</div>
