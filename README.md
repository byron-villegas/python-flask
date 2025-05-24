# Python Flask Project

Proyecto base para aplicaciones Flask con ejemplos de configuración, testing y buenas prácticas.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Ejecutar Aplicación](#ejecutar-aplicación)
- [Testing](#testing)
- [Tests de Rendimiento](#tests-de-rendimiento)
- [Tests de Aceptación](#tests-de-aceptación)
- [Links de Referencia](#links-de-referencia)

## Instalación
### Instalar Python
Para instalar python debemos bajarlo e instalarlo de la siguiente pagina https://www.python.org/downloads/

### Crear Entorno Virtual
Para crear el entorno virtual debemos ejecutar el siguiente comando

```shell
python3 -m venv .venv
```

### Instalar Dependencias
Para instalar las dependencias debemos ejecutar el siguiente comando

```shell
pip install -r requirements.txt
```

#### Dependencias Exclusivas Windows
Cuando nos encontremos con una depencia exclusiva para windows debemos agregarle **;sys_platform == 'win32'** al final de la version de la dependencia en el archivo **requirements.txt**

Ejemplo

```txt
pywin32==306;sys_platform == 'win32'
```
Entonces cuando instalemos las dependencias del proyecto en un sistema operativo como linux, macOS excluira esa libreria

### Actualizar Dependencias
Para actualizar las dependencias en el archivo **requeriments.txt** debemos ejecutar el siguiente comando

```shell
pip freeze > requirements.txt
```

### Crear Archivo Dependencias Formato JSON
Para crear el archivo de dependencias en formato JSON debemos ejecutar el siguiente comando

```shell
pip list --format json > requirements.json
```

### Listar Dependencias Formato JSON
Se debe ejecutar el siguiente comando

```shell
pip list --format json
```

## Ejecutar Aplicación
Se debe ejecutar el siguiente comando

```shell
flask --app app run
```

## Testing
### Configuración
Se debe crear un archivo **pyproject.toml** con el siguiente contenido

```python
[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.coverage.run]
branch = true
source = ["config", "app"]
```

Esta configuracion permite definir la ruta de los tests, las carpetas que debe considerar el reporte de cobertura de codigo

### Ejecutar
Se debe ejecutar el siguiente comando

```shell
pytest
```

### Ejecutar con Cobertura
Se debe ejecutar el siguiente comando

```shell
coverage run -m pytest
```

### Generar Reporte Cobertura Formato Consola
Se debe ejecutar el siguiente comando

```shell
coverage report
```

### Generar Reporte Cobertura Formato HTML
Se debe ejecutar el siguiente comando

```shell
coverage html
```

## Tests de Aceptación
### Configuración
Se debe crear un archivo **behave.ini** 

Se debe ejecutar el siguiente comando

```shell
behave acceptance-test/features -f html -o behave-report.html
```

Esta configuracion permite definir donde se encuentran los features, el formato html y el nombre del archivo del reporte

## Tests de Rendimiento
Se debe ejecutar el siguiente comando

```shell
locust -f performance-test/locust/python-flask.py -H http://localhost:5000 -u 5 -r 10 -t 40 --headless --html locust-report.html
```

Al finalizar generara un reporte locust-report.html

## Links de Referencia
A continuación dejo links utilizados para realizar este proyecto

[Python Naming Conventions](https://www.geeksforgeeks.org/python-naming-conventions/)

[Configuring Your Flask App](https://dev.to/hackersandslackers/configuring-your-flask-app-2246)

[Flask How To Make Validation On Request JSON](https://stackoverflow.com/questions/61644396/flask-how-to-make-validation-on-request-json-and-json-schema)

[Change Host and Port Of Flask On Run](https://stackoverflow.com/questions/41940663/how-can-i-change-the-host-and-port-that-the-flask-command-uses)

[Performance Testing in Python: A Step-by-Step Guide with Locust](https://code.likeagirl.io/performance-testing-in-python-a-step-by-step-guide-with-flask-e5a56f99513d)

[How To Run Locust](https://appian-locust.readthedocs.io/en/stable/how_to_run_locust.html)

[Behave](https://behave.readthedocs.io/en/latest/tutorial/)
