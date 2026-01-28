# 📦 GUÍA DE DISTRIBUCIÓN Y DEPLOY

Instrucciones para distribuir y desplegar el proyecto Asistente de Escritura IA.

---

## 🎁 Preparación para Distribución

### 1. Verificar que TODO esté listo

```bash
# Ejecutar validación
python validate_setup.py

# Verificar que no hay errores
python -m py_compile app.py
python -m py_compile services/ai_service.py
python -m py_compile utils/storage_mock.py
```

### 2. Limpiar archivos no necesarios

```bash
# Windows PowerShell
Get-ChildItem -Recurse -Include "__pycache__" -Directory | Remove-Item -Recurse -Force
Get-ChildItem -Recurse -Include "*.pyc" | Remove-Item -Force
```

### 3. Verificar .gitignore

Asegurar que está ignorando:
- `venv/` o `env/`
- `.env` (solo mantener `.env.example`)
- `__pycache__/`
- `.pytest_cache/`
- `.idea/` y `.vscode/`

---

## 🚀 Opciones de Deploy

### Opción 1: GitHub (Recomendado)

```bash
# 1. Inicializar repo (si no existe)
git init

# 2. Agregar todos los archivos
git add .

# 3. Hacer commit
git commit -m "Asistente de Escritura Automática con IA v1.0"

# 4. Agregar remote
git remote add origin https://github.com/tu-usuario/asistente-ia.git

# 5. Push
git push -u origin main
```

**Verificar que `.env` NO está incluido (debe estar en .gitignore)**

### Opción 2: Streamlit Cloud (Deploy directo)

1. Sube el repo a GitHub
2. Ve a https://streamlit.io/cloud
3. Conecta tu cuenta GitHub
4. Selecciona el repositorio
5. Configura la rama (main)
6. Añade secrets (OPENAI_API_KEY) en Streamlit Cloud

### Opción 3: Docker

Crear `Dockerfile`:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

Ejecutar:
```bash
docker build -t asistente-ia .
docker run -p 8501:8501 -e OPENAI_API_KEY="tu-clave" asistente-ia
```

### Opción 4: Heroku

```bash
# 1. Instalar Heroku CLI
# 2. Login
heroku login

# 3. Crear app
heroku create nombre-app

# 4. Agregar env var
heroku config:set OPENAI_API_KEY="tu-clave"

# 5. Deploy
git push heroku main
```

---

## 📋 Checklist Pre-Deploy

- [ ] Todos los archivos Python compilan sin errores
- [ ] `validate_setup.py` pasa sin problemas
- [ ] `.env` NO está en el repositorio
- [ ] `.env.example` SÍ está en el repositorio
- [ ] `.gitignore` está configurado correctamente
- [ ] `requirements.txt` está actualizado
- [ ] Documentación está completa
- [ ] Código tiene Type Hints 100%
- [ ] Todos los Docstrings están en español
- [ ] README.md tiene instrucciones claras
- [ ] LICENSE está presente
- [ ] No hay credenciales hardcodeadas
- [ ] API key se toma de variables de entorno
- [ ] Ejemplos de uso funcionan correctamente

---

## 📊 Distribución de Archivos

### Usuarios Nueva (primera vez)

Estructura de carpetas que recibirán:

```
asistente-ia/
├── app.py
├── requirements.txt
├── .env.example                ← DEBEN copiar a .env
├── README.md                   ← LEE PRIMERO
├── QUICKSTART.md               ← SIGUE ESTO
├── INDEX.md
├── services/
│   ├── __init__.py
│   └── ai_service.py
├── utils/
│   ├── __init__.py
│   └── storage_mock.py
└── .streamlit/
    └── config.toml
```

### Archivos NO incluir

- `venv/` - Entorno virtual (cada usuario crea el suyo)
- `__pycache__/` - Cache de Python
- `.env` - Variables sensibles
- `.git/` - Historia de Git (opcional)
- `.idea/` - Configuración IDE

---

## 📖 Instrucciones para Usuario Final

### Paso 1: Descarga

Descargar el proyecto desde GitHub:
```bash
git clone https://github.com/usuario/asistente-ia.git
cd asistente-ia
```

O descargar ZIP desde GitHub y descomprimir.

### Paso 2: Lee QUICKSTART.md

El archivo `QUICKSTART.md` tiene todo lo necesario en 2 minutos.

### Paso 3: Instalación

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
pip install -r requirements.txt
```

### Paso 4: Configuración

```bash
copy .env.example .env
# Editar .env y añadir tu clave de OpenAI
```

### Paso 5: Ejecutar

```bash
streamlit run app.py
```

---

## 🎯 Estrategia de Versionamiento

### Versiones

- **v1.0** - Release inicial
- **v1.1** - Bugfixes menores
- **v2.0** - Nuevas características

### Versionamiento Semántico

- `MAJOR.MINOR.PATCH`
  - MAJOR: Cambios incompatibles
  - MINOR: Nuevas características
  - PATCH: Bugfixes

### Cómo actualizar versión

1. Actualizar en `PROJECT_STATS.md`
2. Crear Git tag: `git tag v1.0`
3. Push: `git push --tags`

---

## 🐛 Monitoreo Post-Deploy

### Logs en Streamlit Cloud

Ir a: https://share.streamlit.io/ → Seleccionar app → Ver logs

### Logs en Docker

```bash
docker logs nombre-contenedor
```

### Logs en Heroku

```bash
heroku logs --tail
```

---

## 📊 Análisis de Uso

### Obtener datos de:
1. Streamlit Cloud Analytics
2. Google Analytics (opcional)
3. Custom logging (opcional)

---

## 🔐 Seguridad en Deploy

### NUNCA:
- Commitar `.env` con claves reales
- Exponer `OPENAI_API_KEY` en logs
- Usar claves en código (hardcoding)

### SIEMPRE:
- Usar variables de entorno
- Mantener `.env.example` sin claves
- Regenerar claves si se exponen
- Monitorear uso de API

---

## 💰 Costos Estimados

### OpenAI API (pay-as-you-go)
- ~$0.002 por 1K tokens GPT-3.5
- ~$0.03 por 1K tokens GPT-4
- Usuario típico: $1-5/mes

### Deploy (Streamlit Cloud)
- Gratuito hasta 3 apps
- $5/mes por app adicional
- $100/mes para uso empresarial

---

## 📞 Soporte

### Para usuarios finales:
1. Revisar DEBUGGING.md
2. Ejecutar validate_setup.py
3. Leer README.md

### Para desarrolladores:
1. Fork el repositorio
2. Crear rama para features
3. Hacer pull requests
4. Seguir convenciones de código

---

## 📈 Roadmap Futuro

### v2.0 (Próxima versión)
- [ ] Base de datos real (SQLite/PostgreSQL)
- [ ] Autenticación de usuarios
- [ ] Historial de cambios
- [ ] Soporte para múltiples idiomas
- [ ] API REST
- [ ] Tests unitarios
- [ ] CI/CD pipeline
- [ ] Dashboard de análisis

---

## 🎓 Documentos de Referencia

- [Streamlit Deployment](https://docs.streamlit.io/deploy)
- [Docker Documentation](https://docs.docker.com)
- [Heroku Deployment](https://devcenter.heroku.com)
- [GitHub Pages](https://pages.github.com)

---

**Versión:** 1.0  
**Última actualización:** Enero 2026  
**Mantener actualizado según cambios de versiones**
