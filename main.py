
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("Copie aqui o link do vídeo do YouTube que deseja baixar o áudio: ")

reso = YouTube(url)
    
def audio_mp3(url):
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)

    audio = yt.streams.get_audio_only()
    # print(f"{audio.abr}")
    # print(f"{yt.streams.filter()}")
    
    audio.download(mp3=True)

audio_mp3(url)