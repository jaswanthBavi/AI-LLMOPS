import subprocess
save = subprocess.run(["free","-m"],
        capture_output = True,
        text = True)
store = save.stdout
print(store)
