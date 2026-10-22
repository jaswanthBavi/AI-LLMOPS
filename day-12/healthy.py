def check_cpu(cpu):
    if cpu >= 90:
        return "Critical"
    elif cpu >= 70:
        return "Warning"
    else:
        return "Healthy"
if __name__ == "__main__":
    store = check_cpu(68)
    print(f"Server_Status:{store}")
