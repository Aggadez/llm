# ✍️ Asistente de Escritura Automática con IA

Una aplicación web potente que utiliza OpenAI para ayudarte a:
- **Corregir** gramática y ortografía
- **Mejorar** el estilo y tono de tus textos (Formal, Creativo, Casual)
- **Generar** contenido nuevo basado en ideas

---

## 🎯 Características

- ✅ Interfaz amigable con Streamlit
- ✅ Corrección automática de gramática
- ✅ Reescritura con diferentes tonos
- ✅ Generación de contenido creativo
- ✅ Simulación de almacenamiento en BD
- ✅ Manejo robusto de errores
- ✅ Code 100% tipado y PEP-8 compliant

---

## 💻 Requisitos Previos

- **Python 3.10 o superior**
- **pip** (gestor de paquetes de Python)
- Cuenta en [OpenAI](https://platform.openai.com) con acceso a API
- Una **Clave API de OpenAI** válida

---

## 🚀 Instalación Paso a Paso

### 1️⃣ Crear el Entorno Virtual

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python -m venv venv
```

Esto crea una carpeta `venv` que contendrá todas las dependencias aisladas del proyecto.

### 2️⃣ Activar el Entorno Virtual

#### En **Windows** (PowerShell o CMD):
```bash
venv\Scripts\activate
```

#### En **macOS/Linux** (Terminal/Bash):
```bash
source venv/bin/activate
```

**Nota:** Una vez activado, verás `(venv)` al inicio de tu terminal.

### 3️⃣ Instalar las Dependencias

Con el entorno virtual activado, ejecuta:

```bash
pip install -r requirements.txt
```

Esto instalará:
- `streamlit`: Framework para crear la interfaz web
- `openai`: Cliente de OpenAI
- `python-dotenv`: Para cargar variables de entorno

### 4️⃣ Configurar la Clave API

#### Opción A: Usar el archivo `.env` (Recomendado)

1. Copia el archivo `.env.example` y renómbralo a `.env`:

```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

2. Abre el archivo `.env` y reemplaza `sk-tu-clave-api-aqui` con tu clave real:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

3. Obtén tu clave API en: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

#### Opción B: Ingresar en la Interfaz

Cuando ejecutes la app, puedes ingresar la clave API directamente en el campo de la barra lateral.

### 5️⃣ Ejecutar la Aplicación

Una vez todo configurado, ejecuta:

```bash
streamlit run app.py
```

La aplicación se abrirá en tu navegador predeterminado en `http://localhost:8501`.

---

## 📚 Estructura del Proyecto

```
llm/
├── app.py                      # 🎨 Interfaz principal (Streamlit)
├── requirements.txt            # 📦 Dependencias del proyecto
├── .env.example               # 🔐 Plantilla de variables de entorno
├── .env                       # 🔐 Archivo con tu clave API (NO commitar)
├── README.md                  # 📖 Este archivo
├── LICENSE                    # ⚖️ Licencia del proyecto
│
├── services/
│   └── ai_service.py          # 🤖 Clase WritingAssistant
│
└── utils/
    └── storage_mock.py        # 💾 Simulación de almacenamiento en BD
```

---

## 🔧 Cómo Usar la Aplicación

### 1. **Corregir Gramática**
   - Selecciona "Corregir Gramática" en la barra lateral
   - Pega tu texto en el área de entrada
   - Haz clic en "🚀 Procesar"
   - Verás el texto corregido

### 2. **Mejorar Estilo**
   - Selecciona "Mejorar Estilo" en la barra lateral
   - Elige el tono: Formal, Creativo o Casual
   - Ingresa tu texto
   - Haz clic en "🚀 Procesar"

### 3. **Generar Contenido**
   - Selecciona "Generar Contenido"
   - Describe el tema o idea
   - Haz clic en "🚀 Procesar"
   - Recibe un borrador generado

### 4. **Guardar Borrador**
   - Después de procesar, haz clic en "💾 Guardar Borrador"
   - Verás un mensaje de confirmación en la consola
   - El borrador se "guarda" en la BD simulada

---

## 🐛 Solución de Problemas

### Error: `ModuleNotFoundError: No module named 'streamlit'`
**Solución:** Asegúrate de haber activado el entorno virtual y ejecutado `pip install -r requirements.txt`.

### Error: `Authentication error with API`
**Solución:** Verifica que tu clave API sea correcta en el archivo `.env` o en el campo de entrada.

### Error: `Rate limit exceeded`
**Solución:** Has hecho demasiadas solicitudes. Espera un minuto e intenta de nuevo.

### La app no se abre en el navegador
**Solución:** Abre manualmente `http://localhost:8501` en tu navegador.

---

## 📝 Variables de Entorno

El archivo `.env` contiene:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**⚠️ Importante:** Nunca compartas tu `.env` públicamente ni lo hagas commit en Git.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|----------|---------|----------|
| Python | 3.10+ | Lenguaje base |
| Streamlit | 1.28.1 | Interfaz web |
| OpenAI | 1.3.5 | API de IA |
| python-dotenv | 1.0.0 | Gestión de variables |

---

## 📖 Ejemplos de Uso

### Ejemplo 1: Corrección de Gramática
**Entrada:**
```
Hola, me gustaria saber como puedo mejorar mi escritura. Mi gramatica no es muy buena.
```

**Salida:**
```
Hola, me gustaría saber cómo puedo mejorar mi escritura. Mi gramática no es muy buena.
```

### Ejemplo 2: Mejorar a Tono Formal
**Entrada:**
```
Oye, quería preguntarte si podemos juntarnos mañana para hablar del proyecto.
```

**Salida:**
```
Le escribo para solicitar si sería posible sostener una reunión mañana a fin de discutir los detalles del proyecto.
```

### Ejemplo 3: Generar Contenido
**Entrada:**
```
Escribir un correo para disculparme con un cliente por un retraso en la entrega
```

**Salida:**
```
Estimado [Nombre del cliente],

Le escribo para expresar mis más sinceras disculpas por el retraso en la entrega de [producto/servicio]. 
Entiendo que esto puede haber generado inconvenientes...
```

---

## 🔒 Seguridad

- Nunca compartas tu clave API
- Usa `.env` para guardar credenciales sensibles
- El archivo `.env` está en `.gitignore` (no se sube a repos públicos)

---

## 📞 Soporte

Si encuentras problemas:
1. Verifica los requisitos previos
2. Revisa la sección de "Solución de Problemas"
3. Asegúrate de tener internet activo
4. Comprueba el saldo de tu cuenta OpenAI

---

## 📄 Licencia

Este proyecto está bajo licencia [especificar licencia]. Ver archivo `LICENSE` para más detalles.

---

## 🎓 Autor

Desarrollado como un proyecto de prototipado rápido de IA.

**Última actualización:** Enero 2026

---

¡Disfruta mejorando tu escritura con IA! ✨
