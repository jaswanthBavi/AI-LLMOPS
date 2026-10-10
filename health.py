cpu = int(input("Enter the CPU Utilization:"))
memory = int(input("Enter the Memory Utilization:"))
disk = int(input("Enter the Disk Utilization:"))
if cpu >= 90 and memory >= 90:
    print("CRITICAL: CPU and Memory usage are extremely high")
elif cpu >= 80 or memory >= 80 or disk >= 80:
    print("Warning: High resource utilization")
else:
    print("server: Healthy") 
