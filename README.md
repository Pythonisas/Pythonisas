# Pythonisas
GH Web Pages de la  (auto)organización 'Pythonisas'. Brujas del teclado. Alquimistas de los bits.

## ¿Generar datos aleatoriamente ?

```python 
from faker import Faker
fake = Faker('es_ES')
for _ in range(10):
    print(fake.name())

# Azahara Valera Cuervo
# Porfirio del Camps
# Eloísa Orozco Ochoa
# Poncio Bellido Abella
# Arturo Escobar Salom
# Lalo Ignacio Prat Andrés
# Severiano José María Torre Salinas
# Roberta Ibañez Catalá
# Raquel María Luisa Osuna Giner
# Ágata Diez Soler
```

```
_|_|_|_|          _|
_|        _|_|_|  _|  _|      _|_|    _|  _|_|
_|_|_|  _|    _|  _|_|      _|_|_|_|  _|_|
_|      _|    _|  _|  _|    _|        _|
_|        _|_|_|  _|    _|    _|_|_|  _|
```

## Scripts para generar-datos-aleatoriamente 

Usa el módulo [Python Faker](https://faker.readthedocs.io/) : 

### _El script en su v2_ tiene dos partes : 

  Sección 1 - Formato Simple:
  - 10 personas con nombres españoles completos y edades entre 18-65 años
  - Ejemplos: "María Ángeles Adán-Iglesias - 60 años", "Teodosio Sedano Arcos - 37 años"

  Sección 2 - Formato Estructurado (Diccionarios):
  - 5 personas con datos más completos:
    - Nombre completo
    - Edad adulta aleatoria
    - Email ficticio
    - Ciudad española

  Observaciones didácticas:
  - ✅ Nombres realistas en español (locale es_ES)
  - ✅ Edades adultas variadas (18-65 años)
  - ✅ Datos adicionales útiles (email, ciudad)
  - ✅ Dos enfoques: lista simple vs estructura de datos compleja

  Ideal para:
  - Generar datos de prueba en bases de datos
  - Ejercicios de manipulación de listas/diccionarios
  - Simulaciones de sistemas de gestión de alumnos/usuarios

### _El script en su v3_ genera los INSERT SQL ! :

**Mejoras implementadas:**

📊 **Estructura SQL completa:**
- `CREATE TABLE` con campos: id, nombre, edad, email, ciudad, fecha_registro
- `DROP TABLE IF EXISTS` para evitar conflictos
- Campos con tipos de datos apropiados (VARCHAR, INT, TIMESTAMP)
- Clave primaria autoincremental

🔒 **Seguridad SQL:**
- Escapado automático de comillas simples
- Prevención de errores por caracteres especiales
- Compatible con nombres con tildes y apóstrofos

💾 **Generación de sentencias:**
- 10 INSERT statements listos para ejecutar
- Formato con nombres de columnas explícitos
- Comentarios SQL pedagógicos
- Consultas de verificación incluidas:
  - `SELECT COUNT(*)` para total de registros
  - `SELECT` con ordenación por edad
  - `SELECT` con agrupación por ciudad

✨ **Funcionalidad adicional:**
- Opción interactiva para guardar en archivo `.sql`
- Archivo ejecutable directamente: `mysql -u usuario -p database < alumnos_generados.sql`
- Encoding UTF-8 para soporte completo de español
- Instrucciones de uso incluidas

🎓 **Valor didáctico:**
- Flujo completo: generación de datos → visualización → SQL exportable
- Buenas prácticas de SQL (comentarios, estructura, seguridad)
- Material listo para prácticas de SGBD en ciclos formativos
- Ejemplo real de integración Python + SQL

**Uso:**
```bash
python3 generar-datos-de-alumnos-aleatoriamente-v3.py
```

**Salida ejemplo:**
```sql
DROP TABLE IF EXISTS alumnos;

CREATE TABLE alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    email VARCHAR(100) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO alumnos (nombre, edad, email, ciudad)
VALUES ('María Ángeles Adán-Iglesias', 60, 'ejemplo@example.com', 'Madrid');
-- ... más INSERT statements
```

