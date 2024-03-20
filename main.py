import requests
import json  # to parse string to dict
import pyttsx3

engine = pyttsx3.init("sapi5")  # sapi5-API provided by Microsoft to use diff voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
if __name__ == '__main__':
    city = input("Enter the name of the city:\n")
    url = f"https://api.weatherapi.com/v1/current.json?key=9caf41771ed6472c989173134241903&q={city}"
    r = requests.get(url)
    # print(r.text)  # type=str
    wdic = json.loads(r.text)  # parsed into dict
    w = wdic["current"]["temp_c"]
    engine.say(f"The current weather in {city} is {w} degrees.")
    engine.runAndWait()
