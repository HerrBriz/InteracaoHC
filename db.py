import sqlite3

DB_NAME = "demo.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Cria tabela do zero
    cursor.execute("DROP TABLE IF EXISTS alunos")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        curso TEXT
    )
    """)

    # Insere alguns dados iniciais (se tabela estiver vazia)
    cursor.execute("SELECT COUNT(*) FROM alunos")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
        INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)
        """, [
            ("Ana", 20, "Engenharia"),
            ("Bruno", 22, "Direito"),
            ("Carla", 19, "Computação"),
            ("João", 21, "Medicina"),
            ("Astride", 21, "Computação"),
            ("Hans", 21, "Medicina")
        ])
        conn.commit()

    conn.close()


def executar_sql(query: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(query)

        # Se for SELECT → retorna resultados
        if query.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()
            return rows

        # Se for INSERT / UPDATE / DELETE → aplica commit
        elif query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
            conn.commit()
            return "✅ Operação realizada com sucesso."

        else:
            return "⚠ Query executada, mas sem retorno."

    except Exception as e:
        return f"❌ Erro: {e}"

    finally:
        conn.close()


def add_data(query: str):
    conn = sqlite3.connect(DB_NAME)
    try:
        conn.execute(query)
        conn.commit()
        return True
    except Exception as e:
        return f"❌ Erro: {e}"
    finally:
        conn.close()


def read_data(query: str = "SELECT * FROM alunos"):
    conn = sqlite3.connect(DB_NAME)
    try:
        results = conn.execute(query).fetchall()
        return results
    finally:
        conn.close()
