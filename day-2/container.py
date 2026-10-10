def create_container(name, port = 8080):
    print(f"conatiner: {name}")
    print(f"port: {port}")
create_container("webapp")
create_container("api",5000)

