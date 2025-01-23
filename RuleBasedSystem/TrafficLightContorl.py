def traffic_light_control():
    light_color = input("Enter the current traffic light color (red/green/yellow): ").strip().lower()
    pedestrian_button_pressed = input("Has the pedestrian button been pressed? (yes/no): ").strip().lower()

    if light_color == "red":
        return "Cars must stop."
    elif light_color == "green":
        return "Cars can go."
    elif light_color == "yellow":
        return "Cars must slow down and prepare to stop."
    elif pedestrian_button_pressed == "yes":
        return "The light will turn red after a short delay."
    else:
        return "Invalid input."
    
traffic_action = traffic_light_control()
print(traffic_action)
