try:
    with open ("missing.txt","r") as file:
        value = file.read()
        print(value)
except FileNotFoundError:
    print("file not found error!")
