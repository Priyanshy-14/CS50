
def convert_temperature(value, scale):
    far_result = ((9/5)*value) +32
    cel_result =  (value-32)*5/9
    return far_result, cel_result


def get_input():
    temp = float(input("Enter the temperature value:"))
    unit = input("Enter the unit[C/F]: ").strip().upper()
    
    if unit== "C":
        res1,_ = convert_temperature(temp, unit)
        print(f"The temperature {temp} in fahranite is {res1:.2f}"  )
    elif unit =="F":
        _,res2 = convert_temperature(temp, unit)
        print(f"The temperature {temp} in celcius is {res2:.2f}"  )
    else:
        print("Invalid unit value")



get_input()

    