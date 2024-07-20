# WildRENIEC Project

<!--![Project Logo](path_to_logo_image) <!-- Optional: Add a logo for your project -->

## Descripción

El **WildRENIEC Project** es una aplicación avanzada desarrollada en Python que permite la búsqueda de datos específicos extraídos de un DNI peruano utilizando la API de RENIEC (Registro Nacional de Identificación y Estado Civil). Esta herramienta está diseñada para ser intuitiva y eficiente, brindando una interfaz web desde la cual los usuarios pueden realizar búsquedas rápidas y precisas.

## Características

- **Búsqueda de Datos del DNI**: Extrae información específica del DNI utilizando la API oficial de RENIEC.
- **Interfaz Web Intuitiva**: Proporciona una plataforma web fácil de usar para realizar las búsquedas.
- **Servidor Local**: Inicia un servidor local para la visualización y operación de la aplicación.
- **Desarrollado en Python**: Utiliza Python como lenguaje principal para el desarrollo, asegurando una alta compatibilidad y eficiencia.

## Instalación

1. **Dirigirte a la carpeta del repositorio clonado**
   ```bash
   cd Descargas/WildRProject/
   ```
2. **Abrir una terminal y ejecutar el APP.PY**
   ```bash
   python app.py
   ```

### Requisitos

- Python 3.x
- Librerías necesarias (pueden ser instaladas desde `requirements.txt`)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tuusuario/WildRENIEC-Project.git
   cd WildRENIEC-Project
   ```

2. **Crear un entorno virtual (opcional pero recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows usa `venv\Scripts\activate`
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar las variables de entorno**
   Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
   ```env
   RENIEC_API_KEY=tu_api_key
   ```

5. **Ejecutar el servidor local**
   ```bash
   python app.py
   ```

6. **Acceder a la aplicación**
   Abre tu navegador web y ve a `http://127.0.0.1:5000` para acceder a la interfaz de búsqueda.

## Uso

Una vez que el servidor esté en funcionamiento, los usuarios pueden ingresar el número de DNI en el campo de búsqueda de la interfaz web. La aplicación consultará la API de RENIEC y mostrará los datos relevantes.

## Contribuir

¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos para contribuir al proyecto:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y commitea (`git commit -am 'Agrega una nueva característica'`).
4. Sube tus cambios (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Mira el archivo `LICENSE` para más detalles.

## Contacto

Para cualquier duda o consulta, puedes contactarnos a través del correo electrónico: [basicboywn@gmail.com](mailto:basicboywn@gmail.com).

---

¡Gracias por usar WildRENIEC Project!
