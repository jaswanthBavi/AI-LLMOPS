import json
with open ("server.json","r") as file:
    store = json.load(file)

store["Server"]
store["cpu"]
store["memory_usage"]
store["Status"]
store["disk_usage"]
print(store)
print(f'Server: {store["Server"]}')
print(f'CPU usage: {store["cpu"]}%')
print(f' Memory_usage: {store["memory_usage"]}%')
print(f' disk_usage: {store["disk_usage"]}%')

if store["cpu"] >= 90 and store["memory_usage"] >= 90:
    print('Server Health: Critical')
elif store["cpu"] >=80 or store["memory_usage"] >=80 or store["disk_usage"] >= 85:     print('Server Health: Warning')
else:
    print('Server Health: Healthy')


with open ("server_report.txt","w") as file:
    file.write(f'Server name : {store["Server"]}\n')
    file.write(f'CPU Usage : {store["cpu"]} \n')
    file.write(f'Memory Usage : {store["memory_usage"]}\n')
    file.write(f'Status : {store["Status"]}\n')
    file.write(f'Disk_storage : {store["disk_usage"]}\n')


print("======The report was saved=======") 
    
