import subprocess
from datetime import datetime 
now = datetime.now()
value = subprocess.run(["free","-h"],
        capture_output = True,
        text = True)
disk = subprocess.run(["df","-h"],
        capture_output = True,
        text = True)
store = value.stdout
store_1 = disk.stdout.splitlines()
for manage in store_1:
    split = manage.split()
    if len(split) >=6 and split[5] == "/":
        usage = int(split[4].replace("%",""))
        if usage >= 90:
            status = "critical"
        elif usage >= 80:
            status = "Warning"
        else:
            status = "Healthy"
        with open ("system_report.txt","w") as file:
            file.write("SYSTEM HEALTH REPORT\n")
            file.write("=========================\n")
            file.write(f"Date&Time:{now}\n")
            file.write(f"memory_value:{store}\n")
 
            file.write(f"Disk_usage:{usage}\n")
            file.write(f"Status:{status}\n")
            file.write("=========================\n")
