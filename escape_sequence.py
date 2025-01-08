import re

print("Hello\nWorld") #new line
print("Hello\tWorld") #tab
print("Hello\rWorld") #return cursor to start of line
print("This is a backslash: \\") #backslash
print('It\'s sunny') #escape
print("He said, \"Hi!\"") #double quote
print("Hello World\b") #backspace
print("\u263A") #unicode
print("\U0001F600") #unicode
print(r"C:\Users\Name\Documents") #raw string
print("C:\\Users\\Name\\Documents") #raw string

#regular expression
pattern = r"\d+"  # Matches one or more digits
result = re.findall(pattern, "There are 123 apples and 45 bananas.")
print(result) # ['123', '45']

# I want to print some information in the first line then # I want to print some other information in the second lineprint("Khairi Bin Abu Bakar", "720102121234", "Outstanding Balance", 1455.55)print("Khairi Bin Abu Bakar", "720102121234") # after printing it automatically goes to next lineprint("Outstanding Balance", 1455.55)print("Khairi Bin Abu Bakar", "720102121234", "\n", "Outstanding Balance", 1455.55)print("Khairi Bin Abu Bakar", "720102121234", "\nOutstanding Balance", 1455.55)# \ character is called "escape sequence" in many programming language(s)# When \ is followed by another character it becomes a new meaningful item# \n => new line# \r => carrage return# \t => tab key# \" => in this case it is saying don't treat " as enclosing character# \' => in this case it is saying don't treat ' as enclosing character# \\ => in this case it is saying this is a simple \print("I don't like \"apples\"")print('I don\'t like "apples"')# However when we print the list# print function convert the entire list into a string and print itprint(["apple", "orange", "\n", "mango"]) # "['apple', 'orange', '\n', 'mango']"print("C:\newfolder\table.xlsx")print("C:\\newfolder\\table.xlsx")
#end

# I want to print some information in the first line then 
# I want to print some other information in the second line
print("Khairi Bin Abu Bakar", "720102121234", "Outstanding Balance", 1455.55)
print("Khairi Bin Abu Bakar", "720102121234") 
# after printing it automatically goes to next line
print("Outstanding Balance", 1455.55)

print("Khairi Bin Abu Bakar", "720102121234", "\n", "Outstanding Balance", 1455.55)
print("Khairi Bin Abu Bakar", "720102121234", "\nOutstanding Balance", 1455.55)

# \ character is called "escape sequence" in many programming language(s)
# When \ is followed by another character it becomes a new meaningful item
# \n => new line
# \r => carrage return
# \t => tab key
# \" => in this case it is saying don't treat " as enclosing character
# \' => in this case it is saying don't treat ' as enclosing character
# \\ => in this case it is saying this is a simple \
print("I don't like \"apples\"")
print('I don\'t like "apples"')

# However when we print the list
# print function convert the entire list into a string and print it
print(["apple", "orange", "\n", "mango"]) # "['apple', 'orange', '\n', 'mango']"

print("C:\newfolder\table.xlsx")
print("C:\\newfolder\\table.xlsx")