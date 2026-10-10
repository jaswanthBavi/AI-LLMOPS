import subprocess
line = subprocess.run(["free","-m"],
        capture_output = True,
        text = True)

result = line.stdout.splitlines()


for store in result:
    split = store.split()
    if len(split) >= 7 and split[0] == "Mem:":
        print("=========Server Health Report===========")
        print(f"Total memory {split[1]} MB")
        print(f"Available Memory {split[6]} MB")
        if int(split[6]) <= 300:
            print("Memory status: Warning")
        else:
            print("Memory status: Healthy")
        
line_1 = subprocess.run(["df","-h"],
            capture_output = True,
             text = True)
disk = line_1.stdout.splitlines()

for save in disk:
    place = save.split()
    if len(place) >=6 and place[5] == "/":
        places = int(place[4].replace("%",""))
        print(f"Root Disk Storage {places}%")
        if places >= 90:
            print("Status:Critical")
        elif places >= 80:
            print("Status:Warning")
        else:
            print("Status:Healthy")
print("==========REPORT COMPLETED=============")
