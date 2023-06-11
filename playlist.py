from pytube import Playlist
import os

link = input("Enter the YouTube playlist URL: ")

playlist = Playlist(link)

playlist_folder = playlist.title.replace('/', '-')  # Replace invalid characters in folder name

file_path = os.path.join('./Playlists',playlist_folder)


# Create a folder for the playlist
os.makedirs(file_path, exist_ok=True)

print(f"Downloading videos from playlist: {playlist.title}")

for video in playlist.videos:
    video.streams.first().download(output_path=file_path)


print("Download complete.")

