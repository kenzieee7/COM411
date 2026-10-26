def movements ():
    path= ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run_tasks2 ():
    print("Moving...")

    path= movements()
    for i in range(0,len(path),2):
        #i is the index
        #range allows the values to move up by two.
        #length takes the length of the list which is the stop value.
        #range contains (start, stop, set)
        print(f"{path[i]} for {path[i+1]} steps")


run_tasks2()
