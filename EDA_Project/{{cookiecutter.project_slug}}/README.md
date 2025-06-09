# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

It was automatically generated using Cookiecutter to streamline the creation of robust projects.

---

## 📂 Project Structure

```text
EDA_project/
└── {{cookiecutter.project_slug}}/
    ├── LICENSE                     # Project License
    ├── README.md                   
    ├── data/
    │   ├── cleeaned/               # Clean and processed data
    │   └── raw/                    # Raw data
    ├── environments.yml            # Conda environment with dependencies
    ├── notebooks/                  # Jupyter notebooks for exploration and experiments
    │   └── 01_eda.ipynb
    ├── outputs/
    │   ├── plots/                  # Visualizations generated
    │   └── tables/                 # Summary and statistical tables
    └── src/
        └── __init__.py             # Main source code
```

## ⚙️ Packages

- python={{ cookiecutter.python_version }}
- pandas
- numpy
- matplotlib
- seaborn
- jupyterlab
- jupyter
- ipykernel
- notebook

All dependencies are specified in environment.yml.
Some dependencies may be missing in the environment.yml file, depending on the specific requirements of your project.

To create the environment:

```bash
conda env create -f environments.yml
conda activate <environment-name>
```

## 👤 Author

{{ cookiecutter.author_name }}

## 📄 License

This project is licensed under the {{ cookiecutter.license }}.
See the LICENSE file for more details.
