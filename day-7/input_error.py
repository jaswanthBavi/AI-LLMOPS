try:
    a = int(input("Enter The CPU Utilization:"))
    if  a >= 0 and a <= 100 :
        if a >= 90 :
            status = "Critical"
        elif a >= 70 :
            status = "Warning"
        else: 
            status = "Normal"
        print(f"Status {status}")
    else: 
        print("Cpu value is Out of range")
except ValueError:
    print("Enter The Correct Number")
