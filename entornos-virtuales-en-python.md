# Entornos Virtuales en Python

El soporte para entornos virtuales está incluido en todas las versiones recientes de Python, así que todo lo que necesitas hacer para crear uno es esto:

```bash
$ python3 -m venv venv
```

Con este comando, estoy pidiendo a Python que ejecute el paquete venv, que crea un entorno virtual llamado venv. El primer venv en el comando es un argumento a la opción -m que es el nombre del paquete de entorno virtual de Python, y el segundo es el nombre del entorno virtual que voy a usar para este entorno en particular. Si encuentras esto confuso, puedes reemplazar el segundo venv con un nombre diferente que quieras asignar a tu entorno virtual. En general, creo mis entornos virtuales con el nombre venv en el directorio del proyecto, de modo que cada vez que hago cd a un proyecto encuentro su entorno virtual correspondiente.

Ten en cuenta que en algunos sistemas operativos puede que necesites usar python en lugar de python3 en el comando anterior.

Después de que el comando se complete, vas a tener un directorio llamado venv donde se almacenan los archivos del entorno virtual.

Ahora tienes que decirle al sistema que quieres usar este entorno virtual, y lo haces activándolo. Para activar tu nuevo entorno virtual usas el siguiente comando:

```bash
$ source venv/bin/activate
(venv) $ _
```

Si estás usando una ventana de símbolo del sistema de Microsoft Windows, el comando de activación es ligeramente diferente:

```bash
$ venv\Scripts\activate
(venv) $ _
```

Si estás en Windows pero estás usando PowerShell en lugar del símbolo del sistema, entonces hay otro comando de activación que debes usar:

```bash
$ venv\Scripts\Activate.ps1
(venv) $ _
```

Cuando activas un entorno virtual, la configuración de tu sesión de terminal se modifica de modo que el intérprete de Python almacenado dentro de él es el que se invoca cuando escribes python. Además, el prompt del terminal se modifica para incluir el nombre del entorno virtual activado. Los cambios realizados en tu sesión de terminal son todos temporales y privados de esa sesión, así que no persistirán cuando cierres la ventana del terminal. Si trabajas con múltiples ventanas de terminal abiertas al mismo tiempo, está perfectamente bien tener diferentes entornos virtuales activados en cada una.

Ahora que tienes un entorno virtual creado y activado, puedes finalmente instalar Faker en él:

```bash
(venv) $ pip install faker
```

Si quieres confirmar que tu entorno virtual ahora tiene Faker instalado, puedes iniciar el intérprete de Python e importar Faker en él:

```python
>>> import faker
>>> _
```

Si esta declaración no te da ningún error puedes felicitarte, ya que Faker está instalado y listo para ser usado.
