Temperature = {"Monday": 41, "Tuesday": 45, "Wednesday": 39,
               "Thursday": 38, "Friday": 43, "Saturday": 48, "Sunday": 33}

print(Temperature)

for key, value in Temperature.items():
    if 40 < value < 50:
        print(key)
