command = ''
counter = 'False'
while command != 'quit':
    command = input("> ").lower()
    if(command == 'start'):
        if(counter == True):
            print("Car is already started")
        else:
            print("Car Started")
            counter = True
    elif command == 'stop':
        if not counter:
            print("Car is already stopped")
        else:
            print("Car stopped")
            counter = False
    elif command == 'help':
        print("""
        start - To start the car
        stop - o stop the car
        quit - To quit the car
         """)
    elif command == 'quit':
        break
    else:
        print("Please reseclect option")
