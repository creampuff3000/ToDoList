
def toDoList():
    import os.path
    x = input("Hi! This is your To-Do list maker. Would you make a new list? (this would override previous list) y/n ")
    list = []
    if x == "y":
        os.remove("ToDoList.txt")
    if os.path.exists("ToDoList.txt") == True:
        old = open('ToDoList.txt', 'r+')
    else:
        old = open('ToDoList.txt', 'w')
    while True:
        if str(x) == "y":
            y = input("What would you like to add? (You can stop by writing 'endingKey') ")
            if y == "endingKey":
                list.sort()
                print("This is your final list: " + str(list))
                old.write(str(list))
                old.close()
                break
            else:
                list.append(y)
                print("Current To-Do List: " + str(list))
                continue
        elif str(x) == "n":
            p = input("Would you like to make modifications to your old list? y/n ")
            if p == "y":
                old = open('ToDoList.txt', 'r+')
                print(old.read())
                while True:
                    y = input("What would you like to add? (You can stop by writing 'endingKey') ")
                    if y == "endingKey":
                        list.sort()
                        print("This is your final list: " + old.read())
                        old.write(str(list))
                        old.close()
                        break
                    else:
                        old.write(y)
                        print("Current To-Do List: " + old.read())
                        continue
            else:
                exit(0)
toDoList()

def main():
    toDoList()
if __name__ == "__main__":
  main()
        
