distance = 0
i_velocity = 0
f_velocity = 0
time = 0
acceleration = 0

#sig figs are gonna suck balls

def input_Vals():
    distance = input("Enter distance Value (u if unknown):  ")
    i_velocity = input("Enter Inital Velocity Value (u if unknown): ")
    f_velocity = input("Enter Final Velocity Value (u if unknown): ")
    time = input("Enter time Value (u if unknown): ")
    acceleration = input("Enter acceleration Value (u if unknown): ")

    try:
        if distance.lower() == "u":
            distance = distance.lower()
        else:
            float(distance)

        if i_velocity.lower() == "u":
            i_velocity = i_velocity.lower()
        else:
            float(i_velocity)

        if f_velocity.lower() == "u":
            f_velocity = f_velocity.lower()
        else:
            float(f_velocity)

        if time.lower() == "u":
            time = time.lower()
        else:
            float(time)

        if acceleration.lower() == "u":
            acceleration = acceleration.lower()
        else:
            float(acceleration)
    except ValueError:
        print("\nThere was a problem try again (letters can't be numbers)\n\n")
        input_Vals()


    check = "\nDistance is {} \nInitial Velocity is {} \nFinal Velocity is {} \nTime is {} \nAcceleration is {}"

    print(check.format(distance, i_velocity, f_velocity, time, acceleration))

    checkInput = input("\nAre these correct? (y/n): ")
    if checkInput.lower == "n":
        input_Vals()
    
    calc_All(distance, i_velocity, f_velocity, time, acceleration)

def calc_All(d, i_v, f_v, t, a):
    if d == "u":
        if calc_Distance(i_v, f_v, t, a) == None:
            print("Not enough information known")
        else:
            print(calc_Distance(i_v, f_v, t, a))

def calc_Distance(i_v, f_v, t, a):
    if i_v != "u" and f_v != "u" and time != "u":
        return .5 * (float(i_v) + float(f_v)) * t
    elif i_v != "u" and time != "u" and a != "u":
        return float(i_v) * float(t) + .5 * float(a) * float(t) ** 2
    elif i_v != "u" and f_v != "u" and a != "u":
        return (float(f_v) ** 2 - float(i_v) ** 2) / (2 * float(a))
    else:
        return None
    
def calc_Initial_Velocity(d, f_v, t, a):
    if f_v != "u" and a != "u" and t != "u":
        return float(f_v) - float(a) * float(t)
    elif f_v != "u" and a != "u" and d != "u":
        return float(f_v) ** 2 - 2 * float(a) * float(d)
    elif  f_v != "u" and d != "u" and t != "u":
        return 2 * float(d) / float(t) - float(f_v)
    elif d != "u" and t != "u" and a != "u":
        return (float(d) - .5 * float(a) * float(t))
    else: 
        return None 

input_Vals()
