import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
from db import init_db, executar_sql

# Gera SQL com Ollama
def ollama_generate(prompt: str, model: str = "qwen2.5-coder:3b") -> str:
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        capture_output=True
    )
    return result.stdout.decode("utf-8").strip()

# Converte texto natural para SQL e executa
def text2sql(question: str):
    prompt = f"""
    Você é um gerador de SQL para SQLite.
    Regras:
    - Responda SOMENTE com a query SQL válida.
    - NÃO adicione ```sql ou markdown.
    - NÃO explique, apenas forneça a query.
    - Use apenas a tabela 'alunos' com as colunas: id, nome, idade, curso.
    
    Pergunta: {question}
    """
    sql_query = ollama_generate(prompt)
    results = executar_sql(sql_query)
    return sql_query, results

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! Sou um bot que transforma linguagem natural em SQL usando o Ollama.\n"
        "Por exemplo: 'Mostre todos os alunos de Computação'."
    )

# Handler de mensagens
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text
    await update.message.reply_text("Gerando SQL... (aguarde um momento)")

    sql_query, results = text2sql(question)
    response = f"SQL gerado:\n{sql_query}\n\nResultado:\n{results}"
    await update.message.reply_text(response)

# Inicialização do bot
if __name__ == "__main__":
    init_db()
    app = ApplicationBuilder().token("SEU_TOKEN_DO_TELEGRAM").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot iniciado!")
    app.run_polling()
