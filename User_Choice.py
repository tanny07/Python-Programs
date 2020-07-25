def Get_the_value():
    Switch_math = int(input(
        "For Area of Square press 1 \nFor Area of Circle press 2 \nFor Area of Triangle press 3 \nFor Area of Rectangle press 4 \nTo Exit press 0 \nYour Choice: "))

    if(Switch_math == 1):
        side = int(input("Enter the Side of Square: "))
        result = side*side
        print(result)

    elif(Switch_math == 2):
        radius = int(input("Enter the Value of Radius: "))
        result = 3.14*radius*radius
        print(result)

    elif(Switch_math == 3):
        height = int(input("Enter the Height of Triangle: "))
        base = int(input("Enter the Base of Triangle: "))
        result = base*height/2
        print(result)

    elif(Switch_math == 4):
        widht = int(input("Enter the Width of Rectangle: "))
        lenght = int(input("Enter the Lenght of Rectangle: "))
        result = widht*lenght
        print(result)

    elif(Switch_math != 0 and Switch_math >= 5):
        print("WRONG INPUT")
        exit()

    else:
        exit()


hey = int(input(
    "Hwllo would you love to do some maths, if yes then press 1 or else press 0 to exit: "))
if(hey == 1):
    Get_the_value
else:
    exit()
