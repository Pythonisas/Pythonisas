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

_El script en su v2_ tiene dos partes : 

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

#### MEjoras: 

Fácilmente añadiríamos las siguientes funcionalidades : 
- podrían añadir más campos
    - DNI, 
	- teléfono, 
	- fecha de nacimiento
- guardar los datos en un archivo JSON/CSV
- ¿ exportar a SQL ?
