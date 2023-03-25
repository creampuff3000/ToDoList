
def toDoList():
    x = input("Hi! This is your To-Do list maker. Would you like to add items? y/n ")
    list = []
    while True:
        if str(x) == "y":
            y = input("What would you like to add? (You can stop by writing 'endingKey') ")
            if y == "endingKey":
                list.sort()
                print("This is your final list: " + str(list))
                break
            else:
                list.append(y)
                print("Current To-Do List: " + str(list))
                continue
        elif str(x) == "n":
            exit(0)
        else:
            print("I'm not sure what you mean.")
            exit(0)
toDoList()

        
