#debugging example

givenNumber = 12
squarethegivennumber = givenNumber * givenNumber
print(squarethegivennumber)

reverseGivenNumber = 0
reverseGivenNumber = (reverseGivenNumber * 10) + givenNumber % 10
givenNumber = givenNumber // 10
reverseGivenNumber = (reverseGivenNumber * 10) + givenNumber % 10
squarethereversenumber = reverseGivenNumber * reverseGivenNumber
print(squarethereversenumber)