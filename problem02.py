# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# for i in range(1, 26):
#     print(i, end=" ")
#     if i % 5 == 0:
#         print()

num = 1
for i in range(5):
    for j in range(5):
        print(num, end=" ")
        num += 1
    print("")

#orrrr

col = 5
for i in range(1, col+1):
    for j in range(1, col+1):
        print(i*j, end=" ")
    print()
print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5, 0, -1):
    for j in range(i, i+1):
        print(i, end=" ")
    print()

# for i in range(5, -10, -1):
#     print(i)



# 0 0 0 0 1
# 0 0 0 2 0
# 0 0 3 0 0
# 0 4 0 0 0
# 5 0 0 0 0

for i in range(1,6):
    for j in range(5,0,-1):
        print(i, end=" ") if i == j else print(0, end=" ")
    print()
print()


#         1 1
#       2 1 1 2
#     3 2 1 1 2 3
#   4 3 2 1 1 2 3 4
# 5 4 3 2 1 1 2 3 4 5


for i in range(1, 6):
    for j in range(5, 0, -1):
        print (i, end=" ") if i >= j else print(" ", end=" ")
    for j in range(1, i+1):# column
        print(i, end=' ')
    print("")
print("-" * 50)

def pattern(n):
    for i in range(1, n+1):
        for j in range(n, 0, -1):
            print(i, end=" ") if i >= j else print(" ", end=" ")
        for j in range(1, i+1):
            print(i, end=' ')
        print("")

pattern(5)
# pattern(6) 

def pattern_2(n):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            print(i, end=" ") if i >= j else print(" ", end=" ")
        for j in range(1, i+1):
            print(i, end=' ')
        print("")
    print()

pattern_2(5)

