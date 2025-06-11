# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

It was automatically generated using Cookiecutter to streamline the creation of robust projects.

---

## 📂 Project Structure

```text
{{ cookiecutter.project_slug }}/
├── data/               # Raw, processed and external data
│   ├── raw/
│   ├── processed/
│   └── external/
├── notebooks/           # Jupyter notebooks for exploration and experiments
├── src/                 # Source code of the project
│   ├── data/            # Data loading and transformation scripts
│   ├── features/        # Variable engineering scripts
│   ├── models/          # Model training and prediction
│   └── visualization/   # Result visualization scripts.
├── tests/               # Unit Tests
├── environment.yml      # Conda environment with dependencies
├── README.md            # Project Documentation
└── .gitignore           # Files and folders ignored by git
```

## ⚙️ Packages

Python {{ cookiecutter.python_version }}
numpy
pandas
scikit-learn
matplotlib
seaborn
jupyter
scipy
tqdm

All dependencies are specified in environment.yml.
Some dependencies may be missing in the environment.yml file, depending on the specific requirements of your project. For example:

Deep Learning: tensorflow, pytorch.
Hyperparameter optimization: optuna, scikit-optimize.
Time series analysis: statsmodels, pmdarima.
Advanced visualization: plotly, bokeh.
Natural language processing: nltk, spacy, transformers.
Be sure to review the needs of your project and add the necessary packages.

## 👤 Author

{{ cookiecutter.author_name }}

## 📄 License

This project is licensed under the {{ cookiecutter.license }}.
See the LICENSE file for more details.
