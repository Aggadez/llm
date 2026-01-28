"""
Aplicación principal de Streamlit para el Asistente de Escritura Automática.

Esta aplicación proporciona una interfaz web intuitiva para:
- Corregir gramática y ortografía
- Mejorar el estilo de textos
- Generar contenido nuevo basado en ideas
"""

import os
from typing import Optional
import streamlit as st
from dotenv import load_dotenv

from services.ai_service import WritingAssistant
from utils.storage_mock import save_draft_to_db


# Cargar variables de entorno desde .env
load_dotenv()


def initialize_session_state() -> None:
    """
    Inicializa las variables de sesión de Streamlit.
    
    Esto asegura que los valores persistan entre recargas de página.
    """
    if 'current_result' not in st.session_state:
        st.session_state.current_result = None
    if 'original_text' not in st.session_state:
        st.session_state.original_text = ""


def get_openai_api_key() -> Optional[str]:
    """
    Obtiene la clave API de Google Gemini desde la barra lateral o variables de entorno.
    
    Returns:
        Clave API de Google Gemini o None si no está disponible.
    """
    api_key = st.sidebar.text_input(
        "🔑 Clave API de Google Gemini",
        value=os.getenv("GOOGLE_API_KEY", ""),
        type="password",
        help="Obtén tu clave en https://makersuite.google.com/app/apikey"
    )
    return api_key if api_key else os.getenv("GOOGLE_API_KEY")


def render_sidebar() -> tuple[str, Optional[str]]:
    """
    Renderiza la barra lateral con opciones de configuración.
    
    Returns:
        Tupla con (modo_seleccionado, api_key).
    """
    st.sidebar.title("⚙️ Configuración")
    
    api_key = get_openai_api_key()
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("📋 Selecciona una opción")
    
    mode = st.sidebar.radio(
        "¿Qué deseas hacer?",
        options=["Corregir Gramática", "Mejorar Estilo", "Generar Contenido"],
        help="Selecciona la funcionalidad que necesitas"
    )
    
    if mode == "Mejorar Estilo":
        tone = st.sidebar.selectbox(
            "Elige el tono deseado:",
            options=["Formal", "Creativo", "Casual"],
            help="Selecciona cómo deseas que suene el texto"
        )
        st.session_state.tone = tone
    
    return mode, api_key


def process_text(assistant: WritingAssistant, mode: str, user_text: str) -> None:
    """
    Procesa el texto del usuario según el modo seleccionado.
    
    Args:
        assistant: Instancia de WritingAssistant.
        mode: Modo de procesamiento seleccionado.
        user_text: Texto proporcionado por el usuario.
    """
    with st.spinner("⏳ Procesando tu texto..."):
        if mode == "Corregir Gramática":
            result = assistant.fix_grammar(user_text)
            if result['success']:
                st.session_state.current_result = result['corrected_text']
            else:
                st.error(f"❌ Error: {result['error']}")
        
        elif mode == "Mejorar Estilo":
            tone = st.session_state.get('tone', 'Formal')
            result = assistant.improve_style(user_text, tone)
            if result['success']:
                st.session_state.current_result = result['improved_text']
            else:
                st.error(f"❌ Error: {result['error']}")
        
        elif mode == "Generar Contenido":
            result = assistant.generate_content(user_text)
            if result['success']:
                st.session_state.current_result = result['generated_text']
            else:
                st.error(f"❌ Error: {result['error']}")


def save_draft(user_id: str = "usuario_anonimo") -> None:
    """
    Guarda el borrador actual en la base de datos simulada.
    
    Args:
        user_id: Identificador del usuario (por defecto: anónimo).
    """
    if st.session_state.current_result:
        success = save_draft_to_db(user_id, st.session_state.current_result)
        if success:
            st.success("✅ Borrador guardado en la BD simulada")
        else:
            st.error("❌ Error al guardar el borrador")
    else:
        st.warning("⚠️ No hay contenido para guardar. Procesa un texto primero.")


def main() -> None:
    """
    Función principal de la aplicación Streamlit.
    """
    # Configuración de la página
    st.set_page_config(
        page_title="Asistente de Escritura IA",
        page_icon="✍️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Inicializar sesión
    initialize_session_state()
    
    # Renderizar barra lateral
    mode, api_key = render_sidebar()
    
    # Contenido principal
    st.title("✍️ Asistente de Escritura Automática")
    st.markdown(
        "Una herramienta potente impulsada por IA para mejorar, corregir y generar textos."
    )
    st.markdown("---")
    
    # Validar API key
    if not api_key:
        st.error(
            "❌ No se encontró clave API de Google Gemini. "
            "Por favor, configúrala en la barra lateral o en el archivo `.env`."
        )
        st.stop()
    
    # Crear instancia de WritingAssistant
    assistant = WritingAssistant(api_key)
    
    # Área de entrada de usuario
    st.subheader(f"📝 {mode}")
    
    if mode == "Generar Contenido":
        placeholder_text = "Ejemplo: 'Escribir un correo de disculpa formal al cliente'..."
        user_input = st.text_area(
            "Describe el tema o idea:",
            placeholder=placeholder_text,
            height=150,
            help="Proporciona la idea o tema para el que deseas generar contenido"
        )
    else:
        placeholder_text = "Pega aquí el texto que deseas procesar..."
        user_input = st.text_area(
            "Ingresa tu texto:",
            placeholder=placeholder_text,
            height=150,
            help="Copia y pega el texto que deseas mejorar o corregir"
        )
    
    # Botones de acción
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 Procesar", use_container_width=True):
            if user_input.strip():
                st.session_state.original_text = user_input
                process_text(assistant, mode, user_input)
            else:
                st.warning("⚠️ Por favor, ingresa algo para procesar.")
    
    with col2:
        if st.button("💾 Guardar Borrador", use_container_width=True):
            save_draft()
    
    with col3:
        if st.button("🔄 Limpiar", use_container_width=True):
            st.session_state.current_result = None
            st.session_state.original_text = ""
            st.rerun()
    
    # Mostrar resultados
    if st.session_state.current_result:
        st.markdown("---")
        st.subheader("✨ Resultado")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.text_area(
                "Resultado procesado:",
                value=st.session_state.current_result,
                height=200,
                disabled=True
            )
        
        with col2:
            if st.button("📋 Copiar al portapapeles"):
                st.write("```")
                st.write(st.session_state.current_result)
                st.write("```")
                st.info("Selecciona el texto y cópialo manualmente")


if __name__ == "__main__":
    main()
