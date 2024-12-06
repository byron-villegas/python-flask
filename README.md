# Crear Environment
Se debe ejecutar el siguiente comando

```shell
python3 -m venv .venv
```

# Instalar librerias
Se debe ejecutar el siguiente comando

```shell
pip install -r requirements.txt
```

# Librerias exclusivas para windows
Cuando nos encontremos con una libreria exclusiva para windows debemos agregarle **;sys_platform == 'win32'** al final de la version en el archivo **requirements.txt**

Ejemplo

```txt
pywin32==306;sys_platform == 'win32'
```
Entonces cuando hagamos un pip install -r requirements.txt en un sistema operativo como linux, macOS excluira esa libreria

# Actualizar requirements.txt
Se debe ejecutar el siguiente comando

```shell
pip freeze > requirements.txt
pip list --format json > requirements.json
```

# Listar librerias en formato json
Se debe ejecutar el siguiente comando

```shell
pip list --format json
```

# Ejecutar aplicacion
Se debe ejecutar el siguiente comando

```shell
flask --app app run
```

# Tests Unitarios
### Configurar rutas
Se debe crear un archivo pyproject con el siguiente contenido

```python
[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.coverage.run]
branch = true
source = ["config", "app"]
```

### Ejecutarlo
Se debe ejecutar el siguiente comando

```shell
pytest
```

### Ejecutarlo con cobertura
Se debe ejecutar el siguiente comando

```shell
coverage run -m pytest
```

### Generar reporte de cobertura en consola
Se debe ejecutar el siguiente comando

```shell
coverage report
```

### Generar reporte html de cobertura
Se debe ejecutar el siguiente comando

```shell
coverage html
```

# Tests de Rendimiento
Se debe ejecutar el siguiente comando

```shell
locust -f performance-test/locust/python-flask.py -H http://localhost:5000 -u 5 -r 10 -t 40 --headless --html locust-report.html
```

Al finalizar generara un reporte locust-report.html

# Tests de Aceptación
Se debe ejecutar el siguiente comando

```shell
behave acceptance-test/features -f html -o behave-report.html
```

# Links Referenciales
A continuación dejo links utilizados para realizar este proyecto

[Python Naming Conventions](https://www.geeksforgeeks.org/python-naming-conventions/)

[Configuring Your Flask App](https://dev.to/hackersandslackers/configuring-your-flask-app-2246)

[Flask How To Make Validation On Request JSON](https://stackoverflow.com/questions/61644396/flask-how-to-make-validation-on-request-json-and-json-schema)

[Change Host and Port Of Flask On Run](https://stackoverflow.com/questions/41940663/how-can-i-change-the-host-and-port-that-the-flask-command-uses)

[Performance Testing in Python: A Step-by-Step Guide with Locust](https://code.likeagirl.io/performance-testing-in-python-a-step-by-step-guide-with-flask-e5a56f99513d)

[How To Run Locust](https://appian-locust.readthedocs.io/en/stable/how_to_run_locust.html)

[Behave](https://behave.readthedocs.io/en/latest/tutorial/)
