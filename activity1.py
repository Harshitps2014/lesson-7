print("="*50)
print("welcome to ride builder")
print("="*50)
print()
print("step 1:pick your vehicle")
print("1.bike")
print("2.car")
print()
choice=int(input("enter 1 or 2"))
if choice==1:
    print("step 2:pick your bike type")
    print("1. scooty")
    print("2. mountain bike")
    print()
    bike_type=int(input('enter 1 or 2'))
    if bike_type==1:
        print("you picked scooty")
        print("top speed is 80 km/h")
        print("best for city roads")
    else:
        print("you picked mountain bike")
        print("top speed is 40 km/h")
        print("best for off road tr")
elif choice==2:
    print("step 2:pick your car type")
    print("1. sedon")
    print("2. SUV")
    print()
    car_type=int(input('enter 1 or 2'))
    if car_type==1:
        print("you picked sedon")
        print(" 5 passenger seat")
        print("best for family trips")
    else:
        print("you picked SUV")
        print("7 passenger seat")
        print("best for off road adventure")
else:
    print("invalid choice,please enter 1 or 2")
