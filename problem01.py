# Write a program that prints TRUE if given number is positive and FALSE if it is negative

givenNumber = 3

print(givenNumber >= 0)

if givenNumber > 0:
    print("TRUE")
else:
    print("FALSE")


#Write a python program that prints TRUE if given number is even

givenNumber = 7

print(givenNumber, "is even",givenNumber % 2 == 0)

if givenNumber % 2 == 0:
    print("TRUE")
else:
    print("FALSE")


#Write a python program that reverse the given number without using any string functions

givenNumber = 98765

reverseNumber = 0

while givenNumber != 0:
    remainder = givenNumber % 10 #this will get the last digit
    reverseNumber = reverseNumber * 10 + remainder #this is the reverse from the remainder. for each iteration the reverseNumber will be multiplied by 10
    givenNumber = givenNumber // 10 #this will remove the last digit from the givenNumber

print(reverseNumber)

fruits = ["apple", "orange", "mango"]
index = 0

while index < len(fruits):
    print(fruits[index])
    index = (index + 1) #% 3


