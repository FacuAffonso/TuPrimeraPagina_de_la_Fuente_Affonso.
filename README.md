# TuPrimeraPagina+de la Fuente Affonso

Proyecto Django simple estilo blog, desarrollado siguiendo el patrón **MVT (Model - View - Template)**.  
Cumple con los requisitos solicitados:
- Herencia de plantillas HTML
- 3 clases en `models.py`
- Formularios para insertar datos en cada modelo
- Formulario de búsqueda en la base de datos
- Archivo README con instrucciones de uso
- Proyecto listo para ser subido a GitHub

---

## 🚀 Estructura general del proyecto

```
TuPrimeraPagina_de_la_Fuente_Affonso/
├── manage.py
├── requirements.txt
├── README.md
├── tuprimerapagina/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
└── blog/
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── blog/
            ├── base.html
            ├── home.html
            ├── author_form.html
            ├── category_form.html
            ├── post_form.html
            ├── post_list.html
            └── search.html
```

---

## 🧱 Tecnologías utilizadas

- Python 3.10+
- Django 4.2+
- SQLite (por defecto)
- HTML + CSS (con [Water.css](https://watercss.kognise.dev) para estilo básico)

---

## ⚙️ Instalación y configuración local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/<tu_usuario>/TuPrimeraPagina_de_la_Fuente_Affonso.git
   cd TuPrimeraPagina_de_la_Fuente_Affonso
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor local:**
   ```bash
   python manage.py runserver
   ```

---

## 🧩 Orden sugerido para probar las funcionalidades

1. Ingresar a la página de inicio:  
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

2. Crear un **Autor**:  
   [http://127.0.0.1:8000/authors/new/](http://127.0.0.1:8000/authors/new/)

3. Crear una **Categoría**:  
   [http://127.0.0.1:8000/categories/new/](http://127.0.0.1:8000/categories/new/)

4. Crear un **Post** (seleccionando Autor y Categoría):  
   [http://127.0.0.1:8000/posts/new/](http://127.0.0.1:8000/posts/new/)

5. Ver la **lista de Posts**:  
   [http://127.0.0.1:8000/posts/](http://127.0.0.1:8000/posts/)

6. Usar el **buscador de Posts**:  
   [http://127.0.0.1:8000/search/](http://127.0.0.1:8000/search/)

7. (Opcional) Acceder al **panel de administración**:  
   [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧠 Explicación breve del patrón MVT

| Componente | Archivo(s) principal(es) | Función |
|-------------|--------------------------|----------|
| **Model** | `models.py` | Define la estructura de la base de datos. |
| **View** | `views.py` | Contiene la lógica del negocio. Procesa peticiones y retorna respuestas. |
| **Template** | Carpeta `templates/blog/` | Define la interfaz HTML mostrada al usuario. |

Django conecta estos tres componentes de forma automática mediante las URLs y el ORM.

---

## 🔍 Formularios

Se incluyen 4 formularios:
- `AuthorForm` → para crear autores  
- `CategoryForm` → para crear categorías  
- `PostForm` → para crear posts  
- `SearchForm` → para buscar posts por título  

Cada uno se encuentra definido en `forms.py` y renderizado mediante `form.as_p` en las plantillas.

---

## 🌐 Herencia de plantillas

Todas las páginas heredan desde `base.html`, que contiene:
- Título del sitio
- Navegación
- Encabezado y pie de página


---

## 📄 Licencia y autoría

Proyecto creado por **de la Fuente Affonso**.  
Uso educativo para aprendizaje de Django y patrón MVT.

