# 🚀 Plantillas para Proyectos de Data Science

Un conjunto de plantillas listas para usar que proporcionan una estructura sólida y organizada para proyectos de Data Science principiantes. Estas plantillas incluyen todo lo necesario para comenzar rápidamente con buenas prácticas de organización, gestión de dependencias y automatización.

## ✨ Características

📁 Estructura organizada: Carpetas predefinidas para datos, notebooks, scripts y documentación
🐍 Gestión de ambientes: Archivos environment.yml y requirements.txt incluidos
🔧 Automatización: Post-hooks para instalación automática de dependencias
🔄 Git integrado: Configuración automática de Git y limpieza de archivos
📊 Notebooks organizados: Estructura clara para análisis exploratorio y modelado
🧹 Limpieza automática: Eliminación de archivos temporales y cache

## 🛠️ Requisitos Previos

Antes de usar estas plantillas, asegúrate de tener instalado:

Conda - Para la creación y gestión de ambientes virtuales
Cookiecutter - Para la generación de plantillas

## Instalación de Cookiecutter

```bash
# Con pip
pip install cookiecutter

# Con conda
conda install cookiecutter
```

## 🚀 Obtencion Plantillas en Local

```bash
 # Clonar el repositorio
git clone https://github.com/DiegoRiveraDerpich/Templates_DS_cookiecutter.git

# Navegar al directorio
cd tu-repositorio

# Usar la plantilla desde el directorio local
cookiecutter plantilla-seleccionada
```

## Crear un nuevo proyecto

```bash
cookiecutter Plantilla-seleccionada
```

Sigue las instrucciones interactivas para configurar tu proyecto con:

Nombre del proyecto
Descripción
Autor
Configuraciones específicas

Configuración inicial
Una vez creado el proyecto, los post-hooks se encargarán automáticamente de:

Crear el ambiente conda
Instalar las dependencias
Inicializar el repositorio Git
Configurar los archivos de limpieza

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

Fork el repositorio
Crea una rama para tu feature (git checkout -b feature/nueva-caracteristica)
Commit tus cambios (git commit -am 'Añade nueva característica')
Push a la rama (git push origin feature/nueva-caracteristica)
Crea un Pull Request

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

## 🆘 Soporte

Si encuentras algún problema o tienes sugerencias:

Abre un issue
Consulta la documentación
Contacta al mantenedor

🙏 Reconocimientos

Inspirado en las mejores prácticas de la comunidad de Data Science
Basado en el Cookiecutter Data Science

⭐ ¡No olvides dar una estrella al repositorio si te resulta útil!
