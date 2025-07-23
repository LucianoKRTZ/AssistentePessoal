import speech_recognition as sr
import pyaudio
import os

class Tools:
    def __init__(self):
        pass

    def listen(self):

        dataReturn = {
            'status': False,
            'text': ''
        }
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio, language="pt-BR")
            dataReturn['text'] = text
            dataReturn['status'] = True
        except sr.UnknownValueError:
            dataReturn['text'] = 'Desculpa, não entendi'
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            dataReturn['text'] = 'Não pude processar o aúdio, reinicie a aplicação'
            print(f"Could not request results; {e}")

        return dataReturn

if __name__ == "__main__":
    tools = Tools()
    tools.listen()