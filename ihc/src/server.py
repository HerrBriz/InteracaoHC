from mcp.server.fastmcp import FastMCP
from db import init_db, executar_sql, add_data, read_data
from ia import txt2sql

mcp = FastMCP("demo.db")

@mcp.tool()
def tool_add_data(query: str):
    return add_data(query)

@mcp.tool()
def tool_read_data(query: str = "SELECT * FROM alunos"):
    return read_data(query)

if __name__ == "__main__":
    init_db()
    print("🚀 Sistema TXT2SQL com Ollama + SQLite iniciado!")
    print("Digite uma pergunta em texto (ou 'sair' para encerrar).")

    while True:
        comando = input("\n💬 Pergunta: ")
        if comando.lower() == "sair":
            break

        sql_query = txt2sql(comando)
        print(f"\n🔎 Query gerada pelo Ollama: {sql_query}")

        try:
            resultados = executar_sql(sql_query)
            if resultados:
                print("📊 Resultados:")
                for r in resultados:
                    print(r)
            else:
                print("⚠️ Nenhum resultado encontrado.")
        except Exception as e:
            print("❌ Erro ao executar query:", e)