# 🐋 Mini Chat Local con Docker Model Runner

Un proyecto súper simple para ejecutar un modelo de IA localmente usando Docker Model Runner y una interfaz web minimalista.

## 🚀 Inicio Rápido

### Paso 0: Verifica que tienes Docker instalado

**Docker Model Runner** no se instala por separado. Viene incluido dentro de las imágenes Docker del namespace `ai/`.

Solo necesitas tener **Docker Desktop** (o Docker Engine) instalado en tu computadora.

**¿No tienes Docker?** Descárgalo desde: https://www.docker.com/products/docker-desktop

---

### Paso 1: Descarga y ejecuta Ollama con Docker

Abre tu terminal y ejecuta este comando (puedes copiar-pegar sin pensar):

```bash
docker run -d --rm -p 11434:11434 --name ollama-server ollama/ollama
```

**¿Qué hace esto?**
- **Descarga automáticamente** Ollama (servidor de modelos de IA)
- Levanta un servidor local en el puerto 11434
- Crea una API compatible con OpenAI

**💡 Tip:** 
- La primera vez puede tardar unos minutos (descarga la imagen)
- El contenedor corre en segundo plano (flag `-d`)

### Paso 1.5: Descarga un modelo ligero

Ahora descarga un modelo pequeño (esto puede tardar unos minutos la primera vez):

```bash
docker exec ollama-server ollama pull phi3:mini
```

**¿Qué modelo es?** `phi3:mini` es un modelo pequeño y rápido de Microsoft (~3.8GB), perfecto para empezar.

---

### Paso 2: Instala las dependencias de Python

En otra terminal, navega a esta carpeta y ejecuta:

```bash
pip install -r requirements.txt
```

O instala manualmente:

```bash
pip install openai streamlit python-dotenv
```

---

### Paso 3: Configura las variables de entorno

Crea un archivo llamado `.env` en esta carpeta con el siguiente contenido:

```
OPENAI_API_KEY=docker
OPENAI_BASE_URL=http://localhost:11434/v1
```

**💡 Tip:** Puedes crear el archivo manualmente o copiar estos valores. No necesitas cambiar nada, pero si quieres usar otro puerto o clave, edítalo aquí.

---

### Paso 4: Ejecuta tu interfaz

```bash
streamlit run app.py
```

Se abrirá automáticamente en tu navegador (normalmente en `http://localhost:8501`).

---

## 💻 Ejecutar desde Visual Studio Code

Si quieres ejecutar el proyecto desde VS Code, es muy simple:

1. **Abre el proyecto en VS Code**: `File` → `Open Folder` → Selecciona la carpeta `app`

2. **Abre la terminal integrada**: Presiona `` Ctrl+` `` (Ctrl + backtick) o ve a `Terminal` → `New Terminal`

3. **Sigue los pasos del README**: Ejecuta los mismos comandos que están arriba, pero desde la terminal de VS Code:
   - Instala dependencias: `pip install -r requirements.txt`
   - Crea el archivo `.env` (haz clic derecho → New File → `.env`)
   - Inicia Docker: `docker run -d --rm -p 11434:11434 --name ollama-server ollama/ollama`
   - Descarga el modelo: `docker exec ollama-server ollama pull phi3:mini`
   - Ejecuta Streamlit: `streamlit run app.py`

¡Eso es todo! Los comandos son exactamente los mismos, solo los ejecutas desde la terminal de VS Code.

---

## 🎯 Cómo usar

1. **Asegúrate de que Docker está corriendo** (Paso 1)
2. **Abre la interfaz** (Paso 4)
3. **Escribe una pregunta** en el cuadro de texto
4. **Haz clic en "Enviar"**
5. **¡Disfruta de las respuestas!** 🎉

---

## 📁 Estructura del Proyecto

```
.
├── README.md          # Estas instrucciones
├── app.py            # Interfaz Streamlit
├── .env              # Variables de entorno
├── requirements.txt  # Dependencias Python
└── .gitignore       # Archivos a ignorar en Git
```

---

## 🔧 Solución de Problemas

**"No puedo conectar al servidor"**
- Verifica que Docker está corriendo (Paso 1)
- Asegúrate de que el puerto 11434 está libre
- Revisa que `.env` tiene la URL correcta
- Verifica que el contenedor está corriendo: `docker ps`

**"El modelo no responde"**
- Espera unos segundos después de iniciar Docker (el modelo necesita cargarse)
- Verifica en la terminal de Docker que no hay errores

**"Streamlit no se abre"**
- Ejecuta `streamlit run app.py` de nuevo
- Abre manualmente `http://localhost:8501` en tu navegador

---

## 💡 Próximos Pasos

- Prueba otros modelos del namespace `ai/` cambiando el comando Docker
- Personaliza la interfaz en `app.py`
- Agrega historial de conversación
- Experimenta con diferentes modelos según tus necesidades

---

**¡Disfruta creando con IA local! 🚀**

