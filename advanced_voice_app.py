import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyowm
import pytz

#initialize text-to-speech engine
engine = pyttsx3.init()

#set up email configuration
EMAIL_PASSWORD = 'lindelanimalinga95@gmail.com'
EMAIL_PASSWORD = 'muntuza@0101'

#speech recognition
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print("Sorry, I could not understand that.")
        return ""

#talk function
def talk(text):
    engine.say(text)
    engine.runAndWait()

#send email function
def send_email(to, subject, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_PASSWORD, EMAIL_PASSWORD)
        message = f'Subject: {subject}\n\n{content}'
        server.sendmail(EMAIL_PASSWORD, to, message)
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(e)
        print("Failed to send email.")

#weather updates function
def get_weather():
    owm = pyowm.OWM('9e2b1cd1be621688034a20f11a64471d')
    city = 'johannesburg'
    observation = owm.weather_manager().weather_at_place(city)
    wt = observation.weather
    temp = wt.temperature('celsius')['temp']
    status = wt.status
    return f"The weather in {city} is {status} with a temperature of {temp} degrees Celsius."

#execution tasks
def execute_task(query):
    if 'send email' in query:
        talk("Whom do you want to send the email to?")
        #prompt user to input reciepent email address
        recipient = input('Recipient: ', )
        talk("What is the subject of the email?")
        #prompt user to input subject of the email
        subject = input('Subject: ', )
        talk("What should be the content of the email?")
        #prompt user to say what the email is about or the content of the email
        content = recognize_speech()
        #prompt app to send email 
        send_email(recipient, subject, content)
        return "Email sent successfully!"
    #user gets weather through this code snippet
    elif 'weather' in query:
        return get_weather()
    elif 'search' in query:
        talk("What do you want me to search for?")
        #prompt user to search for what they want to search for
        search_query = recognize_speech()
        #make use of google search url for results
        search_url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(search_url)
        return f"Here are the search results for {search_query}."
    elif 'open youtube' in query:
        #prompt user to open youtube
        webbrowser.open("https://www.youtube.com") #url used for testing purposes
        return "Opening YouTube..."
    elif 'open google' in query:
        #prompt user to open google
        webbrowser.open("https://www.google.com") #url used for testing purposes
        return "Opening Google..."
    elif 'time' in query:
        #provide user with current time
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."
    elif 'quit' in query:
        #prompts user to exit program
        talk("Goodbye!")
        exit()
    else:
        try:
            talk("Searching...")
            result = wikipedia.summary(query, sentences=2)
            return result
        except Exception as e:
            return "I'm sorry, I couldn't find any information on that."

#main motherboard function
def main():
    talk("Hello! How can I help you today?")
    #continue so long the user quits the program
    while True:
        query = recognize_speech()
        if 'assistant' in query:
            query = query.replace("assistant", "")
        response = execute_task(query)
        print("Response:", response)
        talk(response)

if __name__ == "__main__":
    main()