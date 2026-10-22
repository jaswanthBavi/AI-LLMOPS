import subprocess 
try:
    value = subprocess.run(["ls"],
         capture_output = True,
         text = True)

    store = value.returncode
    data = value.stdout
    print(store)
    print(data)
    if store == 0:
        print("Command executed Successfully")
    else:
        print("Command failed")
except FileNotFoundError:
    print("Command could not be found")
