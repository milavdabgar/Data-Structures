CapitalState = {
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur",
    "Maharashtra": "Mumbai",
    "Madhya Pradesh": "Bhopal",
    "Goa": "Panaji",
    "Karnataka": "Bengaluru",
    "Uttar Pradesh": "Lucknow"
}

print(CapitalState)

for key, value in CapitalState.items():
    Answer = input("What is the capital of " + key + "? ")

    if Answer == value:
        print("Correct Answer")
    else:
        print("Not Correct Answer")
