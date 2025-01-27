def counter():
    counter = 0
    counter +=1
    return counter

print(counter())


def counter():
    counter = 0
    counter +=1
    yield counter    
    counter +=1
    yield counter    
    counter +=1
    yield counter

cur_counter = counter()

print(next(cur_counter))
print(next(cur_counter))
print(next(cur_counter))

# This will throw an error as there is no next value in the generator
# print(next(cur_counter)) 

def myrange(start, end):
    for i in range(start, end):
        yield i

myrangeclient = myrange(1, 4)
print(next(myrangeclient))
print(next(myrangeclient))
print(next(myrangeclient))
# This will throw an error as there is no next value in the generator
# print(next(myrangeclient))

for i in myrange(19, 25):
    print(i)

