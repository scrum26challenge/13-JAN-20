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
    zodiac = input("Please enter one of these zodiac signs: aquarius, cancer, or libra\n\n")
    mood = input("Please enter one of these moods: hungry, angry, or sad\n\n")
    zodiac_mood = zodiac + mood
    print("\nYou should wear", combinations[zodiac_mood],"\n\n")
