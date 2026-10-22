import requests

url = "https://jsonplaceholder.typicode.com/todos?_limit=5"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    with open ("multiple_task.txt","w") as file:
        for store in data:
            file.write(f"Tasks: {store['title']}\n")
            file.write(f"completed: {store['completed']}\n")
            file.write(f"Status: {response.status_code}\n")
    print("All Done")
except requests.RequestException as error:
    print("Api failed",error)
             


