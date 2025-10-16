# 🏡 HomeBase API - Gestor de Inmuebles

HomeBase API es un gestor de inmuebles desarrollado con Django y Django REST Framework. Permite administrar propiedades y sus respectivos propietarios a través de una API RESTful, siguiendo los principios de diseño de software y buenas prácticas de desarrollo.

---

## ✨ Características (Features)

-   **Gestión Completa de Propietarios**: CRUD (Crear, Leer, Actualizar, Eliminar) para la entidad `Propietario`.
-   **Gestión Completa de Propiedades**: CRUD (Crear, Leer, Actualizar, Eliminar) para la entidad `Propiedad`.
-   **Relación Propietario-Propiedad**: Cada propiedad está vinculada a un propietario.
-   **Búsqueda Avanzada**: Endpoint de búsqueda para filtrar propiedades por `dirección` o `tipo`.
-   **Respuestas Personalizadas**: El endpoint de propiedades incluye el nombre del propietario asociado para mayor claridad, no solo su ID.

---

## 🛠️ Tecnologías Utilizadas

-   **Backend**: Python, Django
-   **API**: Django REST Framework
-   **Base de Datos**: SQLite3 (para desarrollo)

---

## 🚀 Instalación y Puesta en Marcha

Sigue estos pasos para levantar el entorno de desarrollo local.

**1. Clonar el repositorio:**
```shell
git clone <URL-DE-TU-REPOSITORIO>
cd homebase_api
```

**2. Crear y activar un entorno virtual:**
```shell
# Crear el entorno
python -m venv venv

# Activar en Windows
.\venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
```

**3. Instalar dependencias:**
El archivo `requirements.txt` contiene todas las librerías necesarias.
```shell
pip install -r requirements.txt
```

**4. Aplicar las migraciones:**
Para crear las tablas en la base de datos.
```shell
python manage.py makemigrations
python manage.py migrate
```

**5. Iniciar el servidor de desarrollo:**
```shell
python manage.py runserver
```
La API estará disponible en `http://127.0.0.1:8000/`.

---

## 🔗 Documentación de Endpoints

A continuación se detallan los endpoints disponibles en la API.

### Propietarios (`/propietarios/`)

| Método      | Endpoint                  | Descripción                      |
|-------------|---------------------------|----------------------------------|
| `GET`       | `/propietarios/`          | Lista todos los propietarios.    |
| `POST`      | `/propietarios/`          | Crea un nuevo propietario.       |
| `GET`       | `/propietarios/{id}/`     | Obtiene un propietario por su ID.|
| `PUT`/`PATCH` | `/propietarios/{id}/`     | Actualiza un propietario.        |
| `DELETE`    | `/propietarios/{id}/`     | Elimina un propietario.          |

### Propiedades (`/propiedades/`)

| Método      | Endpoint                  | Descripción                       |
|-------------|---------------------------|-----------------------------------|
| `GET`       | `/propiedades/`           | Lista todas las propiedades.      |
| `POST`      | `/propiedades/`           | Crea una nueva propiedad.         |
| `GET`       | `/propiedades/{id}/`      | Obtiene una propiedad por su ID.  |
| `PUT`/`PATCH` | `/propiedades/{id}/`      | Actualiza una propiedad.          |
| `DELETE`    | `/propiedades/{id}/`      | Elimina una propiedad.            |

#### Búsqueda de Propiedades

-   **Endpoint**: `GET /propiedades/?search={termino}`
-   **Descripción**: Filtra la lista de propiedades donde el `{termino}` de búsqueda coincida en los campos `direccion` o `tipo`.
-   **Ejemplo**: `http://127.0.0.1:8000/propiedades/?search=Avenida`