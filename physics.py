distance = 0
i_velocity = 0
f_velocity = 0
time = 0
acceleration = 0

#sig figs are gonna suck balls

def input_Vals():
    try:
        distance = float(input("Enter distance Value (0 if unknown):  "))
        i_velocity = float(input("Enter Inital Velocity Value (0 if unknown): "))
        f_velocity = float(input("Enter Final Velocity Value (0 if unknown): "))
        time = float(input("Enter time Value (0 if unknown): "))
        acceleration = float(input("Enter acceleration Value (0 if unknown): "))
    except:
        print("An error has occured, try again \n\n\n")
        input_Vals()

    check = "Distance is {} \nInitial Velocity is {} \nFinal Velocity is {} \nTime is {} \nAcceleration is {}"
    if distance == 0.0:
        distance = "..."
    if i_velocity == 0.0:
        i_velocity = "..."
    if f_velocity == 0.0:
        f_velocity = "..."
    if time == 0.0:
        time = "..."
    if acceleration == 0.0:
        acceleration = "..."
    print(check.format(distance, i_velocity, f_velocity, time, acceleration))
    checkInput = input("Are these correct? (y/n): ")
    if checkInput.lower == "n":
        input_Vals()

        

input_Vals()