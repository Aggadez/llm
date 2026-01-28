"""
Script de validación para verificar la estructura del proyecto.

Este script comprueba que todos los archivos y dependencias estén correctamente configurados.
"""

import os
import sys
from pathlib import Path


def check_project_structure() -> bool:
    """
    Verifica que la estructura del proyecto sea correcta.
    
    Returns:
        True si la estructura es válida, False en caso contrario.
    """
    required_files = [
        'app.py',
        'requirements.txt',
        '.env.example',
        'README.md',
        'services/ai_service.py',
        'services/__init__.py',
        'utils/storage_mock.py',
        'utils/__init__.py',
    ]
    
    print("🔍 Verificando estructura del proyecto...\n")
    
    all_valid = True
    for file in required_files:
        path = Path(file)
        if path.exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - NO ENCONTRADO")
            all_valid = False
    
    return all_valid


def check_dependencies() -> bool:
    """
    Verifica que las dependencias requeridas estén instaladas.
    
    Returns:
        True si todas las dependencias están instaladas.
    """
    print("\n\n📦 Verificando dependencias...\n")
    
    required_packages = ['streamlit', 'google', 'dotenv']
    all_valid = True
    
    for package in required_packages:
        try:
            if package == 'google':
                import google.generativeai
            else:
                __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - NO INSTALADO")
            if package == 'google':
                print(f"   Ejecuta: pip install google-generativeai")
            else:
                print(f"   Ejecuta: pip install {package}")
            all_valid = False
    
    return all_valid


def check_env_configuration() -> bool:
    """
    Verifica que el archivo .env esté configurado.
    
    Returns:
        True si el .env existe y está configurado.
    """
    print("\n\n🔐 Verificando configuración de entorno...\n")
    
    if os.path.exists('.env'):
        print("✅ Archivo .env encontrado")
        
        with open('.env', 'r') as f:
            content = f.read()
            if 'GOOGLE_API_KEY' in content and not content.strip().endswith('aqui'):
                print("✅ GOOGLE_API_KEY configurada")
                return True
            else:
                print("❌ GOOGLE_API_KEY no está configurada correctamente")
                print("   Edita .env y añade tu clave de Google Gemini")
                return False
    else:
        print("⚠️  Archivo .env no encontrado")
        print("   Copia .env.example a .env y configura tu clave API")
        return False


def main() -> None:
    """
    Ejecuta todas las validaciones.
    """
    print("\n" + "="*60)
    print("  VALIDACIÓN DEL PROYECTO: ASISTENTE DE ESCRITURA IA")
    print("="*60 + "\n")
    
    structure_valid = check_project_structure()
    dependencies_valid = check_dependencies()
    env_valid = check_env_configuration()
    
    print("\n" + "="*60)
    
    if structure_valid and dependencies_valid and env_valid:
        print("\n✅ ¡TODO ESTÁ LISTO! Puedes ejecutar:")
        print("\n   streamlit run app.py\n")
    else:
        print("\n⚠️  Hay problemas a resolver antes de ejecutar la aplicación.")
        print("    Revisa los mensajes arriba.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
