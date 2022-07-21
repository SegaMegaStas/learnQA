import requests
import time

first_request = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

first_request_data = first_request.json()
seconds = first_request_data["seconds"]

print(f"Process will take {seconds} seconds")

second_request = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": first_request_data["token"]})

second_request_data = second_request.json()

if second_request_data["status"] == "Job is NOT ready":
    time.sleep(float(first_request_data["seconds"]))

third_request = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": first_request_data["token"]})

third_request_data = third_request.json()

print(third_request_data["status"])
print(third_request_data["result"])
