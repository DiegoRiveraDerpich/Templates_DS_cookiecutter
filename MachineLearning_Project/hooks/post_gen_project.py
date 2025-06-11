import os
import subprocess
import sys

def find_environment_file():
    """Search for environment files in different formats and locations."""
    possible_files = [
        "environment.yml",    # Singular
        "environments.yml",   # Plural
        "conda-env.yml",      # Alternative
        "env.yml"            # Short
    ]
    
    for filename in possible_files:
        if os.path.isfile(filename):
            return filename
    return None

def show_environment_packages():
    """Displays the packages of the found environment file"""
    env_file = find_environment_file()
    
    if not env_file:
        print("⚠️  No environment file found conda")
        print("    Wanted files: environment.yml, environments.yml, conda-env.yml, env.yml")
        return False
    
    print(f"\n📦 PACKAGES IN {env_file.upper()}:")
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
                print("  (No packages found in the dependencies section)")
                
    except Exception as e:
        print(f"⚠️  Error reading {env_file}: {e}")
        return False
    
    print("-" * 50)
    print(f"📊 Total: {package_count} packages")
    return True

def ask_conda_confirmation():
    """Ask if you want to create the environment after displaying the packages"""
    print("\nDo you want to create the conda environment with these packages?")
    print("  y  = Yes, create environment now")
    print("  n  = No, just display commands for later")
    print("  c  = Cancel the entire process")
    print("\nOption [y]: ", end="")
    
    response = input().lower().strip()
    
    if response in ['c', 'cancel']:
        print("❌ Process canceled by user")
        # Clean generated files
        import shutil
        project_dir = os.getcwd()
        parent_dir = os.path.dirname(project_dir)
        project_name = os.path.basename(project_dir)
        os.chdir(parent_dir)
        try:
            shutil.rmtree(project_name)
            print(f"🗑️  Directory {project_name} eliminated")
        except Exception:
            print(f"⚠️  Could not delete the directory {project_name}")
        sys.exit(0)
    elif response in ['n', 'no']:
        return False
    else:  # default 'y', 'yes', etc.
        return True

def create_conda_env():
    """Create a Conda environment from environment file"""
    create_env = "{{ cookiecutter.create_conda_env }}"
    env_name = "{{ cookiecutter.conda_env_name }}"
    
    print("\n🔧 CONDA ENVIRONMENT CONFIGURATION")
    print("=" * 50)
    
    # Search and display environment file
    env_file = find_environment_file()
    packages_found = show_environment_packages()
    
    if not packages_found:
        print("❌ Cannot continue without environment file")
        return
    
    # Determine what to do
    should_create = False
    
    if create_env.lower() == "yes":
        should_create = ask_conda_confirmation()
    elif create_env.lower() == "no":
        should_create = False
    
    # Proceed according to the decision
    if should_create:
        try:
            print(f"\n🚀 Creating environment '{env_name}' from {env_file}...")
            result = subprocess.run(
                ["conda", "env", "create", "-f", env_file, "-n", env_name], 
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                print(f"✅ Environment '{env_name}' successfully created!")
                print(f"\n💡 To activate it use:")
                print(f"   conda activate {env_name}")
            else:
                print(f"❌ Error creating the environment:")
                print(f"   {result.stderr}")
                print(f"\n💡 You can create it manually:")
                print(f"   conda env create -f {env_file} -n {env_name}")
                
        except FileNotFoundError:
            print("❌ conda is not installed or not in the PATH")
            print(f"💡 Install conda and run:")
            print(f"   conda env create -f {env_file} -n {env_name}")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print(f"\n📋 UNCREATED ENVIRONMENT")
        print(f"💡 To create it whenever you want:")
        print(f"   conda env create -f {env_file} -n {env_name}")
        print(f"   conda activate {env_name}")

def init_git():
    """Initializes the Git repository and performs an initial commit."""
    try:
        subprocess.run(["git", "init"], check=True, capture_output=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True, capture_output=True)
        print("✅ Initialized Git repository")
    except subprocess.CalledProcessError:
        print("⚠️  Error initializing Git")
    except FileNotFoundError:
        print("⚠️  Git is not installed")

def cleanup_files():
    """Clean unneeded files."""
    files_to_remove = [".DS_Store", "Thumbs.db", "desktop.ini"]
    dirs_to_remove = ["__pycache__", ".pytest_cache"]
    removed_count = 0
    
    # Recursive cleaning
    for root, dirs, files in os.walk("."):
        # Remove directories
        for dir_name in list(dirs):
            if dir_name in dirs_to_remove:
                dir_path = os.path.join(root, dir_name)
                try:
                    subprocess.run(["rm", "-rf", dir_path], check=True)
                    removed_count += 1
                except Exception:
                    pass
        
        # Remove archives
        for file in files:
            if file in files_to_remove or file.endswith('.pyc'):
                try:
                    os.remove(os.path.join(root, file))
                    removed_count += 1
                except Exception:
                    pass
    
    if removed_count > 0:
        print(f"🧹 {removed_count} deleted temporary files/directories")

def show_final_summary():
    """Displays a final summary of the configured project"""
    env_name = "{{ cookiecutter.conda_env_name }}"
    create_env = "{{ cookiecutter.create_conda_env }}"
    
    print(f"\n📋 PROJECT SUMMARY:")
    print(f"   • Name: {{ cookiecutter.project_name }}")
    print(f"   • Directories: {{ cookiecutter.project_slug }}")
    print(f"   • Author: {{ cookiecutter.author_name }}")
    
    if create_env.lower() == "yes":
        print(f"   • Environment conda: {env_name}")
        print(f"   • To activate: conda activate {env_name}")
    else:
        print(f"   • Environment conda: {env_name} (not created)")
    
    print(f"   • Git: Initialized repository")

def main():
    """Main function that executes all post-generation tasks."""
    print("\n🚀 CONFIGURING PROJECT")
    print("=" * 60)

    # Configure conda environment
    create_conda_env()

    # Clean unneeded files
    print("\n🧹 Cleaning up temporary files...")
    cleanup_files()

    # Initialize git repository
    print("\n📚 Initializing Git repository...")
    init_git()

    # Mostrar resumen
    show_final_summary()

    print("\n🎉 PROJECT SUCCESSFULLY CONFIGURED!")

if __name__ == "__main__":
    main()