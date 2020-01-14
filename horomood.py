my_list = { 
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


zodiac = input("Hello. Please enter one of three zodiac signs: aquarius, cancer, and libra\n\n")
mood = input("Please enter one of three moods: hungry, angry, and sad\n\n")


new = zodiac + mood

print(my_list[new])
