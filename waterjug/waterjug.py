j1 = 0  # Initial amount in Jug X
j2 = 0  # Initial amount in Jug Y

x = 4  # Capacity of Jug X
y = 3  # Capacity of Jug Y

print("Initial state: (0, 0)")
print("Capacities: (4, 3)")
print("Goal state: (2, 0 or any number)")

while j1 != 2:  # Continue until Jug X contains exactly 2 liters
    print("\nChoose a rule to apply:")
    print("1: Fill Jug X (if X < 4)")
    print("2: Fill Jug Y (if Y < 3)")
    print("3: Empty Jug X (if X > 0)")
    print("4: Empty Jug Y (if Y > 0)")
    print("5: Transfer water from Jug X to Jug Y (if X > 0)")
    print("6: Transfer water from Jug Y to Jug X (if Y > 0)")

    r = int(input("Enter the rule: "))

    if r == 1:  # Fill Jug X to its full capacity (4 liters)
        j1 = x
    elif r == 2:  # Fill Jug Y to its full capacity (3 liters)
        j2 = y
    elif r == 3:  # Empty Jug X
        j1 = 0
    elif r == 4:  # Empty Jug Y
        j2 = 0
    elif r == 5:  # Transfer water from Jug X to Jug Y without exceeding Jug Y's capacity
        transfer = min(j1, y - j2)  # Transfer the minimum of Jug X's contents or available space in Jug Y
        j1 -= transfer
        j2 += transfer
    elif r == 6:  # Transfer water from Jug Y to Jug X without exceeding Jug X's capacity
        transfer = min(j2, x - j1)  # Transfer the minimum of Jug Y's contents or available space in Jug X
        j2 -= transfer
        j1 += transfer

    print(f"Current state: Jug X = {j1}, Jug Y = {j2}")

print("Goal achieved! Jug X = 2.")
