from sqlite3 import connect, Error

def init_db():
    conn = None
    try:
        conn = connect('demo.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                curso TEXT NOT NULL
            )
        ''')
        conn.commit()
        # Insere dados pré-existentes
        insert_initial_data()
    except Error as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()

def insert_initial_data():
    """Insere dados iniciais na tabela alunos"""
    conn = None
    try:
        conn = connect('demo.db')
        cursor = conn.cursor()
        
        # Verifica se já existem dados
        cursor.execute("SELECT COUNT(*) FROM alunos")
        if cursor.fetchone()[0] > 0:
            return
        
        # Dados pré-existentes
        dados = [
            ("Ana", 20, "Engenharia"),
            ("Bruno", 22, "Direito"),
            ("Carla", 19, "Computação"),
            ("João", 21, "Medicina"),
            ("Astride", 21, "Computação"),
            ("Hans", 21, "Medicina")
        ]
        
        cursor.executemany(
            "INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)",
            dados
        )
        conn.commit()
        print("✓ Dados iniciais inseridos com sucesso.")
    except Error as e:
        print(f"Erro ao inserir dados iniciais: {e}")
    finally:
        if conn:
            conn.close()

def add_data(query: str):
    conn = None
    try:
        conn = connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Erro ao adicionar dados: {e}")
        return None
    finally:
        if conn:
            conn.close()

def read_data(query: str):
    conn = None
    try:
        conn = connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(f"Erro ao ler dados: {e}")
        return None
    finally:
        if conn:
            conn.close()

def executar_sql(query: str):
    conn = None
    try:
        conn = connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return cursor.fetchall()
    except Error as e:
        print(f"Erro ao executar query: {e}")
        return None
    finally:
        if conn:
            conn.close()