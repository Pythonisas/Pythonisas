from faker import Faker

fake = Faker()

for _ in range(10):
print({
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
    })
