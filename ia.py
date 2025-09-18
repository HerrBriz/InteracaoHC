import subprocess

MODEL = "qwen3:4b"  # modelo Ollama escolhido

def txt2sql(prompt: str) -> str:
    """
    Converte texto em query SQL usando Ollama.
    """
    query = f"""
        You are an assistant that converts text into valid SQL commands for SQLite.
        Database: table 'alunos(id, nome, idade, curso)'.
        Text: {prompt}

        Respond ONLY with the SQL query, without explanations, without comments.
        """

    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=query,
        text=True,
        capture_output=True,
        encoding = "utf-8"
    )

    def extract_sql(response: str) -> str:
        # Pega só a primeira linha que parece SQL
        for line in response.splitlines():
            if line.strip().upper().startswith(("SELECT", "INSERT", "UPDATE", "DELETE")):
                return line.strip()
        return response.strip()

    return extract_sql(result.stdout)
