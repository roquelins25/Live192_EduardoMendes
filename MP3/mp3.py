import os
from gtts import gTTS

pasta_save = os.path.join(os.path.expanduser("~"),"Downloads")

textos = {
    "servio": "Potrebno je da naš tim ima veći pritisak da ispuni cilj. Danas izgleda da su svi opušteni i ne daju svoj maksimum.",
    "ingles": "I need our team to have more pressure to meet the goal. Today, it seems like everyone is slacking off and not giving their best.",
    "espanhol": "Necesito que nuestro equipo tenga más presión para alcanzar la meta. Hoy parece que todos están flojeando y no están dando el máximo.",
    "portugues": "textanto essa biblioteca"
}

for idioma, texto in textos.items():
    tts = gTTS(
    text=texto, 
    lang='en' if idioma == 'ingles' else 'es' if idioma == 'espanhol' else 'pt',  # Corrigido para 'pt'
    tld='com.br' if idioma == 'portugues' else 'com'  # 'com.br' para português brasileiro
)
    arquivo = os.path.join(pasta_save,f"{idioma}.mp3")
    tts.save(arquivo)
    print(f"Áudio salvo: {arquivo}")
