# ⚡ INICIO RÁPIDO (Quick Start)

¿Impaciencia? Aquí está el resumen de **2 minutos** para empezar.

## 1️⃣ Clone / Descargar el Proyecto
```bash
# Ya lo tienes? Salta al paso 2
```

## 2️⃣ Crear Entorno Virtual
```bash
python -m venv venv
```

## 3️⃣ Activar Entorno (Windows)
```bash
venv\Scripts\activate
```
*(En Mac/Linux: `source venv/bin/activate`)*

## 4️⃣ Instalar Todo
```bash
pip install -r requirements.txt
```

## 5️⃣ Copiar Configuración
```bash
copy .env.example .env
```

## 6️⃣ Editar `.env`
Abre el archivo `.env` que acabas de crear y reemplaza:
```
sk-tu-clave-api-aqui
```
Por tu clave real de: https://platform.openai.com/api-keys

## 7️⃣ ¡Listo! Ejecutar
```bash
streamlit run app.py
```

Se abrirá en tu navegador en `http://localhost:8501`

---

## 🎯 Ya está funcionando!

### Prueba esto:
1. Escribe algo en el recuadro (ej: "Hola, me gusta escribir")
2. Haz clic en "🚀 Procesar"
3. ¡Verás la magia de la IA!

---

## ❌ Problema?

### Error: `ModuleNotFoundError`
```bash
# Asegúrate de activar el entorno:
venv\Scripts\activate

# E instalar dependencias:
pip install -r requirements.txt
```

### Error: `OPENAI_API_KEY not found`
```bash
# Verifica que .env existe y tiene tu clave:
cat .env
```

### Error: `Port 8501 already in use`
Streamlit usará otro puerto automáticamente. No es problema.

---

## 📖 Documentación Completa

Para más detalles:
- **README.md** - Documentación completa
- **SETUP_GUIDE.md** - Guía detallada de instalación
- **PROJECT_STATS.md** - Estadísticas del proyecto

---

## ✨ ¡Disfruta!

Eres genial por llegar hasta aquí. Ahora crea contenido increíble con IA.

**Preguntas frecuentes?** Revisa el README.md
