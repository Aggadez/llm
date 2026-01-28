"""
Módulo de servicio de IA para el Asistente de Escritura.

Este módulo contiene la clase WritingAssistant que interactúa con la API de Google Gemini
para proporcionar servicios de corrección de gramática, mejora de estilo y generación
de contenido.
"""

from typing import Optional
import google.generativeai as genai


class WritingAssistant:
    """
    Asistente de escritura que utiliza Google Gemini para mejorar y generar textos.
    
    Attributes:
        api_key (str): Clave API de Google Gemini.
        model_name (str): Nombre del modelo a utilizar (por defecto: gemini-pro).
    """
    
    def __init__(self, api_key: str, model_name: str = "gemini-2.5-flash") -> None:
        """
        Inicializa el asistente de escritura.
        
        Args:
            api_key: Clave API de Google Gemini (API gratuita).
            model_name: Nombre del modelo a utilizar. Por defecto es gemini-2.5-flash.
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
    
    def fix_grammar(self, text: str) -> dict:
        """
        Corrige la gramática y la ortografía del texto proporcionado.
        
        Args:
            text: Texto a corregir.
            
        Returns:
            Diccionario con las claves:
            - 'success': Boolean indicando si fue exitoso.
            - 'corrected_text': Texto corregido.
            - 'error': Mensaje de error (si ocurrió).
        """
        try:
            prompt = f"""Eres un experto corrector de gramática y ortografía en español. 
Corrige el siguiente texto manteniendo el mismo significado y tono. 
Devuelve solo el texto corregido sin explicaciones adicionales.

Texto: {text}"""
            
            response = self.model.generate_content(prompt)
            corrected_text = response.text.strip()
            
            return {
                'success': True,
                'corrected_text': corrected_text,
                'error': None
            }
        
        except Exception as e:
            return {
                'success': False,
                'corrected_text': None,
                'error': f'Error: {str(e)}'
            }
    
    def improve_style(self, text: str, tone: str) -> dict:
        """
        Mejora el estilo del texto según el tono especificado.
        
        Args:
            text: Texto a mejorar.
            tone: Tono deseado (Formal, Creativo, Casual).
            
        Returns:
            Diccionario con las claves:
            - 'success': Boolean indicando si fue exitoso.
            - 'improved_text': Texto mejorado.
            - 'error': Mensaje de error (si ocurrió).
        """
        tone_instructions = {
            'Formal': 'Usa un lenguaje profesional y cortés. Mantén estructuras de oraciones complejas.',
            'Creativo': 'Usa un lenguaje imaginativo y expresivo. Incluye metáforas y descripción vivida.',
            'Casual': 'Usa un lenguaje relajado y conversacional. Como si hablaras con un amigo.'
        }
        
        instructions = tone_instructions.get(tone, tone_instructions['Formal'])
        
        try:
            prompt = f"""Eres un experto editor de textos en español. 
Reescribe el siguiente texto manteniendo el contenido pero cambiando el estilo. 
Instrucción de tono: {instructions}
Devuelve solo el texto reescrito sin explicaciones.

Texto: {text}"""
            
            response = self.model.generate_content(prompt)
            improved_text = response.text.strip()
            
            return {
                'success': True,
                'improved_text': improved_text,
                'error': None
            }
        
        except Exception as e:
            return {
                'success': False,
                'improved_text': None,
                'error': f'Error: {str(e)}'
            }
    
    def generate_content(self, topic: str) -> dict:
        """
        Genera contenido nuevo basado en un tema o idea proporcionada.
        
        Args:
            topic: Tema o idea para generar contenido.
            
        Returns:
            Diccionario con las claves:
            - 'success': Boolean indicando si fue exitoso.
            - 'generated_text': Contenido generado.
            - 'error': Mensaje de error (si ocurrió).
        """
        try:
            prompt = f"""Eres un escritor talentoso en español. 
Crea contenido original, bien estructurado y atractivo basado en el siguiente tema:

Tema: {topic}

Devuelve el contenido generado."""
            
            response = self.model.generate_content(prompt)
            generated_text = response.text.strip()
            
            return {
                'success': True,
                'generated_text': generated_text,
                'error': None
            }
        
        except Exception as e:
            return {
                'success': False,
                'generated_text': None,
                'error': f'Error: {str(e)}'
            }
