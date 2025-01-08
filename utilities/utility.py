def calculateNumTotal(*data):
    result = 0
    for item in data:
        result += item
    return result

def calculateSimpleInterest(principal, rate, time):
    interest = principal * rate * time / 100
    return interest