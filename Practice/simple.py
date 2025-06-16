def simple_interest(p, t, r):
    si= (p*t*r)/100
    return si

def get_input():
    pri = int(input("Enter principle amount:"))
    time = float(input("Enter time period:"))
    roi = float(input("Enter rate of interet:"))
    print(f"The Value of Simple Interest is: {simple_interest(pri, time, roi):.2f}")

get_input()
