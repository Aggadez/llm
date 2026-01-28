"""
Módulo de almacenamiento simulado para el Asistente de Escritura.

Este módulo proporciona funciones para simular la persistencia de datos
sin conectarse a una base de datos real.
"""

from typing import Optional


def save_draft_to_db(user_id: str, text: str) -> bool:
    """
    Simula el guardado de un borrador en una base de datos.
    
    En una aplicación real, esto escribiría en una base de datos como PostgreSQL,
    MongoDB o Firestore. Por ahora, simplemente imprime en consola y retorna True.
    
    Args:
        user_id: Identificador único del usuario.
        text: Contenido del borrador a guardar.
        
    Returns:
        True si el guardado fue simulado exitosamente.
    """
    try:
        print(f"\n🔄 Simulando conexión a DB...")
        print(f"💾 Guardando borrador del usuario {user_id}...")
        print(f"📝 Contenido: {text[:50]}..." if len(text) > 50 else f"📝 Contenido: {text}")
        print("✅ Borrador guardado exitosamente en la BD simulada.\n")
        return True
    
    except Exception as e:
        print(f"❌ Error al guardar el borrador: {str(e)}\n")
        return False
