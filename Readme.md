# NAEX Web App

Aplicación web para gestión académica de la academia online NAEX, desarrollada en Python (Flask) y MongoDB Atlas.

## 🧩 Características

- Registro de clases por parte de tutores.
- Administración de estudiantes y profesores.
- Seguimiento del progreso de los estudiantes.
- Conexión con base de datos MongoDB en la nube (Atlas).
- Despliegue en la nube (Render.com u otra plataforma gratuita).

## 🚀 Tecnologías

- Python 3.x
- Flask
- MongoDB Atlas (pymongo)
- HTML + CSS (para la interfaz)
- Gunicorn (servidor de producción)
- Dotenv (manejo de variables de entorno)

## ⚙️ Instalación local

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/naex-web.git
cd naex-web
Crea un entorno virtual e instálalo:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
Crea un archivo .env con tu URI de MongoDB:

env
Copiar
Editar
MONGO_URI=mongodb+srv://usuario:clave@cluster.mongodb.net/naex?retryWrites=true&w=majority
Ejecuta la app:

bash
Copiar
Editar
python app.py
☁️ Despliegue en Render.com
Sube tu código a GitHub.

Crea una cuenta en Render.com.

Crea un nuevo Web Service y conecta tu repo.

Usa gunicorn como comando de ejecución:

nginx
Copiar
Editar
gunicorn app:app
Agrega la variable de entorno MONGO_URI en el dashboard de Render.

¡Deploy!

📄 Archivos importantes
app.py: archivo principal de Flask.

requirements.txt: dependencias.

Procfile: instrucción para ejecutar la app en producción.

.env: (no subir al repo) contiene credenciales seguras.

🙌 Contribuciones
Si quieres contribuir, ¡bienvenido! Puedes enviar PRs o sugerencias.

🛡️ Licencia
MIT © 2025 - NAEX