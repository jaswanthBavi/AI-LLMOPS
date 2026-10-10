servers =["web-server","api-server","db-server"]
def utilization(servers, cpu, memory):
    if cpu >= 80:
        cpu_utilization = "High"
    else:
       cpu_utilization = "Normal"

    if memory >= 80:
        memory_utilization = "High"
    else:
        memory_utilization = "Normal"

    return servers, cpu_utilization, memory_utilization

server, cpu_utilization, memory_utilization = utilization("web-server" ,93, 32)
print(f"server1:{server}")
print(f"cpu 93%:{cpu_utilization}")
print(f"memory 32%:{memory_utilization}")

server, cpu_utilization, memory_utilization = utilization("api-server", 43, 90)
print(f"server2:{server}")
print(f"cpu 43%: {cpu_utilization}")
print(f"memory 90%: {memory_utilization}")

server, cpu_utilization, memory_utilization = utilization("db-server", 43, 14)
print(f"server3:{server}")
print(f"cpu 43%: {cpu_utilization}")
print(f"memory 14%: {memory_utilization}")
