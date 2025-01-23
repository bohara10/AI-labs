def smart_home_automation():
    temperature = float(input("Enter the current temperature in °C: ").strip())
    is_dark = input("Is it dark outside? (yes/no): ").strip().lower()
    someone_at_home = input("Is someone at home? (yes/no): ").strip().lower()
    security_armed = input("Is the security system armed? (yes/no): ").strip().lower()
    door_opened = input("Is a door opened? (yes/no): ").strip().lower()

    # Rule 1: Temperature control
    if temperature < 18:
        print("Turn on the heater.")
    
    # Rule 2: Temperature control
    if temperature > 25:
        print("Turn on the air conditioner.")
    
    # Rule 3: Lighting control
    if is_dark == "yes" and someone_at_home == "yes":
        print("Turn on the lights.")
    
    # Rule 4: Security system
    if security_armed == "yes" and door_opened == "yes":
        print("Sound the alarm.")

# Example usage:
smart_home_automation()
