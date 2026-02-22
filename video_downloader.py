# import datetime
# data  =  datetime.datetime.now().strftime('%Y-%M-%D')
# print(data)
import yt_dlp
import tkinter as tk
from tkinter import filedialog

# label.pack()
# root.geometry('300*200')

# root = tk.Tk()
# root.title("Downloading ")
# label = tk.Label(root, text='welcome to mohammed kamal downloader')
# tk.Label(root, text="First Name").grid(row=2, column=0)
# tk.Label(root, text="Last Name").grid(row=3, column=0)

# entry1 = tk.Entry(root)
# entry2 = tk.Entry(root)


# entry1.grid(row=2, column=1)
# entry2.grid(row=3, column=1)

# root.mainloop()

def download(url, path="downloads"):

    ydl_opts = {
        "outtmpl": f"{path}/%(title)s.%(ext)s",
        # "format": "worstvideo+worstaudio/worst",
        "format": "best[ext=mp4]/best",
        "merge_output_format": "mp4",
        "quiet": False,
        "noplaylist": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts)as f:
            file = f.extract_info(url,download=True)
            return file
    except Exception as e:
        print('Error is',e)
        return


def open_file_diloge():
    folder = filedialog.askdirectory()
    if folder:
        print(f'folder selected is {folder}')
    return folder


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    path = open_file_diloge()
    url = input("inter URL to video ? \n")
    if not path:
        print("please select dir... or check downloads file ")
    data =  download(url,path)    
    if data:
        print("\nDownload complete!")
        print(f"Title: {data.get('title')}")
        print(f"Uploader: {data.get('uploader')}")
        print(f"Duration: {data.get('duration')} seconds")
        print(f"File saved in: downloads/")
