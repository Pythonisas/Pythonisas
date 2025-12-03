from faker import Faker

# Inicializar Faker con locale español
fake = Faker('es_ES')

# Generar 10 personas con datos completos
print("=== Generador de Datos Aleatorios: Nombre + Edad + SQL ===\n")

# Almacenar todas las personas generadas
personas = []
for i in range(1, 11):
    persona = {
        'nombre': fake.name(),
        'edad': fake.random_int(min=18, max=65),
        'email': fake.email(),
        'ciudad': fake.city()
    }
    personas.append(persona)
    print(f"{i}. {persona['nombre']} - {persona['edad']} años")
    print(f"   Email: {persona['email']}")
    print(f"   Ciudad: {persona['ciudad']}\n")

# Separador visual
print("\n" + "="*70)
print("=== SENTENCIAS SQL GENERADAS ===")
print("="*70 + "\n")

# Generar CREATE TABLE
create_table = """-- Crear tabla de alumnos
DROP TABLE IF EXISTS alumnos;

CREATE TABLE alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    email VARCHAR(100) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

"""

print(create_table)

# Generar INSERT statements
print("-- Insertar datos de alumnos generados aleatoriamente\n")

for persona in personas:
    # Escapar comillas simples para evitar errores SQL
    nombre_escaped = persona['nombre'].replace("'", "''")
    email_escaped = persona['email'].replace("'", "''")
    ciudad_escaped = persona['ciudad'].replace("'", "''")

    insert_sql = f"""INSERT INTO alumnos (nombre, edad, email, ciudad)
VALUES ('{nombre_escaped}', {persona['edad']}, '{email_escaped}', '{ciudad_escaped}');"""

    print(insert_sql)

# Agregar consultas de verificación
print("\n-- Consultas de verificación")
print("SELECT COUNT(*) AS total_alumnos FROM alumnos;")
print("SELECT * FROM alumnos ORDER BY edad DESC;")
print("SELECT ciudad, COUNT(*) AS cantidad FROM alumnos GROUP BY ciudad;")

# Opción de guardar en archivo SQL
print("\n" + "="*70)
opcion = input("¿Deseas guardar las sentencias SQL en un archivo? (s/n): ").lower()

if opcion == 's':
    nombre_archivo = "alumnos_generados.sql"

    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(create_table)
        archivo.write("-- Insertar datos de alumnos generados aleatoriamente\n\n")

        for persona in personas:
            nombre_escaped = persona['nombre'].replace("'", "''")
            email_escaped = persona['email'].replace("'", "''")
            ciudad_escaped = persona['ciudad'].replace("'", "''")

            insert_sql = f"""INSERT INTO alumnos (nombre, edad, email, ciudad)
VALUES ('{nombre_escaped}', {persona['edad']}, '{email_escaped}', '{ciudad_escaped}');\n"""
            archivo.write(insert_sql)

        archivo.write("\n-- Consultas de verificación\n")
        archivo.write("SELECT COUNT(*) AS total_alumnos FROM alumnos;\n")
        archivo.write("SELECT * FROM alumnos ORDER BY edad DESC;\n")
        archivo.write("SELECT ciudad, COUNT(*) AS cantidad FROM alumnos GROUP BY ciudad;\n")

    print(f"\n✅ Archivo '{nombre_archivo}' generado correctamente!")
    print(f"   Puedes ejecutarlo con: mysql -u usuario -p database < {nombre_archivo}")
else:
    print("\n📋 Las sentencias SQL están en la salida anterior.")
    print("   Puedes copiarlas y pegarlas en tu gestor de BD.")
