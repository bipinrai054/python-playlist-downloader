from pytube import Playlist
import os

playlist_name = input('Enter the playlist name: ')
print('               ')

#p = Playlist('https://www.youtube.com/playlist?list=PLgkbRcCnThjCsHYvpExLqZEI891dFAMR2')

p = Playlist(playlist_name)

print(f'Downloading: {p.title}')
print ('                    ')

for video in p.videos:
    #video.streams.first().download()
    output_file = video.streams.filter(only_audio=True).first().download(output_path='./songs')
    base,ext = os.path.splitext(output_file)
    new_file = base + '.mp3'
    print(video.title) 
    print('                             ')
    os.rename(output_file,new_file)

