# Projeto IHC - Sistema de Consulta e Adição de Dados

Este projeto implementa um sistema que permite a consulta e adição de dados em um banco de dados SQLite, utilizando um servidor MCP. O sistema é capaz de converter perguntas em texto em consultas SQL, facilitando a interação do usuário com o banco de dados.

## Estrutura do Projeto

```
ihc
├── src
│   ├── server.py        # Ponto de entrada da aplicação, gerencia o servidor e a interação com o usuário.
│   ├── db.py            # Implementações das funções para interagir com o banco de dados.
│   ├── ia.py            # Função que converte perguntas em texto em consultas SQL.
│   └── config.py        # Configurações do projeto, como parâmetros de conexão.
├── demo.db              # Banco de dados SQLite onde os dados são armazenados.
├── requirements.txt     # Dependências do projeto.
└── README.md            # Documentação do projeto.
```

## Funcionalidades

- **Adicionar Dados**: Permite que o usuário adicione novos registros ao banco de dados.
- **Ler Dados**: O usuário pode consultar os dados armazenados no banco de dados.
- **Executar Consultas SQL**: O sistema permite a execução de consultas SQL personalizadas.

## Como Executar o Projeto

1. **Instalação das Dependências**:
   Execute o seguinte comando para instalar as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```

2. **Inicialização do Banco de Dados**:
   O banco de dados `demo.db` será criado automaticamente ao executar o servidor pela primeira vez.

3. **Executar o Servidor**:
   Para iniciar o servidor, execute o seguinte comando:
   ```
   python src/server.py
   ```

4. **Interação com o Usuário**:
   Após iniciar o servidor, você poderá fazer perguntas em texto. O sistema converterá suas perguntas em consultas SQL e retornará os resultados.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork do repositório e envie suas alterações através de um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.