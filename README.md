# Sistema de Gestión de Inmobiliarias

Este proyecto es un sistema de gestión para inmobiliarias, desarrollado con Django y Django REST Framework. Permite manejar agentes, inmuebles, prospectos interesados y transacciones realizadas.

## Características

- Registro y gestión de agentes inmobiliarios.
- Administración de inmuebles disponibles.
- Seguimiento de prospectos interesados en los inmuebles.
- Registro de transacciones cerradas entre prospectos y agentes.
- APIs RESTful generadas con Django REST Framework.
- API personalizada para obtener transacciones recientes.

## Requerimientos

- Python 3.8 o superior
- Django 4.2 o superior
- Django REST Framework 3.14 o superior
- Virtualenv (opcional pero recomendado)

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio

```bash
git clone https://github.com/iuriiernich/Diplomado_Modulo_5_Django.git
cd inmobiliaria
```

### 2. Crear y activar un entorno virtual

```bash
virtualenv env
.\env\Scripts\activate
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Crear un superusuario (opcional)
```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

### 7. Acceder al sistema
- Panel de administración: http://127.0.0.1:8000/admin/
- API base: http://127.0.0.1:8000/api/

## Endpoints Principales

### Rutas Automáticas
- Agentes: `/api/agentes/`
- Inmuebles: `/api/inmuebles/`
- Prospectos: `/api/prospectos/`

### Ruta Personalizada
- Transacciones Recientes: `/api/transacciones-recientes/`
