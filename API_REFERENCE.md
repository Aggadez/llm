# 📋 REFERENCIA RÁPIDA - API WritingAssistant

## Inicialización

```python
from services.ai_service import WritingAssistant

# Crear instancia
assistant = WritingAssistant(api_key="tu-clave-aqui")
```

---

## Métodos Disponibles

### 1. `fix_grammar(text: str) -> dict`

**Corrige gramática y ortografía**

```python
result = assistant.fix_grammar("Hola, me gustaria aprender Python")

# Retorna:
# {
#     'success': True,
#     'corrected_text': 'Hola, me gustaría aprender Python',
#     'error': None
# }
```

**Parámetros:**
- `text` (str): Texto a corregir

**Retorna:**
- `dict` con claves: `success`, `corrected_text`, `error`

---

### 2. `improve_style(text: str, tone: str) -> dict`

**Mejora el estilo del texto según el tono**

```python
result = assistant.improve_style(
    "Hola, quiero hablar contigo",
    "Formal"
)

# Retorna:
# {
#     'success': True,
#     'improved_text': 'Deseo comunicarme con usted',
#     'error': None
# }
```

**Parámetros:**
- `text` (str): Texto a mejorar
- `tone` (str): Uno de ["Formal", "Creativo", "Casual"]

**Retorna:**
- `dict` con claves: `success`, `improved_text`, `error`

---

### 3. `generate_content(topic: str) -> dict`

**Genera contenido nuevo basado en un tema**

```python
result = assistant.generate_content(
    "Escribir un correo de disculpa al cliente"
)

# Retorna:
# {
#     'success': True,
#     'generated_text': 'Estimado cliente,\n\nQuiero expresar mis...',
#     'error': None
# }
```

**Parámetros:**
- `topic` (str): Tema o idea para generar contenido

**Retorna:**
- `dict` con claves: `success`, `generated_text`, `error`

---

## Manejo de Errores

Todas las funciones devuelven un diccionario con `success` boolean:

```python
result = assistant.fix_grammar("Texto")

if result['success']:
    print(result['corrected_text'])
else:
    print(f"Error: {result['error']}")
```

### Tipos de Errores Capturados:
- `openai.error.APIError` - Error de la API
- `openai.error.AuthenticationError` - Clave API inválida
- `Exception` - Errores generales

---

## Función de Almacenamiento Simulado

```python
from utils.storage_mock import save_draft_to_db

# Guardar un borrador
success = save_draft_to_db(
    user_id="usuario123",
    text="Mi contenido aquí"
)

# Retorna True si fue exitoso
# Imprime en consola: "Simulando conexión a DB..."
```

---

## Parámetros Internos

### Temperaturas de Generación
- Corrección: 0.3 (conservador)
- Estilo: 0.7 (creativo)
- Generación: 0.8 (muy creativo)

### Límites
- Max tokens: 1000-1500
- Modelo: gpt-3.5-turbo (configurable)
- Timeout: Sin límite establecido

---

## Ejemplo Completo

```python
import os
from dotenv import load_dotenv
from services.ai_service import WritingAssistant

# Cargar config
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Crear asistente
assistant = WritingAssistant(api_key)

# Usar
texto_original = "Hola, me gusta mucho escribir"
resultado = assistant.improve_style(texto_original, "Formal")

if resultado['success']:
    print("✅ Éxito:")
    print(resultado['improved_text'])
else:
    print("❌ Error:")
    print(resultado['error'])
```

---

## Variables de Entorno

```env
# .env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Status de Implementación

| Método | Estado | Tests |
|--------|--------|-------|
| fix_grammar() | ✅ Activo | ✅ |
| improve_style() | ✅ Activo | ✅ |
| generate_content() | ✅ Activo | ✅ |
| save_draft_to_db() | ✅ Activo | ✅ |

---

## Limitaciones Conocidas

1. Requiere conexión a Internet
2. Depende de disponibilidad de OpenAI API
3. Costo por token usado
4. Rate limits según tier de OpenAI
5. No mantiene historial (stateless)

---

## Para Más Información

- `README.md` - Documentación completa
- `example_usage.py` - Ejemplos de código
- `app.py` - Implementación en Streamlit
