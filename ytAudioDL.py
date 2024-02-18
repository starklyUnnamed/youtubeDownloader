from pytube import YouTube

yt = YouTube(input("Please Enter the URL of the YouTube video you would like to download:  "))

video = yt.streams.get_highest_resolution()
video.download(output_path='/home/stark/Desktop/youtubeDLs/')