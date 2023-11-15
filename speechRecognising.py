import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def jarvis():
    speak("Hello, Sir. How can I assist you today?")

    while True:
        command = listen()

        if "stop" in command:
            speak("Goodbye, Sir.")
            break
        elif "introduce yourself" in command:
            speak("I am your personal assistant, a simple version inspired by Jarvis.")
        else:
            speak("Sorry, I'm not programmed for that command.")

if __name__ == "__main__":
    jarvis()
