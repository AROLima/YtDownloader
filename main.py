from pytube import YouTube
from pytube.exceptions import VideoUnavailable, PytubeError
import os

def download_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()

        if video_stream:
            print(f"Iniciando o download de: {yt.title}...")

            # Faz o download do vídeo para o diretório especificado
            video_stream.download(output_path)

            print(f"Download concluído: {yt.title}")

        else:
            print("Não foi possível encontrar uma stream disponível para download.")

    except VideoUnavailable as ve:
        print(f"Erro: {ve}")
    except PytubeError as pe:
        print(f"Erro no Pytube: {pe}")
    except KeyboardInterrupt:
        print("\nDownload interrompido pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Exemplo de uso
if __name__ == "__main__":
    video_url = input("Insira a URL do vídeo do YouTube: ")
    output_directory = input("Insira o diretório de saída (pressione Enter para usar o diretório atual): ")

    if not output_directory:
        output_directory = '.'

    download_video(video_url, output_directory)

