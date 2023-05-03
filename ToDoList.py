import os.path
def readFile(old):
    old = open('/Users/justinluo/projects/toDoList/ToDoList.txt', 'r')
    print(old.read())

def listToString(list):
    str1 = ""
    for i in list:
        str1 += i
    return str1
def toDoList():
    while True:
        list = []
        x = input("Hi! This is your To-Do list maker. Would you make a new list? (this would override previous list) y/n ")
        if x == "y":
            os.remove("/Users/justinluo/projects/toDoList/ToDoList.txt")
        if os.path.exists("/Users/justinluo/projects/toDoList/ToDoList.txt") == True:
            old = open('/Users/justinluo/projects/toDoList/ToDoList.txt', 'r+')
        else:
            old = open('/Users/justinluo/projects/toDoList/ToDoList.txt', 'a')
        while True:
            if str(x) == "y":
                y = input("What would you like to add? (You can stop by writing 'endingKey') ")
                if y == "endingKey":
                    print("This is your final list: " + str(list))
                    old.writelines(list)
                    old.close()
                    break
                else:
                    list.append(y)
                    print("Current To-Do List: " + str(list))
                    continue
            elif str(x) == "n":
                p = input("Would you like to make modifications to your old list? y/n ")
                if p == "y":
                    readFile(old)
                    old.close()
                    while True:
                        y = input("What would you like to add? (You can stop by writing 'endingKey', please write with quotes) ")
                        if y == "endingKey":
                            old = open('/Users/justinluo/projects/toDoList/ToDoList.txt', 'a')
                            print(list)
                            old.writelines(list)
                            list = []
                            readFile(old)
                            old.close()
                            break
                        else:
                            old = open('/Users/justinluo/projects/toDoList/ToDoList.txt', 'r')
                            list.append(y)
                            print("This is what you're going to add to the original file: " + str(list))
                            continue
                    m = input("Would you like to know how many characters are in your list? y/n ")
                    if m == "y":
                        old = open('/Users/justinluo/projects/toDoList/ToDoList.txt', 'r+')
                        count = 0
                        countingList = old.readlines()
                        for i in countingList:
                            count += len(i)
                            print(count)
                            continue
                        else:
                            exit(0)
                    else:
                        exit(0)
                else:
                    exit(0)