def check_cpu(cpu):
    if cpu >= 80: 
        return "high"
    else:
        return "Normal"
result=check_cpu(80)
print(f"cpu 80:{result}")
result= check_cpu(60)
print(f"cpu 60:{result}")
