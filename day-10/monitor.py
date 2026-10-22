import subprocess
try:
    test = subprocess.run(["lsx"],
            capture_output = True,
            text = True)
    mater = test.stdout
    mem = test.stderr
    value = test.returncode
    with open ("command_report.txt","w") as file:
        file.write("Report values\n")
        file.write(f"Return_code: {value}\n")

        file.write(f"Standard Output: {mater}\n")
        file.write(f"Error: {mem}\n")
        if value == 0:
            file.write(f"Memory command success\n")
        else:
            file.write(f"Memory command failed\n")
except FileNotFoundError:
    with open ("command_report.txt","w") as file:
        file.write("Linux command execution Report\n")
        file.write("Command: lxs\n")
        file.write("Status: Command not found\n")


    
