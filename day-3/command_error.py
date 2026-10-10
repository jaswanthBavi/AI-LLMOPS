import subprocess

store = subprocess.run(['ls','/fake_directory'],
         capture_output = True,
         text = True)
if store.returncode == 0:
    print("command sucessful")
else:
    print("command failed if its fais")
    print(store.stderr)
