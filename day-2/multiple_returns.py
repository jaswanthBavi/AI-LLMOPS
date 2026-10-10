def check_resourece(cpu, memory):
    if cpu >= 80 and memory >=80:
        return "high","normal"

a = check_resourece("cpu")
    print(f"cpu {a}")
b = check_resourece("memory")
    print(f"Memory {b}")
