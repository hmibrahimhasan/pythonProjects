import pytube

link = input("Enter URL: ")
yt = pytube.YouTube(link)

# print(yt.streams)

stream = yt.streams.filter(progressive = True)

for i in stream:
	print(i)

tag = input("Enter itag: ")
ys = yt.streams.get_by_itag(int(tag))

print("Download Started....")

ys.download()

print("\nDownload Completed /////")

