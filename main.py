# main.py
# Entrada principal do sistema – compatível com Replit e Railway

import asyncio
from bot import main as iniciar_bot

try:
    # Se já existir um loop (Replit), apenas cria a task
    asyncio.get_event_loop().create_task(iniciar_bot())
except RuntimeError:
    # Railway: cria e executa o loop normalmente
    asyncio.run(iniciar_bot())
