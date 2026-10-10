def check_resource(cpu, memory):
    if cpu >= 80:
        cpu_status = "High"
    else:
        cpu_status = "Normal"
    if memory >=80:
        memory_status = "High"
    else:
        memory_status = "NOrmal"
    return cpu_status, memory_status

cpu_status, memory_status = check_resource(90,43)
print (f"cpu_status 90: {cpu_status}")
print (f" memory_status 43: {memory_status}")

cpu_status, memory_status = check_resource(54,93)
print (f"cpu_status 54: {cpu_status}")
print (f" memory_status 93: {memory_status}")

