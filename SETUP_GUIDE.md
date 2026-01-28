# GUÍA DE CONFIGURACIÓN: ASISTENTE DE ESCRITURA IA

## 📋 Resumen Rápido

Este documento proporciona una guía rápida de configuración para el Asistente de Escritura Automática.

---

## 🚀 Guía de Instalación Rápida (5 minutos)

### Paso 1: Crear el entorno virtual
```bash
python -m venv venv
```

### Paso 2: Activar el entorno
**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Configurar la API Key
```bash
copy .env.example .env
# Edita .env y añade tu clave de OpenAI
```

### Paso 5: Validar la instalación
```bash
python validate_setup.py
```

### Paso 6: Ejecutar la aplicación
```bash
streamlit run app.py
```

---

## 📁 Estructura de Carpetas

```
llm/
├── app.py                          # Interfaz principal Streamlit
├── example_usage.py                # Ejemplos de uso programático
├── validate_setup.py               # Script de validación
├── requirements.txt                # Dependencias
├── .env.example                    # Plantilla de .env
├── .env                            # (NO COMMITAR) Tu clave API
├── .gitignore                      # Archivos ignorados por Git
├── SETUP_GUIDE.md                  # Este archivo
├── README.md                       # Documentación completa
├── LICENSE                         # Licencia del proyecto
│
├── services/
│   ├── __init__.py
│   └── ai_service.py               # Clase WritingAssistant
│
├── utils/
│   ├── __init__.py
│   └── storage_mock.py             # Simulación de BD
│
└── .streamlit/
    └── config.toml                 # Configuración de Streamlit
```

---

## 🔧 Archivos Importantes

### `requirements.txt`
Contiene todas las dependencias necesarias:
- **streamlit**: Interfaz web
- **openai**: Cliente de OpenAI
- **python-dotenv**: Manejo de variables de entorno

### `.env.example` y `.env`
- `.env.example`: Plantilla (SE PUEDE COMMITAR)
- `.env`: Tu configuración actual (NO COMMITAR - está en .gitignore)

Contenido esperado:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### `services/ai_service.py`
Clase `WritingAssistant` con métodos:
- `fix_grammar(text)`: Corrige gramática
- `improve_style(text, tone)`: Mejora estilo
- `generate_content(topic)`: Genera contenido

### `utils/storage_mock.py`
Función `save_draft_to_db(user_id, text)` que simula guardado en BD.

### `app.py`
Aplicación principal con:
- Interfaz de usuario en Streamlit
- Barra lateral para configuración
- Área de procesamiento
- Botones de acción

---

## 🐛 Solución Rápida de Problemas

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError` | Activa venv: `venv\Scripts\activate` |
| `No module named 'streamlit'` | Instala: `pip install -r requirements.txt` |
| `Authentication error` | Verifica tu clave en `.env` |
| `Rate limit exceeded` | Espera unos minutos y reintenta |
| Puerto 8501 en uso | Streamlit usará otro puerto automáticamente |

---

## ✨ Características Principales

### 1. Corrección de Gramática
- Entrada: Texto con errores
- Salida: Texto corregido
- Usa: `gpt-3.5-turbo` con temperatura baja (0.3)

### 2. Mejora de Estilo
- Selecciona tono: Formal, Creativo, Casual
- Reescribe manteniendo contenido
- Temperatura media (0.7)

### 3. Generación de Contenido
- Tema: Describa qué quiere generar
- Genera borradores completos
- Temperatura alta (0.8)

### 4. Almacenamiento Simulado
- Simula guardado en BD sin dependencias
- Imprime en consola
- Listo para integración real

---

## 🔐 Seguridad

1. **NUNCA** publiques tu `.env`
2. El `.gitignore` ya ignora `.env`
3. Solo `.env.example` debe estar en repos públicos
4. Regenera tu API Key si la expones accidentalmente

---

## 📊 Dependencias del Proyecto

```
streamlit==1.28.1          # Interfaz web interactiva
openai==1.3.5              # API de OpenAI
python-dotenv==1.0.0       # Gestión de variables de entorno
```

**Total de dependencias principales:** 3
**Tamaño aproximado:** ~50 MB con dependencias

---

## 💡 Ejemplos de Uso

### Uso desde la interfaz Streamlit
1. Abre `streamlit run app.py`
2. Selecciona operación en la barra lateral
3. Ingresa texto o tema
4. Haz clic en "Procesar"
5. Opcionalmente, guarda el resultado

### Uso programático
```bash
python example_usage.py
```

Esto ejecuta 4 ejemplos de uso de `WritingAssistant`.

### Validación de instalación
```bash
python validate_setup.py
```

Verifica que todo esté correctamente instalado.

---

## 🎯 Próximos Pasos

1. ✅ Instala el proyecto siguiendo los pasos arriba
2. ✅ Obtén tu API Key en https://platform.openai.com/api-keys
3. ✅ Configura tu `.env`
4. ✅ Ejecuta `validate_setup.py`
5. ✅ Inicia la app: `streamlit run app.py`
6. ✅ Prueba cada funcionalidad

---

## 📞 Recursos

- **OpenAI API Docs:** https://platform.openai.com/docs
- **Streamlit Docs:** https://docs.streamlit.io
- **Python Docs:** https://docs.python.org/3.10

---

## ✍️ Notas Finales

- El código es 100% PEP-8 compliant
- Incluye type hints en todas las funciones
- Manejo robusto de errores
- Estructura modular y escalable
- Listo para extensiones futuras

---

**Versión:** 1.0  
**Última actualización:** Enero 2026  
**Estado:** ✅ Producción
