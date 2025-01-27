myset = {"apple", "banana", "cherry", "durian", "eggplant", "fig",
 "grape", "honeydew", "ice", "jelly", "kiwi", "lemon", "mango",
  "nectarine", "orange", "peach", "quince", "raspberry", "strawberry",
   "tomato", "watermelon", "xylophone", "yam", "zucchini"}
print(myset)

hat = {"cap", "hat", "top", "turban"}

for item in hat:
    print(item)
print("Items in hat:", hat)

print("Is apple in myset ","apple" in myset)
print("Is apple not in myset ","apple" not in myset)

hat.add("sunglasses")
hat.add("glasses")
print("New hat",hat)
print("Number of items in hat",len(hat))

hat.remove("sunglasses")
hat.discard("glasses") #will not throw an error if the item is not in the set
print("New hat",hat)
hat.clear() #This will only clear the entire set but not delete it
print("New hat",hat)

del hat #This will delete the entire set in memory
# print("New hat",hat) #this will throw an error

car = ["Honda", "Toyota", "Mazda", "Honda", "Proton", "Ferrari", "Honda"]
print("list: ",car)
new_car = set(car)
print("set: ",new_car) #this will remove the duplicates

#set arithmetic
local_fruits = {"durian", "banana", "mango", "papaya", "mango", "pineapple"}
overseas_fruits = {"apple", "banana", "cherry", "lemon", "mango"}

print("union1",local_fruits | overseas_fruits) #union to get all the fruits
print("union2",local_fruits.union(overseas_fruits)) #union

print("sym.diff1",local_fruits ^ overseas_fruits) #symmetric difference to get the unique fruits
print("sym.diff2",local_fruits.symmetric_difference(overseas_fruits)) #symmetric difference

print("intersection1",local_fruits & overseas_fruits) #intersection to get the common fruits
print("intersection2",local_fruits.intersection(overseas_fruits)) #intersection

print("diff1",local_fruits - overseas_fruits) #difference to get the unique fruits (different than symmetric difference as it does not include the common fruits)
print("diff2",local_fruits.difference(overseas_fruits)) #difference

print("subset1",local_fruits <= overseas_fruits) #subset to check if local_fruits is a subset of overseas_fruits
print("subset2",local_fruits.issubset(overseas_fruits)) #subset

print("superset1",local_fruits >= overseas_fruits) #superset to check if local_fruits is a superset of overseas_fruits
print("superset2",local_fruits.issuperset(overseas_fruits)) #superset

print("disjoint1",local_fruits.isdisjoint(overseas_fruits)) #disjoint to check if local_fruits and overseas_fruits are disjoint meaning they have no common fruits

print("issuperset1",local_fruits.issuperset(overseas_fruits)) #issuperset to check if local_fruits is a superset of overseas_fruits

print("issubset1",local_fruits.issubset(overseas_fruits)) #issubset to check if local_fruits is a subset of overseas_fruits

email_description = """ The email content is a communication sent to a user from an email address to another email address.
The email content is composed of a subject, a message body, and a message headers. """
print(email_description)
email = email_description.lower()
one_two_char = {'a', 'to', 'be', 'or', 'not', 'to', 'be'}
email_words = email.split()
unique_email_words = set(email_words) #This will remove the duplicates
valid_email_description = unique_email_words - one_two_char
print(valid_email_description)