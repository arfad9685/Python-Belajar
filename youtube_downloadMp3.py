from unittest import result
from pytube import YouTube
import os

url = input("masukkan link : ")
yt = YouTube(url)
result = yt.streams.filter(only_audio=True).first()
output_file = result.download('download')
path, _ = os.path.splitext(output_file)

os.rename(output_file, path + '.mp3')
print(yt.title,"berhasil di download")