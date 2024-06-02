import speech_recognition as sr
import time
import os

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {command}")

        if "iniciar" in command.lower():
            print("Comando 'iniciar' reconhecido")
            # Adicione o código para mostrar a tela de login
        elif "me mostre vestidos" in command.lower():
            print("Comando 'me mostre vestidos' reconhecido")
            # Adicione o código para navegar para a página de vestidos
        elif "tire uma foto" in command.lower():
            print("Comando 'tire uma foto' reconhecido")
            # Adicione o código para tirar uma foto
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError:
        print("Erro ao se conectar ao serviço de reconhecimento de voz.")

if __name__ == "__main__":
    while True:
        recognize_speech()
        time.sleep(1)  # Adiciona um pequeno intervalo entre as tentativas
