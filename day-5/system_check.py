import subprocess
value = subprocess.run[("free","-m"), 
          capture_output = True,
          text = True)

store = value.stdout()
print(store)
          
