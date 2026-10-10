import subprocess
result = subprocess.run(["df","-h"],
             capture_output = True,
             text = True)
mater = result.stdout.splitlines()
for maters in mater:
    parts = maters.split()
    if len(parts) >=6 and parts[5] == "/":
        usage = int(parts[4].replace("%",""))
        print(f"Root disk usage: {usage}%")
        if usage >= 90:
            print("Status:Critical")
        elif usage >=80:
            print("Status:Warning")
        else:
            print("Status:Healthy")

