from pytube import YouTube
import os

yt = YouTube(
	str(input("İndirmek istediğiniz videonun URL'sini girin: \n>> ")))

video = yt.streams.filter(only_audio=True).first()

print("Hedefi Girin")
destination = str(input(">> ")) or '.'

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " başarıyla indirildi.")
