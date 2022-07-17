from pytube import Playlist
import os

p = Playlist('https://www.youtube.com/playlist?list=PLgkbRcCnThjCsHYvpExLqZEI891dFAMR2')

print(f'Downloading: {p.title}')

for video in p.videos:
    #video.streams.first().download()
    output_file = video.streams.filter(only_audio=True).first().download(output_path='./songs')
    base,ext = os.path.splitext(output_file)
    new_file = base + '.mp3'
    os.rename(output_file,new_file)

