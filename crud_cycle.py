

import requests


# Create 
BASE_URL = "https://jsonplaceholder.typicode.com/todos"

new_post = {
    "title": "Complete Module 4",
    "completed": False,
    "userId": 1
}

response = requests.post(
    BASE_URL,
    json=new_post
)
print()
print(f"POST {BASE_URL}")
print(response.status_code)
print(response.json())
print()


# READ
data = response.json()
todo_id = data["id"]
todo_url = f"{BASE_URL}/{todo_id}"

read_response = requests.get(todo_url)

print(f"GET {todo_url}")
print(f"Status: {read_response.status_code}")
print(f"Result: {read_response.json()}")
print()


# UPDATE
partial_update = {
    "completed": True
}

response = requests.patch(
    todo_url, json=partial_update
)

print(f"PATCH {todo_url}")
print(f"Status: {response.status_code}")
result = response.json()
print(f"Updated Status: {result['completed']}")
print()



# READ AGAIN
read_response = requests.get(todo_url)

print(f"GET {todo_url}")
print(f"Status: {read_response.status_code}")
print(f"Result: {read_response.json()}")
print()


# DELETE
response = requests.delete(todo_url)

print(f"DELETE {todo_url}")
print(f"Status: {response.status_code}")
print(f"Result: {response.json()}")
print()


# VERIFY 
verify_response = requests.get(todo_url)

print(f"GET {todo_url}")
print(f"Status: {verify_response.status_code}")
print(f"Result: {verify_response.json()}")

if verify_response.status_code == 404:
    print("Todo successfully deleted.")

else: 
    print("Todo still exists.")

