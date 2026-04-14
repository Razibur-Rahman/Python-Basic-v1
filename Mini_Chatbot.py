# datetime module import for time,date,day
import datetime

# infinite loop to keep chatbot running
while True:
    msg = input("you: ").lower() #user input converted to lowercase

    # greeting response
    if "hello" in msg or "hi" in msg:
        print("Bot: hi there! how can i help you.")
    
    # name question response
    elif "your name" in msg:
        print("Bot: I am a python chatbot")

    # how are you response
    elif "how are you" in msg:
        print("Bot: I'm just code, but I'm fine")

    # show current time
    elif "time" in msg:
        now = datetime.datetime.now()  # get current date & time
        print("Bot: Time is:",now.strftime("%H:%M")) # format hour:minute

    # show current day name
    elif "day" in msg:
        now = datetime.datetime.now()
        print("Bot:",now.strftime("%A")) # full weekday name
    
    # exit chatbot
    elif msg in ["bye","exit","quit"]:
        print("Bot: Goodbye!")
        break

    # default response if no match
    else:
        print("Bot: I don't understand")