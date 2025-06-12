# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

Fue generado automáticamente usando Cookiecutter para agilizar la creación de proyectos robustos.

---

## 📂 Estructura del Proyecto

```text
EDA_project/
└── {{cookiecutter.project_slug}}/
    ├── LICENSE                     # Licencia del proyecto
    ├── README.md                   # Este archivo
    ├── data/
    │   ├── cleeaned/               # Datos limpios y procesados
    │   └── raw/                    # Datos crudos sin procesar
    ├── environments.yml            # Entorno Conda con dependencias
    ├── notebooks/                  # Jupyter notebooks para exploración y experimentos
    │   └── 01_eda.ipynb
    ├── outputs/
    │   ├── plots/                  # Visualizaciones generadas
    │   └── tables/                 # Tablas resumen y estadísticas
    └── src/
        └── __init__.py             # Módulo principal de código fuente
```

## ⚙️ Dependencias principales

- python={{ cookiecutter.python_version }}  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- jupyterlab  
- jupyter  
- ipykernel  
- notebook  

Todas las dependencias están especificadas en environment.yml.  
Es posible que falten algunas dependencias en el archivo environment.yml, dependiendo de los requisitos específicos de tu proyecto.

Para crear el entorno:

```bash
conda env create -f environments.yml
conda activate <nombre_del_entorno>
```

## 👤 Autor

{{ cookiecutter.author_name }}

## 📄 Licencia

Este proyecto está licenciado bajo la licencia {{ cookiecutter.license }}.  
Consulta el archivo LICENSE para más detalles.
