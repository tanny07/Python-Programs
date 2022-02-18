# right triangle star pattern (1)
size = 5
for i in range(size):
    for j in range(1, size - i):
        print(" ", end="")
    for k in range(0, i + 1):
        print("*", end="")
    print()


# hollow triangle star pattern (2)
n = 6
for i in range(1, n+1):
    for j in range(i):
        # print star only at start and end of the row
        if j == 0 or j == i-1:
            print('*', end='')
        # print only star if it's last row
        else:
            if i != n:
                print(' ', end='')
            else:
                print('*', end='')
    print()


# downward triangle star pattern (3)
n = 5
for i in range(n):
    print('*' * (n - i))


# pyramid star pattern (4)
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()

# hollow pyramid star pattern (5)
n = 5
for i in range(n):
    # printing spaces
    for j in range(n - i - 1):
        print(' ', end='')

# printing stars (6)
for k in range(2 * i + 1):
    # print star at start and end of the row
    if k == 0 or k == 2 * i:
        print('*', end='')
    else:
        if i == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# reverse pyramid pattern (7)
n = 5

for i in range(n):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing stars
    for j in range(2*(n-i)-1):
        print('*', end='')
    print()


# diamond star pattern (8)
n = 5

# upward pyramid
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
# downward pyramid 
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        print('*', end='')
    print()


# hollow diamond star pattern (9)
n = 5

# upward hollow pyramid
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
# downward pyramid
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        if j == 0 or j == 2*(n - i - 1) - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# hourglass star pattern (10)
n = 5

# downward pyramid
for i in range(n-1):
    for j in range(i):
        print(' ', end='')
    for k in range(2*(n-i)-1):
        print('*', end='')
    print()
# upward pyramid
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()


# right pascal triangle (11)
n = 5

# upper triangle
for i in range(n):
    for j in range(i + 1):
        print('*', end="")
    print()
# lower triangle
for i in range(n):
    for j in range(n - i - 1):
        print('*', end="")
    print()


# left pascal triangle (12)
n = 5

# upper triangle
for i in range(n):
    # print spaces
    for j in range(n - i - 1):
        print(' ', end='')
    # print stars
    for k in range(i + 1):
        print('*', end='')
    print()
# lower triangle
for i in range(n - 1):
    # print spaces
    for j in range(i + 1):
        print(' ', end='')
    # print stars
    for k in range(n - i - 1):
        print('*', end='')
    print()


# heart pattern (13)
n = 6

# upper part of heart
for i in range(n//2, n, 2):
    # print first spaces
    for j in range(1, n-i ,2):
        print(" ", end="")
    # print first stars
    for j in range(1, i+1, 1):
        print("*", end="")
    # print second spaces
    for j in range(1, n-i+1, 1):
        print(" ", end="")
    # print second stars
    for j in range(1, i+1, 1):
        print("*", end="")
    print()

# lower part
for i in range(n,0,-1):
    for j in range(i, n, 1):
        print(" ", end="")
    for j in range(1, i*2, 1):
        print("*", end="")
    print()

