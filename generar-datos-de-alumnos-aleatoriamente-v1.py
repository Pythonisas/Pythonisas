from faker import Faker
fake = Faker('es_ES')
for _ in range(10):
    print(fake.name())

# 'Elsa Palombo'
# 'Paco Giméne'
