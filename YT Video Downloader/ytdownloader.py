from pytube import YouTube
import sys
import os

link = input("Enter YT Link: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Publish Date: ", yt.publish_date)

res = int(input("1.Get Highest Resolution\n2.Get Lowest Resolution\nInput: "))

if res == 1:
    yd = yt.streams.get_highest_resolution()
else:
    yd = yt.streams.get_lowest_resolution()

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_directory, yd.title)
try:
    yd.download(file_path)
except FileNotFoundError:
    sys.exit("Incorrect File Path :(")

print("Successfully Downloaded At Path: ", file_path)
sys.exit()
