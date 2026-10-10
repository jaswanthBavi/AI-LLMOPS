server = input("Enter server name:")
cpu = int(input("Enter CPU utilization:"))
memory = int(input("Enter memory utilization:"))
disk = float(input("Enter Disk Utilization:"))
if cpu >= 90 and memory >= 90:
    print(f"SERVER:{server}")
    print("STATUS:CRITICAL")
    print("Reason: CPU and memory are extremely high")
elif cpu >= 80 or memory >= 80 or disk >=80:
    print(f"SERVER:{server}")
    print("STATUS: Warning")
    print("Reason: High resource utilization")
else:
    print(f"SERVER:{server}")
    print("STATUS: Healthy")
