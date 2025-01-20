def getCurrentBalance(accountnumber):
    if accountnumber != None:
        return 3500
    
# passing function as argument
def my_decorator(func):
    def calculat_sst(*args):
        prices_with_sst = []
        for arg in args:
            print(arg)
            prices_with_sst.append(arg + (arg * 0.06))
        func(prices_with_sst)
    def capture_time(*args):
        print("Start Time")
        result = func(*args)
        print("End Time")
        return result
    if func.__name__ == "pricesWithSST":
        return calculat_sst
    else:
        return capture_time

# Let us assume we go to ATM and withdraw money
# the code inside the function is not going to be this simple
# the code may also cause performance issue
# Let us assume somebody make a complain the withdraw function is slow
# You must capture the average time take for the function to be executed
@my_decorator
def withdraw(accountnumber, amount):
    # print("Start Time")
    currentBalance = getCurrentBalance(accountnumber)
    currentBalance = currentBalance - amount
    print(f"Current Balance after withdraw {amount}:", currentBalance)
    # print("End Time")
    return currentBalance

@my_decorator
def transfer(accountnumber, amount, toaccountnumber):
    # print("Start Time")
    currentBalance = getCurrentBalance(accountnumber)
    currentBalance = currentBalance - amount
    print(f"Current Balance after transfer {amount} to {toaccountnumber}:", currentBalance)
    # print("End Time")
    return currentBalance

@my_decorator
def pricesWithSST(data):
    for item in data:
        print(item)

# Without modifing the withdraw function we are adding more feature to the function
# Initially it can do withdraw only but now it can capture start time end time and
# also can do the withdraw function

print(withdraw("1234-5678-9012", 500))
# decorated_withdraw = my_decorator(withdraw)
# print(decorated_withdraw("1234-5678-9012", 500))
print(transfer("1234-5678-9012", 500, "98765-4321-1234"))

pricesWithSST(10, 20, 30, 40, 50)