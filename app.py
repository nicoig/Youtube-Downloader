# Para crear el requirements.txt ejecutamos 
# pipreqs --encoding=utf8 --force

# Primera Carga a Github
'''
git init
git add .
git remote add origin https://github.com/nicoig/Youtube-Downloader.git
git commit -m "Initial commit"
git push -u origin master
'''

# Actualizar Repo de Github
'''
git add .
git commit -m "Se actualizan las variables de entorno"
git push origin master
'''

# En Render
# agregar en variables de entorno
# PYTHON_VERSION = 3.9.12

################################################


import streamlit as st
from pytube import YouTube
from io import BytesIO

st.title("Descargador de YouTube")

video_url = st.text_input("Ingresa la URL del video de YouTube:")

if video_url:
    yt = YouTube(video_url)
    download_type = st.radio("¿Qué deseas descargar?", ("Video", "Audio"))

    if download_type == "Video":
        video_qualities = [stream.resolution for stream in yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()]
        selected_quality = st.selectbox("Selecciona la calidad del video:", video_qualities)
    else:
        audio_qualities = [stream.abr for stream in yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc()]
        selected_quality = st.selectbox("Selecciona la calidad del audio:", audio_qualities)

    if st.button("Descargar"):
        try:
            if download_type == "Video":
                video_stream = yt.streams.filter(res=selected_quality, progressive=True, file_extension='mp4').first()
                if not video_stream:
                    video_stream = yt.streams.filter(res=selected_quality, file_extension='mp4').first()
                video_buffer = BytesIO()
                video_stream.stream_to_buffer(video_buffer)
                video_buffer.seek(0)
                st.download_button(
                    label="Descargar video",
                    data=video_buffer,
                    file_name=f"{yt.title}-{selected_quality}.mp4",
                    mime="video/mp4"
                )
            else:
                audio_stream = yt.streams.filter(only_audio=True, abr=selected_quality, file_extension='mp4').first()
                audio_buffer = BytesIO()
                audio_stream.stream_to_buffer(audio_buffer)
                audio_buffer.seek(0)
                st.download_button(
                    label="Descargar audio",
                    data=audio_buffer,
                    file_name=f"{yt.title}.mp3",
                    mime="audio/mp3"
                )
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

    st.subheader("Detalles del Video")
    st.write(f"Título: {yt.title}")
    st.write(f"Duración: {yt.length // 60} minutos")
    st.write(f"Cantidad de vistas: {yt.views}")
    st.video(video_url)
