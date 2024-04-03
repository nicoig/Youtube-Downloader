# Descargador de YouTube con Streamlit y Pytube

Esta aplicación permite descargar videos y audios de YouTube seleccionando la calidad deseada. La interfaz de usuario está construida con Streamlit, y la descarga se maneja a través de Pytube.

## Características

- **Descarga de Videos**: Selecciona la calidad del video para descargar.
- **Descarga de Audios**: Extrae y descarga el audio en calidad seleccionable.
- **Visualización de Detalles del Video**: Muestra el título, duración y cantidad de vistas del video de YouTube.

## Instalación

Para ejecutar esta aplicación, necesitarás Python instalado en tu sistema. Se recomienda usar Python 3.7 o superior. Además, deberás instalar las siguientes dependencias:

```bash
pip install streamlit pytube
Ejecución
Una vez instaladas las dependencias, puedes ejecutar la aplicación con el siguiente comando:

```bashbash
streamlit run tu_script.py
Reemplaza tu_script.py con el nombre de tu archivo que contiene el código de la aplicación.

Uso
Abre la aplicación en tu navegador web.
Ingresa la URL del video de YouTube que deseas descargar.
Selecciona el tipo de descarga: Video o Audio.
Elige la calidad deseada para la descarga.
Haz clic en "Descargar" para iniciar la descarga del archivo seleccionado.
Limitaciones
La capacidad para combinar video y audio de streams separados (para calidades de video altas que no sean progresivas) no está implementada directamente en la aplicación y requeriría herramientas adicionales como FFmpeg.
Asegúrate de respetar los derechos de autor y las políticas de uso de contenido de YouTube al utilizar esta herramienta.