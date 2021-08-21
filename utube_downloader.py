from pytube import YouTube
import os

video_url = input("Enter URL of Video\n")
video = YouTube(video_url)
stream = video.streams.get_highest_resolution()
stream.download()
print("Download Successful")

restart=input("Would you like to install more videos?(y/n)\n")
if restart == "y":
    while True:
        os.system('cls')
        pass
elif restart == "n":
    while True:
        print("Thanks for using")
        exit()
