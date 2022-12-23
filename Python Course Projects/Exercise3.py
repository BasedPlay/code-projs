command = ""
has_started = False
while True:
    command = input("\n>").lower()
    if command == 'start':
        if has_started:
            print ("\nThe car has already started!!")
        else:
            has_started = True
            print ("\nThe car has started")
    elif command == 'stop':
        if not has_started:
            print ("\nCar is already stopped!!")
        else:
            has_started = False
            print ("\nThe car has stopped")
    elif command == 'help':
        print ("""
'Start' to start the car
'stop' to stop the car
'quit' to quit game""")
    elif command == 'quit':
        break
    else:
        print ("\nI don't understand that! please type help for command list")