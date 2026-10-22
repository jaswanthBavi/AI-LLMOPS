import subprocess
result = subprocess.run(["df","-h"],
          capture_output = True,
          text = True)

save = result.stdout.splitlines()
for store in save:
    value = store.split()
    if len(value) >= 6 and value[5] == "/":
        values = int(value[4].replace("%",""))
with open ("disk_report.txt","w") as file:
        if values >= 90:
            status = "critical"
        elif values >= 80:
            status = "Warning"
        else:
            status = "Healthy"
        file.write(f"filesystem:/ \n")
        file.write(f"Disk Usage:{values}\n")
        file.write(f"Status:{status} \n")

