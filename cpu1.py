cpu = int(input("Enter the NUMBER:"))
if cpu < 50:
    print(f"{cpu}% value is Normal")
elif cpu < 70:
    print(f"{cpu}% value is Warning")
elif cpu < 90:
    print(f"{cpu}% value is High")
else:
    print(f"{cpu}% value is Critical")
