import subprocess
try:
    value = subprocess.run (["free","-h"],
             capture_output = True,
             text = True)

    data = value.stdout
    store = value.returncode
    if store == 0:
        print(data)
        print(f"memory_output:{store}")

    else:
        print("memory command failed")
except FileNotFoundError:
    print("Memory command failed")
