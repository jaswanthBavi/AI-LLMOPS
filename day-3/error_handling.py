try:
    user = input("enter cpu utilization:")
    con = int(user)
    if con >= 0:
        print(f"CPU Utilization is:{con}%")
    else:
        print("enter the correct value!")
except ValueError:
    print("invalid input ,please enter valid number:")

