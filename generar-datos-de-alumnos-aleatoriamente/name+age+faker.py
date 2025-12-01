from faker import Faker

# Inicializar Faker con locale español
fake = Faker('es_ES')

# Generar 10 personas con nombre y edad adulta aleatoria
print("=== Generador de Datos Aleatorios: Nombre + Edad ===\n")

for i in range(1, 11):
    nombre = fake.name()
    edad = fake.random_int(min=18, max=65)  # Edad adulta entre 18 y 65 años

    print(f"{i}. {nombre} - {edad} años")

print("\n" + "="*50)
print("Ejemplo con estructura de diccionario por persona:")
print("="*50 + "\n")

# Alternativa: generar datos estructurados en diccionarios
personas = []
for _ in range(5):
    persona = {
        'nombre': fake.name(),
        'edad': fake.random_int(min=18, max=65),
        'email': fake.email(),
        'ciudad': fake.city()
    }
    personas.append(persona)

# Mostrar las personas generadas
for i, persona in enumerate(personas, 1):
    print(f"Persona {i}:")
    print(f"  Nombre: {persona['nombre']}")
    print(f"  Edad: {persona['edad']} años")
    print(f"  Email: {persona['email']}")
    print(f"  Ciudad: {persona['ciudad']}")
    print()
