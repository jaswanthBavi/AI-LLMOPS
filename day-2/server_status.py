def server_status(server, status="running"):
    print(f"server: {server}")
    print(f"status: {status}")

server_status("server1")
server_status("server2", "stopped")
