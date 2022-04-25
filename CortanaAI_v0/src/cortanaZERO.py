# Project-CortanaAI, Level 0, Step-2

"""
Developer: Starboy
Purpose: Cortana AI for a 'Sci-Fi' dream of mine...
Date: 12022.02.15.21:35
"""


import pyttsx3
import speech_recognition as source1
import datetime
import os
from cortana_introduction import introduction

# username
username = "Starboy"
ai_name = "Cortana"


# voice_engine
voice_engine = pyttsx3.init("sapi5")       # object creation, voice_engine
# voice_engine.say('Hello World')


# voice_engine_voice
voice_engine_voice = voice_engine.getProperty("voices")

# print(voice_engine_voice[1].id)
voice_engine.setProperty("voice", voice_engine_voice[1].id)

# voice_engine_rate
voice_engine_rate = voice_engine.getProperty("rate")

# print(voice_engine_rate)
voice_engine.setProperty("rate", 200)


def speak(audio):             # A speak function(), which takes audio as it's parameter
    voice_engine.say(audio)
    voice_engine.runAndWait()


# Greeting message
def greeting():
    datetime.datetime.now()

    # print(time1)
    time_in_hour = int(datetime.datetime.now().hour)

    # print(time_in_hour)
    if time_in_hour > 0 and time_in_hour < 12:
        print(f"Hello {username}, Good Morning :)\n")

    elif time_in_hour > 12 and time_in_hour < 16:
        print(f"Hello {username}, Good Afternoon :)\n")

    else:
        print(f"Hello {username}, Good Evening :)\n")

    # Ultimate statements
    print("I'm here... \n")
    speak("I'm here")


def process_command():
    """
    As the name says, It processes voice command from microphone & returns result of the command.

    """
    command = source1.Recognizer()

    with source1.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1.5
        audio = command.listen(source)

    # Executing Query
    try:
        print("Recognizing...")
        query = command.recognize_google(audio, language="en-us")
        print(f"You said; {query}\n")

    except Exception:
        return "Something's not right, Please try again! \n"

    return query


# Ultimate-Function
attempt = 0
if __name__ == "__main__":
    introduction()
    greeting()

    # logic
    try:
        while True:
            query = process_command().lower()
            attempt = attempt + 1

            # base-commands;
            if attempt >= 4:
                print("Looking forward to helping out... \n")
                speak("Looking forward to helping out...")
                break

            # define yourself
            elif "who are you" in query:
                print(
                    f"Hello, I'm {ai_name} & I'm here to help you... \n")
                speak(f"Hello, I'm {ai_name}, and I'm here to help you")
                continue

            # feedback | work required!
            elif "you need to improve" in query:
                print("Sorry for the inconvenience :( \n")
                speak("Sure")
                break

            # date | work required!
            elif "the date" in query:
                current_date = str(os.system("date"))
                print(f"The current date is; {current_date} \n")
                speak(f"The current date is, {current_date}")
                continue

            # time
            elif "the time" in query:
                current_time = datetime.datetime.now().strftime(" %H:%M:%S ")
                print(f"The time is; {current_time} \n")
                speak(f"The time is; {current_time}")
                continue

            # wishing
            elif "good morning" in query:
                print(f"Good morning {username}, have a nice day :) \n")
                speak(f"Good morning {username}, have a nice day")
                continue

            elif "good afternoon" in query:
                print(f"Good afternoon {username}, hope you doing good :) \n")
                speak(f"Good afternoon {username}, hope you doing good")
                continue

            elif "good evening" in query:
                print(
                    f"Good evening {username}, It's time to get refreshed :) \n")
                speak(
                    f"Good evening {username}, It's time to get refreshed")
                continue

            elif "good night" in query:
                print(f"Good Night {username}, Have a nice dream :) \n")
                speak(f"Good Night {username}, Have a nice dream")
                continue

            # exit
            elif "quit" in query:
                print("Okay :) \n")
                speak("Okay")
                break

            elif "exit" in query:
                print("Okay :) \n")
                speak("Okay")
                break

            # ok
            elif "ok" in query:
                print("Alright ;) \n")
                speak("Alright")
                break

            # error-message
            else:
                print("Please Try Again! \n")
                speak("Say again")
                continue

    except KeyboardInterrupt:
        print("\n\n Operation cancelled by the user :( \n")
