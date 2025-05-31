# emotion.py
def analisar_emocao(texto):
    if "sinto sua falta" in texto.lower():
        return "carente"
    elif "você sumiu" in texto.lower():
        return "ciumes"
    elif "bom dia" in texto.lower():
        return "feliz"
    return "neutra"
