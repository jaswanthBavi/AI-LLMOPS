import subprocess
from datetime import datetime

try:
    now = datetime.now()
    result = subprocess.run(['free','-m'],
         capture_output = True,
         text = True)
    disk = subprocess.run(['df','-h'],
           capture_output = True,
           text = True)
    value = result.stdout.splitlines()
    for values in value:
        matter = values.split()
        if len(matter) >= 7 and matter[0] == "Mem:":
            total = int(matter[1])
            available = int(matter[6])
            used = total - available
            work = (used / total) * 100
            code = result.returncode
            if work < 80:
                memory_status = "Healthy"
            elif work < 90:
                memory_status = "Warning"
            else: 
                memory_status = "Critical"
    with open ("smart_report.txt","w") as file:
        file.write("System Health Report\n")   
        file.write(f"Date & Time: {now}\n")
        file.write(f"Memory usage: {work:.2f}%\n")
        file.write(f"Memory_Status: {memory_status}\n")
        mem = disk.stdout.splitlines()
        memory = disk.returncode
        for mems in mem:
            parts = mems.split()
            if len(parts) >=6 and parts[5] == "/":
                usage = int(parts[4].replace("%",""))
                if usage >= 90:
                    status = "Critical"
                elif usage >= 80:
                    status = "Warning"
                else:
                    status = "Healthy"
                file.write(f"Usage of Disk: {usage}%\n")
                file.write(f"Status: {status}\n")
                file.write("calculate Overall Status\n")
                file.write("===========================\n")
                if memory_status == "Critical" or status == "Critical":
                    overall_status = "Critical"
                elif memory_status == "Warning" or status == "Warning":
                    overall_status = "Warning"
                else: 
                    overall_status = "Healthy"
                file.write(f"Overall_status: {overall_status}\n")

        if code == 0:
            file.write("memory command succeeded\n")
            if memory == 0:
                file.write( "disk information successfully\n")
        else:
            file.write(" memory not working\n")
        
except FileNotFoundError:
    print("Memory/disk Command not found")

