user_input = int(input("Enter a number: "))
line = 1 
no_of_spaces = user_input - 1
while line <= user_input:
    dec = 1
    while dec <= no_of_spaces:
        print(" ",end="")
        dec+=1
    inc = 1
    while inc <= line:
        print("* ",end="")
        inc+=1
    dec = 0
    while dec <= no_of_spaces:
        print(" ",end="")
        dec+= 0.5
    inc = 1
    while inc <= line:
        print("* ",end="")
        inc+= 1
    no_of_spaces-=1
    print("")
    line+=1
line = 1
no_of_spaces = (user_input * 2) 
while line <= (user_input * 2) :
    inc = 1
    while inc <= line:
        print(" ",end="")
        inc+=1
    dec=1
    while dec <= no_of_spaces:
        print("* ",end="")
        dec+=1
    no_of_spaces-=1
    print("")
    line+=1
    