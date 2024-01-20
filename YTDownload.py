# the program can download both the mp4 and mp3 files of a youtube video through its YouTubeUrl

# pytube got a problem with mac in which using yt.streams.filter(only_audio=True).first() give an audio file that is twice as long and the file format remains .mp4
# so the solution is to extract the video file first (mp4 file) using pytube, and afterwards converting it to mp3 through ffmpeg

from pytube import YouTube, Playlist
import subprocess



def downloadVideo(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()

    videoPath = video.download()
    print(videoPath)
    audioPath = videoPath.replace(".mp4", ".mp3")
    print(audioPath)

    subprocess.run(['ffmpeg', '-i', videoPath, '-q:a', '0', '-map', 'a', audioPath])



print(" ")
print("Option 1: download with individual URL")
print("Option 2: download with playlist URL")
print(" ")

option = input("Choose Option: ")

if option == "1":

    print(" ")
    YouTubeUrl = input("Enter YouTubeURL: ")
    downloadVideo(YouTubeUrl)

    print("Done")

elif option == "2":

    print(" ")
    playlistUrl = input("Enter Playlist URL: ")
    print(" ")
    playlist = Playlist(playlistUrl)

    # show the number of videos contained in the playlist
    print(f"Number of videos in the playlist: {len(playlist.video_urls)}")

    for url in playlist:
        downloadVideo(url)

else:
    print("Inputted Option Incorrect")
