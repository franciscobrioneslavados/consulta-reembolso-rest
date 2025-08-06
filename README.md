# Consulta Reembolso REST API

API REST en Python con Flask para manejar boletas de reembolso, conectada a PostgreSQL.

---

## 🛠️ Tecnologías

- Python 3.11
- Flask
- SQLAlchemy
- PostgreSQL
- dotenv (para variables de entorno)
- psycopg2-binary

---

## ⚙️ Configuración

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo
```

2. Crea un entorno virtual e instala dependencias:

```bash
python -m venv venv
source venv/bin/activate  # Linux / MacOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

3. Crea un archivo .env con las variables de conexión a la base de datos:
```conf
DATABASE_USER=avnadmin
DATABASE_PASS=tu_password
DATABASE_HOST=tu_host
DATABASE_PORT=puerto
DATABASE_NAME=tu_base
DATABASE_SSLMODE=require
FLASK_ENV=development
```

4. Modifica el archivo config.py para construir la URI desde estas variables (ya incluido).

🚀 Cómo ejecutar

```bash
python main.py
# El servidor correrá en http://localhost:8080
```

📚 Endpoints disponibles
1. Crear una boleta
* URL: /boletas
* Método: POST
* Body (JSON):
```json
{
  "id_boleta": 1234,
  "key_boleta": "abc123",
  "procesa_isapre": true,
  "response_isapre": {"status": "ok"},
  "procesa_seguro": false,
  "response_seguro": null,
  "half": 50.5
}
````
* Respuesta: Código 201
```json
{
  "message": "Boleta creada",
  "id": 1
}
```

2. Obtener todas las boletas
* URL: /boletas
* Método: GET
* Respuesta: Código 200

```json
[
  {
    "id_": 1,
    "id_boleta": 1234,
    "key_boleta": "abc123",
    "procesa_isapre": true,
    "response_isapre": {"status": "ok"},
    "procesa_seguro": false,
    "response_seguro": null,
    "half": 50.5
  },
  ...
]
```

3. Obtener una boleta por ID
* URL: /boletas/<id_>
* Método: GET
* Respuesta: Código 200
```json
{
  "id_": 1,
  "id_boleta": 1234,
  "key_boleta": "abc123",
  "procesa_isapre": true,
  "response_isapre": {"status": "ok"},
  "procesa_seguro": false,
  "response_seguro": null,
  "half": 50.5
}
```
* Si no existe, devuelve 404:

```json
{
  "error": "Boleta no encontrada"
}
````

4. Actualizar una boleta
* URL: /boletas/<id_>
* Método: PUT
* Body (JSON): Campos a actualizar (puede ser parcial)

```json
{
  "procesa_isapre": false,
  "half": 60.0
}
```
* Respuesta: Código 200

```json
{
  "message": "Boleta actualizada"
}
```
* Si no existe, devuelve 404.


5. Eliminar una boleta
* URL: /boletas/<id_>
* Método: DELETE
* Respuesta: Código 200

```json
{
  "message": "Boleta eliminada"
}
```
* Si no existe, devuelve 404.

📝 Notas
Asegúrate que la base de datos está creada y accesible.

La tabla boletas será creada automáticamente al iniciar el servidor.

Variables sensibles como contraseñas no deben subirse a repositorios públicos.

🐳 Docker
El proyecto incluye un Dockerfile para construir la imagen y desplegar fácilmente.

```bash
docker build -t consulta-reembolso .
docker run -p 5000:5000 consulta-reembolso
```