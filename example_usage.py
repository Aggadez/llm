"""
Ejemplo de uso del módulo WritingAssistant.

Este script demuestra cómo usar la clase WritingAssistant de forma programática,
sin necesidad de la interfaz Streamlit.
"""

import os
from dotenv import load_dotenv
from services.ai_service import WritingAssistant


def main() -> None:
    """
    Ejecuta ejemplos de uso del WritingAssistant.
    """
    # Cargar variables de entorno
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ Error: GOOGLE_API_KEY no está configurada en .env")
        print("   Obtén tu clave en: https://makersuite.google.com/app/apikey")
        return
    
    # Crear instancia del asistente
    assistant = WritingAssistant(api_key)
    
    print("\n" + "="*60)
    print("  EJEMPLOS DE USO: ASISTENTE DE ESCRITURA CON GEMINI")
    print("="*60)
    
    # Ejemplo 1: Corregir gramática
    print("\n\n📝 EJEMPLO 1: Corrección de Gramática")
    print("-" * 60)
    
    text_to_correct = "Hola, me gustaria saber como puedo mejorar mi escritura. Mi gramatica no es muy buena."
    print(f"\nTexto original:\n{text_to_correct}")
    
    result = assistant.fix_grammar(text_to_correct)
    if result['success']:
        print(f"\nTexto corregido:\n{result['corrected_text']}")
    else:
        print(f"Error: {result['error']}")
    
    # Ejemplo 2: Mejorar estilo (Formal)
    print("\n\n📝 EJEMPLO 2: Mejora de Estilo (Formal)")
    print("-" * 60)
    
    text_to_improve = "Oye, quería preguntarte si podemos juntarnos mañana para hablar del proyecto."
    print(f"\nTexto original:\n{text_to_improve}")
    
    result = assistant.improve_style(text_to_improve, "Formal")
    if result['success']:
        print(f"\nTexto mejorado (Formal):\n{result['improved_text']}")
    else:
        print(f"Error: {result['error']}")
    
    # Ejemplo 3: Mejorar estilo (Creativo)
    print("\n\n📝 EJEMPLO 3: Mejora de Estilo (Creativo)")
    print("-" * 60)
    
    text_to_improve = "El sol brilla en el cielo azul."
    print(f"\nTexto original:\n{text_to_improve}")
    
    result = assistant.improve_style(text_to_improve, "Creativo")
    if result['success']:
        print(f"\nTexto mejorado (Creativo):\n{result['improved_text']}")
    else:
        print(f"Error: {result['error']}")
    
    # Ejemplo 4: Generar contenido
    print("\n\n📝 EJEMPLO 4: Generación de Contenido")
    print("-" * 60)
    
    topic = "Escribir un correo formal disculpándome por un retraso en la entrega"
    print(f"\nTema:\n{topic}")
    
    result = assistant.generate_content(topic)
    if result['success']:
        print(f"\nContenido generado:\n{result['generated_text']}")
    else:
        print(f"Error: {result['error']}")
    
    print("\n" + "="*60)
    print("  FIN DE LOS EJEMPLOS")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
