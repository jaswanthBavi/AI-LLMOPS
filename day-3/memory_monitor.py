import subprocess
store = subprocess.run(["free","-m"],
          capture_output = True,
          text = True)
result = store.stdout

print(result)
