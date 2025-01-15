student = {
    "fname": "John",
    "lname": "Doe",
    "age": 20,
    "phone_no": "1234567890",
    "email": "John@hmail.com",
    "ic_number": None,
    "passport": None,
    "subjects": ["Math", "English", "Science"],
    "active": True
}

print(student["fname"], student["lname"])

student["car"] = [{
    "brand": "Toyota",
    "model": "Camry",
    "year": 2018
    },
    {
    "brand": "Honda",
    "model": "Civic",
    "year": 2019
    }]

print(student["car"])
print(student["car"][0])
print(student["car"][0]["model"])

print(student.keys())
print(student.values())

print(student.items())

for key, value in student.items():
    if (isinstance(value, list)):
        for item in value:
            if isinstance(item, str):
                print(item)
            elif isinstance(item, dict):
                for key2, value2 in item.items():
                    print(key2, value2)
            else:
                print(item)
            print(item)
    elif (isinstance(value, dict)):
        for key2, value2 in value.items():
            print(key2, value2)
    else:
        print(key, value)

print("="*69)

menu = {
    0: "Exit",
    1: ["Manage Student", {
        0: "Exit",
        1: "Add Student",
        2: "Update Student",
        3: "Delete Student",
        4: "Search Student"
    }],
    2: ["Manage Teacher", {
        0: "Exit",
        1: "Add Teacher",
        2: "Update Teacher",
        3: "Delete Teacher",
        4: "Search Teacher"
    }],
    3: ["Manage Subject", {
        0: "Exit",
        1: "Add Subject",
        2: "Update Subject",
        3: "Delete Subject",
        4: "Search Subject"
    }],
    4: ["Manage Class", {
        0: "Exit",
        1: "Add Class",
        2: "Update Class",
        3: "Delete Class",
        4: "Search Class"
    }]
}

choice = -1
while choice != 0:
    for key, value in menu.items():
        if isinstance(value, str):
            print(key, value)
        else:
            print(key, value[0])
    choice = int(input("Enter your choice: "))
    selected_menu = menu[choice]
    if isinstance(selected_menu, list):
        choice2 = -1
        while choice2 != 0:
            for key, value in selected_menu[1].items():
                print(key, value)
            choice2 = int(input("Enter your choice: "))
            print("You have select ",selected_menu[1][choice2])