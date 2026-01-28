# 🔧 DEBUGGING Y TROUBLESHOOTING

Guía completa para resolver problemas comunes.

---

## 🚨 Errores Comunes

### 1. `ModuleNotFoundError: No module named 'streamlit'`

**Causa:** Dependencias no instaladas o entorno virtual no activado

**Solución:**
```bash
# Verificar que el entorno esté activado
# Deberías ver (venv) al inicio de la línea
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
python -c "import streamlit; print(streamlit.__version__)"
```

---

### 2. `ModuleNotFoundError: No module named 'openai'`

**Causa:** La librería openai no está instalada

**Solución:**
```bash
pip install openai==1.3.5
```

---

### 3. `Error: OPENAI_API_KEY environment variable is not set`

**Causa:** No hay archivo `.env` o la clave no está configurada

**Solución:**
```bash
# 1. Crear .env desde el ejemplo
copy .env.example .env

# 2. Editar .env y añadir tu clave
# Obtén la clave en: https://platform.openai.com/api-keys

# 3. Verificar que .env existe
type .env
```

**Contenido esperado de .env:**
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### 4. `AuthenticationError: Incorrect API key provided`

**Causa:** La clave API es inválida o está expirada

**Solución:**
1. Verifica la clave en `.env`
2. Genera una nueva clave en: https://platform.openai.com/api-keys
3. Reemplaza en `.env`
4. Reinicia la aplicación

---

### 5. `RateLimitError: Rate limit exceeded for requests`

**Causa:** Has hecho demasiadas solicitudes demasiado rápido

**Solución:**
```python
# Espera 1-2 minutos antes de intentar de nuevo
# O usa el tier de pago de OpenAI para aumentar límites
```

---

### 6. `streamlit.errors.StreamlitAPIException: Port 8501 is already in use`

**Causa:** Otro proceso está usando el puerto 8501

**Solución Opción A:** Usar otro puerto
```bash
streamlit run app.py --server.port 8502
```

**Solución Opción B:** Matar el proceso anterior
```bash
# En Windows
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# En Mac/Linux
lsof -i :8501
kill -9 <PID>
```

---

### 7. `ConnectionError: Failed to establish connection`

**Causa:** Sin conexión a internet o API no disponible

**Solución:**
1. Verifica tu conexión a internet
2. Comprueba que OpenAI API está disponible: https://status.openai.com
3. Espera e intenta de nuevo

---

## 🔍 Debugging

### Activar Modo Debug en Streamlit

```bash
streamlit run app.py --logger.level=debug
```

### Logs Detallados

```bash
# Ver todos los logs
streamlit run app.py --verbose
```

### Verificar Configuración

```bash
python validate_setup.py
```

---

## 🧪 Testing Manual

### Prueba 1: Verificar Importaciones

```bash
python -c "from services.ai_service import WritingAssistant; print('✅ Imports OK')"
```

### Prueba 2: Verificar .env

```bash
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('API Key:', os.getenv('OPENAI_API_KEY'))"
```

### Prueba 3: Verificar Conexión OpenAI

```bash
python example_usage.py
```

---

## 📊 Checklist de Debugging

- [ ] ¿Está activado el entorno virtual?
  ```bash
  # En Windows, deberías ver (venv) al inicio de la línea
  ```

- [ ] ¿Están instaladas las dependencias?
  ```bash
  pip list | findstr streamlit
  ```

- [ ] ¿Existe el archivo `.env`?
  ```bash
  type .env
  ```

- [ ] ¿Tiene `.env` la clave válida?
  ```bash
  # La clave debe empezar con "sk-" y tener 48+ caracteres
  ```

- [ ] ¿Es válida la sintaxis Python?
  ```bash
  python -m py_compile app.py
  ```

- [ ] ¿Hay conexión a internet?
  ```bash
  ping google.com
  ```

---

## 🛠️ Comandos Útiles

### Reinstalar Completamente

```bash
# Eliminar entorno
rmdir /s venv

# Crear nuevo
python -m venv venv

# Activar
venv\Scripts\activate

# Instalar
pip install -r requirements.txt
```

### Ver Versiones

```bash
python --version
pip --version
streamlit --version
openai --version
```

### Limpiar Cache de Python

```bash
# Windows
del /s __pycache__
for /r %d in (.pytest_cache) do @if exist "%d" rmdir /s /q "%d"

# Mac/Linux
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type d -name .pytest_cache -exec rm -rf {} +
```

---

## 🚀 Performance

### Si la app es lenta:

1. **Streamlit está recompilando?**
   - Espera a que termine
   - Cierra tabs innecesarias

2. **OpenAI API es lenta?**
   - Puede ser congestión del servidor
   - Intenta después de unos minutos

3. **Tu computadora es lenta?**
   - Cierra otras aplicaciones
   - Aumenta RAM disponible

---

## 🔐 Problemas de Seguridad

### ¿Expuse tu clave accidentalmente?

1. **Regenera tu clave inmediatamente:**
   - https://platform.openai.com/api-keys
   - Revoca la clave antigua
   - Crea una nueva

2. **Verifica tus repos:**
   ```bash
   git log --all -- '.env'
   ```

3. **Limpiar historial:**
   ```bash
   git filter-branch --tree-filter 'rm -f .env'
   ```

---

## 📞 Si Nada Funciona

1. **Ejecuta el validador:**
   ```bash
   python validate_setup.py
   ```

2. **Revisa los logs:**
   ```bash
   streamlit run app.py --logger.level=debug 2>&1 | tee debug.log
   ```

3. **Consulta la documentación:**
   - README.md
   - SETUP_GUIDE.md
   - API_REFERENCE.md

4. **Recursos externos:**
   - https://docs.streamlit.io
   - https://platform.openai.com/docs
   - https://github.com/openai/openai-python

---

## 📝 Reportar Problemas

Si encuentras un error, incluye:
1. Mensaje de error completo (con stack trace)
2. Versión de Python: `python --version`
3. Versión de Streamlit: `streamlit --version`
4. Sistema operativo (Windows/Mac/Linux)
5. Pasos para reproducir el error

---

**Última actualización:** Enero 2026  
**Mantener actualizado según nuevas versiones de dependencias**
