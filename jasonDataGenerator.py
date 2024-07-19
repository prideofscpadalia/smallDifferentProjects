import json
import random
from faker import Faker

fake = Faker()

data = []

for _ in range(1000):
    user = {
        "id": _ + 1,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "user_name": fake.user_name()
    }
    data.append(user)

json_data = json.dumps(data, indent=4)


file_path = "/home/rengoku/Downloads/data.json"
with open(file_path, "w") as file:
    file.write(json_data)

file_path

