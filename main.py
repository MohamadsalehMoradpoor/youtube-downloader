from pytube import YouTube
link = input('Enter the link: ')
yl = YouTube(link)

print("Title: ", yl.title)
print("Number of views: ", yl.views)
print("Length of video: ", yl.length)
print("Rating of video: ", yl.rating)

# print(yl.streams.filter(only_audio=True))
# print(yl.streams.filter(only_video=True))

# ys = yl.streams.get_by_itag('251')
# ys.download()

ys = yl.streams.get_highest_resolution()
print("Downloading...")
ys.download()
print("Download Completed!!")