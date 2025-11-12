from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
from db import init_db, executar_sql
from ia import txt2sql  # Importando a função txt2sql

# Converte texto natural para SQL e executa
def text2sql(question: str):
    sql_query = txt2sql(question)  # Usando a função txt2sql diretamente
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
    # Formata o resultado para exibição
    if results is None:
        result_str = "❌ Erro ao executar a consulta ou consulta inválida."
    elif isinstance(results, list) and len(results) == 0:
        result_str = "⚠️ Nenhum resultado encontrado."
    else:
        # Formata lista de tuplas para string legível
        result_str = "\n".join([str(row) for row in results])

    response = f"SQL gerado:\n{sql_query}\n\nResultado:\n{result_str}"
    await update.message.reply_text(response)

# Inicialização do bot
if __name__ == "__main__":
    init_db()
    app = ApplicationBuilder().token("TOKEN_AQUI").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot iniciado!")
    app.run_polling()