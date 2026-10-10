#import subprocess
#disk = subprocess.run(["df","-h"])
#print(disk)

a = "/dev/mapper/cs_root 17G 17G 727M 96% /"
store = a.split()

print (f"Disk_usage:{store[4]}")

