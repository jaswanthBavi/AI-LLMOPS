servers = [ 54,67,97,56,90,45,27,86,95,59]
for server_cpu in servers:
    if server_cpu <80:
        print (f"CPU {server_cpu}: Normal")
    else: 
        print(f"CPU {server_cpu}: High")

