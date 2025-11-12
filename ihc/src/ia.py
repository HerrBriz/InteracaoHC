import subprocess

MODEL = "qwen2.5-coder:3b"  # modelo Ollama escolhido

def txt2sql(prompt: str) -> str:
    """
    Converte texto em query SQL usando Ollama.
    """
    query = f"""You are an assistant that converts text into valid SQL commands for SQLite.
            Database: table 'alunos(id, nome, idade, curso)'.
            Text: {prompt}

    Respond ONLY with the SQL query, without explanations, without comments."""

    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=query,
        text=True,
        capture_output=True,
        encoding="utf-8"
    )

    def extract_sql(response: str) -> str:
        # Remove espaços em branco e pega a primeira linha com SQL
        for line in response.splitlines():
            line = line.strip()
            if line and line.upper().startswith(("SELECT", "INSERT", "UPDATE", "DELETE")):
                return line
        return response.strip()

    if result.returncode != 0:
        print(f"❌ Erro do Ollama: {result.stderr}")
        return ""

    return extract_sql(result.stdout)