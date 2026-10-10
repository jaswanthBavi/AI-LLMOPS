server = input("Enter server status:")
cpu = int(input("Enter CPU Utilization:"))
if server == "running":
    if cpu >= 80:
        print("Alert: server is running but cpu is high")
    else:
        print("server is running and cpu is normal")
else:
    print("server is not running")

