import os

def cwd():
    path = os.getcwd()
    print(f"Current Working Directory: {path} \n")

    print("The directory contains the following files : ")
    for file in os.listdir(path):
        print("\n",file)
cwd()

