import os
import subprocess
import sys

def find_environment_file():
    """Busca archivos de entorno en diferentes formatos y ubicaciones"""
    possible_files = [
        "environment.yml",    # Singular
        "environments.yml",   # Plural
        "conda-env.yml",      # Alternativo
        "env.yml"            # Corto
    ]
    
    for filename in possible_files:
        if os.path.isfile(filename):
            return filename
    return None

def show_environment_packages():
    """Muestra los paquetes del archivo de entorno encontrado"""
    env_file = find_environment_file()
    
    if not env_file:
        print("⚠️  No se encontró archivo de entorno conda")
        print("    Archivos buscados: environment.yml, environments.yml, conda-env.yml, env.yml")
        return False
    
    print(f"\n📦 PAQUETES EN {env_file.upper()}:")
    print("-" * 50)
    
    try:
        with open(env_file, "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.split('\n')
            in_dependencies = False
            package_count = 0
            
            for line in lines:
                stripped_line = line.strip()
                if 'dependencies:' in stripped_line:
                    in_dependencies = True
                    continue
                elif in_dependencies and stripped_line.startswith('- '):
                    package = stripped_line[2:]
                    print(f"  • {package}")
                    package_count += 1
                elif in_dependencies and stripped_line and not line.startswith(' ') and not stripped_line.startswith('-'):
                    break
            
            if package_count == 0:
                print("  (No se encontraron paquetes en la sección dependencies)")
                
    except Exception as e:
        print(f"⚠️  Error leyendo {env_file}: {e}")
        return False
    
    print("-" * 50)
    print(f"📊 Total: {package_count} paquetes")
    return True

def ask_conda_confirmation():
    """Pregunta si quiere crear el entorno después de mostrar los paquetes"""
    print("\n¿Quieres crear el entorno conda con estos paquetes?")
    print("  y/s = Sí, crear entorno ahora")
    print("  n   = No, solo mostrar comandos para después")
    print("  c   = Cancelar todo el proceso")
    print("\nOpción [y]: ", end="")
    
    response = input().lower().strip()
    
    if response in ['c', 'cancel', 'cancelar']:
        print("❌ Proceso cancelado por el usuario")
        # Limpiar archivos generados
        import shutil
        project_dir = os.getcwd()
        parent_dir = os.path.dirname(project_dir)
        project_name = os.path.basename(project_dir)
        os.chdir(parent_dir)
        try:
            shutil.rmtree(project_name)
            print(f"🗑️  Directorio {project_name} eliminado")
        except Exception:
            print(f"⚠️  No se pudo eliminar el directorio {project_name}")
        sys.exit(0)
    elif response in ['n', 'no']:
        return False
    else:  # default 'y', 'yes', etc.
        return True

def create_conda_env():
    """Create a Conda environment from environment file"""
    create_env = "{{ cookiecutter.create_conda_env }}"
    env_name = "{{ cookiecutter.conda_env_name }}"
    
    print("\n🔧 CONFIGURACIÓN DEL ENTORNO CONDA")
    print("=" * 50)
    
    # Buscar y mostrar archivo de entorno
    env_file = find_environment_file()
    packages_found = show_environment_packages()
    
    if not packages_found:
        print("❌ No se puede continuar sin archivo de entorno")
        return
    
    # Determinar qué hacer
    should_create = False
    
    if create_env.lower() == "yes":
        should_create = ask_conda_confirmation()
    elif create_env.lower() == "no":
        should_create = False
    
    # Proceder según la decisión
    if should_create:
        try:
            print(f"\n🚀 Creando entorno '{env_name}' desde {env_file}...")
            result = subprocess.run(
                ["conda", "env", "create", "-f", env_file, "-n", env_name], 
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                print(f"✅ Entorno '{env_name}' creado exitosamente!")
                print(f"\n💡 Para activarlo usa:")
                print(f"   conda activate {env_name}")
            else:
                print(f"❌ Error creando el entorno:")
                print(f"   {result.stderr}")
                print(f"\n💡 Puedes crearlo manualmente:")
                print(f"   conda env create -f {env_file} -n {env_name}")
                
        except FileNotFoundError:
            print("❌ conda no está instalado o no está en el PATH")
            print(f"💡 Instala conda y ejecuta:")
            print(f"   conda env create -f {env_file} -n {env_name}")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print(f"\n📋 ENTORNO NO CREADO")
        print(f"💡 Para crearlo cuando quieras:")
        print(f"   conda env create -f {env_file} -n {env_name}")
        print(f"   conda activate {env_name}")

def init_git():
    """Inicializa el repositorio Git y realiza un commit inicial."""
    try:
        subprocess.run(["git", "init"], check=True, capture_output=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True, capture_output=True)
        print("✅ Repositorio Git inicializado")
    except subprocess.CalledProcessError:
        print("⚠️  Error inicializando Git")
    except FileNotFoundError:
        print("⚠️  Git no está instalado")

def cleanup_files():
    """Limpiar archivos no necesarios."""
    files_to_remove = [".DS_Store", "Thumbs.db", "desktop.ini"]
    dirs_to_remove = ["__pycache__", ".pytest_cache"]
    removed_count = 0
    
    # Limpiar recursivamente
    for root, dirs, files in os.walk("."):
        # Remover directorios
        for dir_name in list(dirs):
            if dir_name in dirs_to_remove:
                dir_path = os.path.join(root, dir_name)
                try:
                    subprocess.run(["rm", "-rf", dir_path], check=True)
                    removed_count += 1
                except Exception:
                    pass
        
        # Remover archivos
        for file in files:
            if file in files_to_remove or file.endswith('.pyc'):
                try:
                    os.remove(os.path.join(root, file))
                    removed_count += 1
                except Exception:
                    pass
    
    if removed_count > 0:
        print(f"🧹 {removed_count} archivos/directorios temporales eliminados")

def show_final_summary():
    """Muestra un resumen final del proyecto configurado"""
    env_name = "{{ cookiecutter.conda_env_name }}"
    create_env = "{{ cookiecutter.create_conda_env }}"
    
    print(f"\n📋 RESUMEN DEL PROYECTO:")
    print(f"   • Nombre: {{ cookiecutter.project_name }}")
    print(f"   • Directorio: {{ cookiecutter.project_slug }}")
    print(f"   • Autor: {{ cookiecutter.author_name }}")
    
    if create_env.lower() == "yes":
        print(f"   • Entorno conda: {env_name}")
        print(f"   • Para activar: conda activate {env_name}")
    else:
        print(f"   • Entorno conda: {env_name} (no creado)")
    
    print(f"   • Git: Repositorio inicializado")

def main():
    """Función principal que ejecuta todas las tareas post-generación."""
    print("\n🚀 CONFIGURANDO PROYECTO")
    print("=" * 60)

    # Configurar entorno conda
    create_conda_env()

    # Limpiar archivos no necesarios
    print("\n🧹 Limpiando archivos temporales...")
    cleanup_files()

    # Inicializar repositorio git
    print("\n📚 Inicializando repositorio Git...")
    init_git()

    # Mostrar resumen
    show_final_summary()

    print("\n🎉 ¡PROYECTO CONFIGURADO EXITOSAMENTE!")

if __name__ == "__main__":
    main()