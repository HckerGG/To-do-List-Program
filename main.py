# Simple CLI based To-do list program 
# Credits : HckerGG 

class Process:
    def __init__(self):
        self.todo = []
        self.complete = []

    def add(self):
        task = input("Enter the task you want to add: ")
        self.todo.append(task)
        print(f"Task: {task} added successfully to list")

    def display(self):
        print("To - do List")
        print("******************************************")        
        print("Pending tasks")
        if(self.todo != []):
            for i in range(len(self.todo)):
                print(f"{i+1}: {self.todo[i]}")
        else:
            print("The list is empty ")        
        print("******************************************")
        print("Finished tasks ")
        if(self.complete != []):
            for i in range(len(self.complete)):
                print(f"{i+1}: {self.complete[i]}")
        else:
            print("The list is empty ")
        print("******************************************")
        
    def edit(self):
        option = input("Completed (C) / Remove (R): ")
        choice = int(input("Enter the task number you want to edit: "))
        elmt = self.todo[choice-1]

        if(option.lower() == "c"):
            self.complete.append(elmt)
            self.todo.remove(elmt)
            print("Completed!")
            self.display()
        elif(option.lower() == "r"):
            self.todo.remove(elmt)            
            print("Removed! ")
            self.display()
        else:
            print("Invalid choice! ")        

process = Process()
running = True
while running:
    wmsg = """    
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    |   To - do List        |
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    |   1) Add task         |  
    |   2) Edit task        |
    |   3) Display tasks    |
    |   4) Quit             |
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    print(wmsg)
    user = int(input("Choice: "))
    if(user == 1):
        process.add()
    elif(user==2):
        process.edit()
    elif(user==3):
        process.display()
    elif(user==4):
        running = False
    else:
        print("Invalid choice ")
        running =  True
