from pytube import YouTube
import sys

link = input("Enter YT Link: ")
yt = YouTube(link)


print("Title: ", yt.title)
print("Views: ", yt.views)
print("Publish Date: ", yt.publish_date)

res = int(input("1.Get Highest Resolution\n2.Get Lowest Resolution\nInput:"))

if res == 1:
    yd = yt.streams.get_highest_resolution()
else:
    yd = yt.streams.get_lowest_resolution()
file_path = input("Enter Download Path: ")
try:
    yd.download(file_path)
except FileNotFoundError:
    sys.exit("Incorrect File Path :(")

print("Sucessfully Downloaded At Path: ", file_path)
sys.exit()
