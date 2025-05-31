# bot.py
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from emotion import analisar_emocao
from memory import registrar_mensagem, obter_resposta
from dotenv import load_dotenv
from cron_internal import verificar_ocupacao, mensagem_rotina
from config import DANNYELE_NOME, USUARIO_NOME

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    emocao = analisar_emocao(texto)
    registrar_mensagem("usuario", texto)
    resposta = obter_resposta(texto, emocao)
    await update.message.reply_text(resposta)

async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    handler = MessageHandler(filters.TEXT & (~filters.COMMAND), responder)
    app.add_handler(handler)
    print(f"🤖 {DANNYELE_NOME} está online e pronta para conversar com {USUARIO_NOME}!")
    await app.run_polling()
