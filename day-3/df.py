import subprocess
result = subprocess.run(["df","-h"],
             capture_output=True,
             text=True)
output=(result.stdout)
print(output)
