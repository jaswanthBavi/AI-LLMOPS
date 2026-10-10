def check_server(cpu, memory, disk):
    if cpu >= 90 and memory >= 90:
        return "Critical"
    elif cpu >=80 or memory >=80 or disk >= 80:
        return "Warning"
    else:
        return "Healthy"
a = check_server( 92, 95, 60)
print(a)
b = check_server( 85, 50, 40)
print(f"{b}")
c = check_server( 40, 50, 60)
print(c)
d = check_server( 80, 45, 30)
print(d)
