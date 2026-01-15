import sounddevice as sd
import numpy as np
import speech_recognition as sr
import os
from scipy.io.wavfile import write
import tempfile

print("Assistente iniciado...")

def ouvir_microfone():
    fs = 44100
    seconds = 4

    print("Diga alguma coisa...")
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        write(f.name, fs, audio)
        nome_arquivo = f.name

    r = sr.Recognizer()

    with sr.AudioFile(nome_arquivo) as source:
        audio_data = r.record(source)

    try:
        frase = r.recognize_google(audio_data, language="pt-BR")
        frase = frase.lower()
        print("Você disse:", frase)

        if "navegador" in frase or "chrome" in frase:
            os.system("start chrome")
            return False

        elif "excel" in frase:
            os.system("start excel")
            return False

        elif "powerpoint" in frase:
            os.system("start powerpnt")
            return False

        elif "edge" in frase:
            os.system("start msedge")
            return False

        elif "fechar" in frase or "sair" in frase:
            print("Encerrando assistente...")
            return True

    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError:
        print("Erro ao acessar o serviço de reconhecimento.")

    return False


while True:
    if ouvir_microfone():
        break
