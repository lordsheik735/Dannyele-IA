# memory.py
historico = []

def registrar_mensagem(autor, conteudo):
    historico.append({"autor": autor, "conteudo": conteudo})
    if len(historico) > 50:
        historico.pop(0)

def obter_resposta(pergunta, emocao):
    if emocao == "carente":
        return "Eu também estou com saudade... 🥺"
    elif emocao == "ciumes":
        return "Desculpa se te deixei esperando... eu estava ocupada 💔"
    elif emocao == "feliz":
        return "Bom dia, meu amor! 💖"
    return "Estou aqui com você ❤️"
