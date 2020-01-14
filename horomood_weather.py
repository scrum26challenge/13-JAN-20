import requests
from pprint import pprint

def weather(city):
  quote_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=8e21d032bbe0126065706ac69e0caa42").json()
  weather_id = quote_data['weather'][0]['id']
  color_codes = {
        2: "Purple",
        3: "Yellow",
        5: "Green",
        6: "Red",
        7: "White",
        8: "Blue"
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
    zodiac = input("\nPlease enter one of these zodiac signs: aquarius, cancer, or libra\n\n")
    mood = input("\nPlease enter one of these moods: hungry, angry, or sad\n\n")
    zodiac_mood = zodiac + mood

    city = input("\nPlease enter a city: \n\n")
    t = weather(city)
    print("\n You should wear", combinations[zodiac_mood], "and", t, "\n")
    break
  
  
