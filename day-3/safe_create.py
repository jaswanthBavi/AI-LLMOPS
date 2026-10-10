import os
if os.path.exists("logs"):
    print("The dir already exists")
else:
    os.mkdir("logs")
    print("the dir was created")

