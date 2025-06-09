# {{ cookiecutter.project_name }}

Project created by {{ cookiecutter.autor_name }}

## Description

This project uses Python {{ cookiecutter.python_version }} and is licensed under the {{ cookiecutter.license }}.

## Project Structure

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

## Set Up

To configure the environment, run the following command:

```bash
conda env create -f enviroments.yml
```

## License

This project is licensed under the {{ cookiecutter.license }}.
