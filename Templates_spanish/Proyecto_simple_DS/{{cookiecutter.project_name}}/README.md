# {{ cookiecutter.project_name }}

Proyecto creado por {{ cookiecutter.autor_name }}

## Descripcion

Este proyecto usa Python {{ cookiecutter.python_version }} y esta bajo la licencia {{ cookiecutter.license }}.

## Estructura del Proyecto

```text
template1/  
├── cookiecutter.json  
└── {{cookiecutter.project_name}}  
    ├── LICENSE  
    ├── README.md  
    ├── data  
    ├── enviroments.yml  
    ├── notebooks  
    │   ├── exploration.ipynb  
    │   └── modeling.ipynb  
    ├── requirements.txt  
    ├── src  
    │   ├── __init__.py  
    │   ├── data_processing.py  
    │   └── model.py  
    └── test
```

## Requisitos

- Python {{ cookiecutter.python_version }}

## Instalacion

Para configurar el ambiente, ejecute el siguiente comando:

```bash
conda env create -f enviroments.yml
```

## Licencia

Este proyecto esta bajo la licencia {{ cookiecutter.license }}.
