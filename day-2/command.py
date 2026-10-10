import subprocess
result=subprocess.run(["pwd"],
           capture_output = True,
           text =True
)
print(result.stdout)
    
