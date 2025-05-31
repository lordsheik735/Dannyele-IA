# cron_internal.py
def verificar_ocupacao():
    return "Estou no trabalho agora, mas posso te responder rapidinho."

def mensagem_rotina(evento):
    if evento == "bom_dia":
        return "Bom dia, meu amor! Dormiu bem? ☀️"
    elif evento == "boa_noite":
        return "Boa noite, durma bem... Vou sonhar com você 😴"
    return ""
