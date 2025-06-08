# 🚀 Data Science Project Templates

A set of ready-to-use templates that provide a solid and organized structure for beginning Data Science projects. These templates include everything you need to get started quickly with good organization, dependency management and automation practices..

## ✨ Features

📁 Organized Structure: Predifine folders for data, notebooks, scripts and docs
🐍 Environment management: environments.yml and requirements.txt included
🔧 Automatization: Post-hooks for automatic dependencies instalation
🔄 Git integrado: Configuración automática de Git y limpieza de archivos
📊 Organized notebooks: Clear structure for exploratory analysis and modeling
🧹 Automatic cleanup: Temporary files and cache deletion

## 🛠️ Prerequisites

Before using these templates, make sure you have installed:

Conda - For the creation and management of virtual environments
Cookiecutter - For template generation.

## Cookiecutter installation

```bash
# pip
pip install cookiecutter

# Conda
conda install cookiecutter
```

## 🚀 Obtaining Templates

```bash
 # Clone repository
git clone https://github.com/DiegoRiveraDerpich/Templates_DS_cookiecutter.git

# Navigate directory
cd your-repository

# Use template from local directory
cookiecutter template-directory

# Example
cookiecutter EDA_project
```

## Crear un nuevo proyecto

```bash
cookiecutter template-directory

# Example
cookiecutter EDA_project
```

Follow the interactive instructions to configure your project with:

Project name
Description
Author
Specific settings

Initial configuration
Once the project is created, post-hooks will automatically take care of:

Create the conda environment
Install dependencies
Initialize the Git repository
Configure cleanup files

## 🤝 Contributions

Contributions are welcome. Please:

Fork the repository
Create a branch for your feature (git checkout -b feature/new-feature)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/new-feature)
Create a Pull Request

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for more details.

## 🆘 Soporte

If you encounter any problems or have suggestions:

Open an issue
Consult the documentation
Contact the maintainer

## 🙏 Acknowledgments

Inspired by the best practices of the Data Science community
Based on Cookiecutter Data Science

## ⭐ Don't forget to give a star to the repository if you find it useful
