import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
try:
    response = requests.get(url, timeout = 10)
    response.raise_for_status()
    data = response.json()
    with open ("Api_report.txt","w") as file:
        file.write(f"Tasks: {data['title']}\n")
        file.write(f"Completed: {data['completed']}\n")
        file.write(f"Status: {response.status_code}\n")
    print("API report saved")
except requests.exceptions.RequestException as error:
    print("Api failed:",error)
