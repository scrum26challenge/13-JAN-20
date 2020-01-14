import requests
from pprint import pprint

def weather(city):

    try:
        data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=8e21d032bbe0126065706ac69e0caa42").json()
        weather_id = data['weather'][0]['id']
    except:
        pass

    color_codes = {
        2: "purple",
        3: "yellow",
        5: "green",
        6: "red",
        7: "white",
        8: "blue"
    }
    return color_codes[weather_id//100]

combinations = { 
    "aquariushungry": "green",
    "aquariusangry": "teal",
    "aquariussad": "blue",
    "cancerhungry": "red",
    "cancerangry": "yellow",
    "cancersad": "orange",
    "librahungry": "black",
    "libraangry": "blue",
    "librasad": "white"
}

while True:
    zodiac = input("\nWhich is your zodiac sign: aquarius, cancer, or libra?\n\n")
    mood = input("\nHow are you feeling today, hungry, angry, or sad?\n\n")
    zodiac_mood = zodiac + mood

    city = input("\nIn what city are you? \n\n")
    try:
        code = weather(city)
    except:
        print("I couldn't find your city. Please try again!")

    try:
        print("\n You should wear", combinations[zodiac_mood], "and", code,".\n")
        break
    except:
        print("I couldn't understand your input. Please try again!")

  
  
