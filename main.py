from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
import traceback

file_size = 0


def checkprogress(stream=None, chunk=None, remaining=None):
    file_downloaded = (file_size-remaining)
    percentage = (file_downloaded/file_size)*100
    button.config(text="{:00.0f} % downloaded".format(percentage))


def downloadvideo():
    try:
        global file_size
        button.config(text="Please wait...")
        button.config(state=DISABLED)
        url = urlfield.get()
        download_path = askdirectory()
        if download_path is None:
            return
        youtube = YouTube(url, on_progress_callback=checkprogress)
        video_stream = youtube.streams.first()
        file_size = video_stream.filesize
        video_stream.download(download_path)
        button.config(text="Download")
        button.config(state=NORMAL)
        showinfo("Video Downloaded", "Video Downloaded Successfully")
        urlfield.delete(0, END)
    except Exception as e:
        print(e)
        traceback.print_exc()
        print("Some error occurred!!")


def downloadvideothread():
    thread=Thread(target=downloadvideo)
    thread.start()


# GUI of Youtube Video Downloader
view = Tk()
view.title("Youtube Video Downloader")
view.geometry("500x600")
#file = PhotoImage(file='image.png')
label = Label(view, text='Youtube Video Downloader', font=("arial", 18))
label.pack(side=TOP, pady=50)
urlfield=Entry(view, font=("arial", 18), justify=CENTER)
urlfield.pack(side=TOP, fill=X, padx=10)
button = Button(view, text="Download", font=("arial", 18), relief="ridge", command=downloadvideothread)
button.pack(side=TOP, pady=10)
view.mainloop()
