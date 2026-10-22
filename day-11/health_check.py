def check_memory(memory):
    if memory >= 90:
        return "Critical"
    elif memory >= 70:
        return "Warning"
    else:
        return "Healthy"
def check_disk(disk):
    if disk >= 90:
        return "Critical"
    elif disk >= 80:
        return "Warning"
    else:
        return "Healthy"
status = check_memory(95)
#print(f"Status:{status}")
status = check_memory(75)
#print(f"Status:{status}")
status = check_memory(55)
#print(f"Status:{status}")
stack = check_disk(95)
#print(f"Disk_usage:{stack}")
stack = check_disk(85)
#print(f"Disk_usage:{stack}")
stack = check_disk(60)
#print(f"Disk_usage:{stack}")
with open ("server_report.txt","w") as file:

    memory_status = check_memory(75)
    disk_status = check_disk(95)
    if memory_status == "Critical" or disk_status == "Critical":
        overall_status = "Critical"
    elif memory_status == "Warning" or disk_status == "Warning":
        overall_status = "Warning"
    else:
        overall_status = "Healthy"

    file.write(f"Memory_status: {memory_status}\n")
    file.write(f"Disk_usage: {disk_status}\n")
    file.write(f"Overall_status:{overall_status}\n")
