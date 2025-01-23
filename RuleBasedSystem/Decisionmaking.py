def decision_making():
    time = float(input("Enter the current time : ").strip())
    weekday = input("Is it a weekday? (yes/no): ").strip().lower()
    weather = input("What is the weather like? (sunny/rainy): ").strip().lower()

    if 6 <= time <= 8 and weekday == "yes":
        return "It's time to go to work."
    elif 12 <= time <= 13:
        return "It's time for lunch."
    elif 21 <= time <= 22:
        return "It's time to go to bed."
    elif weekday == "no" and weather == "sunny":
        return "Go for a walk."
    else:
        return "No specific action for this time."


decision = decision_making()
print(decision)
