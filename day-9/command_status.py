import subprocess
try:
    result = subprocess.run(['free','-m'],
             capture_output = True,
             text = True)
    std = result.stdout
    vac = result.stderr
    value = result.returncode
    with open ("Command_report.txt","w") as file:
        file.write("Server Command Report\n")
        file.write("Command: free -m \n")
        file.write("Status: Success\n")
        file.write(f"Return value:{value}\n")
        file.write("Memory_details\n")
        file.write(f"{std}\n")
        file.write(f"{vac}\n")

        if value == 0:
            file.write("command succeeded\n")
        else: 
            file.write("command failed\n")

except FileNotFoundError:
    print("Command not found!\n")
    with open ("Command_report.txt","w") as file:
        file.write("Command Execution Report\n")
        file.write("command:l\n")
        file.write("Status:Command not found\n")
       
