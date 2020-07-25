def Factorial_Num(num):
    if(num == 0):
        return 1
    else:
        return num * Factorial_Num(num-1)


def Star_Pattern():
    numb = int(input("Enter the Number to print Pattern till that Number: "))
    line = 1
    while(line <= numb):
        star = 1
        while(star <= line):
            print("* ", end="")
            star += 1
        print("")
        line += 1


def Fibo_Series(new):
    if new <= 1:
        return new
    else:
        return Fibo_Series(new-1)+Fibo_Series(new-2)


say = int(input(" Press 1 for Factorial Number\n Press 2 for Pattern Printing\n Press 3 for Fibonacci Series\n Press 4 to Exit\n Enter your Choice: "))
if(say == 1):
    num = int(input("Enter the Number to Find Its Factorial: "))
    print(Factorial_Num(num))
if(say == 2):
    (Star_Pattern())
if(say == 3):
    new = int(input("Enter the Number: "))
    if new <= 0:
        print("Enter a Postive Number")
    else:
        print("Fibonacci Series:")
        for i in range(new):
            print(Fibo_Series(i))
