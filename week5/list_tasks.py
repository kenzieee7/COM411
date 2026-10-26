def movements ():
    steps= [ "Move Forward", "MoveBackward", "Turn Left", "Turn Right",]
    return steps

def menu_and_input ():
    print("Please select a direction:")

    steps= movements()
    for i in range(0,len(steps),1):
        #i is the index
        #range allows the values to move up by two.
        #length takes the length of the list which is the stop value.
        #range contains (start, stop, set)
        print(f"{i} : {steps[0]}")


menu_and_input ()
