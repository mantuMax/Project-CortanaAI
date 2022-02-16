# Cortana AI - v0.0

"""
Developer: Starboy
Purpose: Cortana AI for a 'Sci-Fi' dream of mine...
Date: 12022.02.15.21:35
"""

import pyttsx3
import speech_recognition as source1
import datetime
import os
import webbrowser
import random


# username
username = "Starboy"
ai_name = "Stargirl"

# voice_engine
voice_engine = pyttsx3.init('sapi5')  # object creation, voice_engine
# voice_engine.say('Hello World')

# voice_engine_voice
voice_engine_voice = voice_engine.getProperty('voices')
# print(voice_engine_voice[1].id)
voice_engine.setProperty('voice', voice_engine_voice[2].id)

# voice_engine_rate
voice_engine_rate = voice_engine.getProperty('rate')
# print(voice_engine_rate)
voice_engine.setProperty('rate', 210)


def speak(audio):  # A speak function(), which takes audio as it's parameter
    voice_engine.say(audio)
    voice_engine.runAndWait()


# Greeting message
def greeting():
    datetime.datetime.now()
    # print(time1)
    time_in_hour = int(datetime.datetime.now().hour)
    # print(time_in_hour)
    if (time_in_hour > 0 and time_in_hour < 12):
        print(f"Hello {username}, Good Morning :)\n")

    elif time_in_hour > 12 and time_in_hour < 16:
        print(f"Hello {username}, Good Afternoon :)\n")
    else:
        print(f"Hello {username}, Good Evening :)\n")

    print("I'm here...")  # Ultimate statements
    speak("I'm here... ")


def processCommand():
    """
    It processes voice command from microphone & returns result of the command !
    """
    command = source1.Recognizer()
    with source1.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1.5
        audio = command.listen(source)

    # Executing Query
    try:
        print('Recognizing...')
        query = command.recognize_google(audio, language='en-us')
        print(f"You said; {query}\n")

    except Exception:
        return 'None'

    return query


# Ultimate-Function
attempt = 1
if __name__ == "__main__":
    greeting()
    # logic
    while True:
        query = processCommand().lower()

        # base-commands
        # attempt-limit
        if attempt == 6:
            print("Looking Forward To Help You ...")
            speak("Looking Forward To Help You ...")
            exit()

