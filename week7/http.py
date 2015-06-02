import requests

API_URL = "https://hackbulgaria.com/api/students/"

students = requests.get(API_URL).json()

print(students)
