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