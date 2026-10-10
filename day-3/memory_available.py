import subprocess

store = subprocess.run(["free","-m"], 
         capture_output = True,
         text = True)
result = store.stdout.splitlines()

for line in result:
   value = line.split()
   if len(value) >= 7 and value[0] == "Mem:":
       print(f"Total memory:{value[1]} MB")
       print(f"Available Memory:{value[6]} MB")
       if int(value[6]) <= 300:
           print("Memory Status: Warning")
       else:
           print("Memory status: Healthy")
