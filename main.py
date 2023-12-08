from pydeezer import Deezer, Downloader
from pydeezer.constants import track_formats
import os
import json

download_dir = "C:\\Users\\Seu\\diretorio"
arl = 'arl'

deezer = Deezer(arl=arl)
user_info = deezer.user
#print(user_info)

playlist_id = "6409629584"
playlist = deezer.get_playlist_tracks(playlist_id)

track_ids = []

for track in playlist:
    track_ids.append(track["SNG_ID"])


downloader = Downloader(deezer, track_ids, download_dir, quality=track_formats.MP3_320, concurrent_downloads=2)
downloader.start()

def remover_arquivos_lrc(diretorio):
    if not os.path.isabs(diretorio):
        diretorio = os.path.abspath(diretorio)

    contador = 0
    try:
        print("Limpando os arquivos temporários...")
        for arquivo in os.listdir(diretorio):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            if os.path.isfile(caminho_arquivo) and arquivo.endswith(".lrc"):
                os.remove(caminho_arquivo)
                contador += 1
                print(f"Arquivo removido: {caminho_arquivo}")
        print(f'Limpeza concluída.\n{contador} arquivo(s) removido(s)')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

remover_arquivos_lrc(download_dir)