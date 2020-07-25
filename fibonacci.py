name=(input("Enter Your Name: "))

def Fibo_series():
    num=int(input("Enter the Number for Fibonacci Series: "))
    first=0
    new=1
    while new<num:
        result=first+new
        first=new
        new=result
        print(result)


def Star_pattern():
    numb=int(input("Enter the Number to Print Pattern: "))
    line=1
    while numb<line:
        star=1
        print("* " ,end="")
        star+=1
    line+=1

choice=int(input(name+" For fibonacci Series Press 1 and for Star Pattern Press 2: "))

while choice==1:
    print(Fibo_series())
else:
    print(Star_pattern())


enter=int(input("Want to do it Again? If Yes then press 1 and If No then press 0: "))
while enter==1:
    print(choice)
    if choice==1:
        print(Fibo_series())
    elif name==2:
        print(Star_pattern())
    else:
        exit()
else:
    exit()

