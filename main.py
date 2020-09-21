from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *


file_size = 0

def progress(stream , chunk, file_handle , remaining = None):
    #gets % of file download
    file_downloaded = (file_size - file_handle)
    per = float((file_downloaded/file_size)*100)
    dBtn.config(text = "{:00.0f} % downloaded" . format(per))

def startDownload():
    global file_size
    try:
        url = urlField.get()
        print(url)
        #button change
        dBtn.config(text= 'Please wait....')
        dBtn.config(state = DISABLED)
        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return

        # Craeting youtube object for url..
        ob = YouTube(url, on_progress_callback= progress)

        strm = ob.streams.first()
        file_size = strm.filesize
        vTitle.config(text = strm.title)
        vTitle.pack(side=TOP)
        print(file_size)

        strm.download(path_to_save_video)
        print("DONE")
        dBtn.config(text= "Start DownLoad")
        dBtn.config(state = NORMAL)
        showinfo("Download Finished", "Downloaded Succesfully")
        urlField.delete(0,END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print("Error..")

def startDownloadThread():
    #create thread..
    thread = Thread(target=startDownload)
    thread.start()

# Starting GUI building..
main = Tk()

main.title("YouTube DownLoader")

#icon set
main.iconbitmap('utube.ico')

main.geometry("500x600")

#heading icon
file = PhotoImage(file='utube.png')
headingIcon = Label(main,image=file)
headingIcon.pack(side = TOP)

#url textfield
urlField = Entry(main, font = ("verdana", 18), justify = CENTER)
urlField.pack(side=TOP, fill = X, padx = 10)

#Download buttom
dBtn = Button(main,text="Start Download", font = ("verdana", 18), relief = 'ridge', command= startDownloadThread)
dBtn.pack(side = TOP, pady = 10)

#video_title
vTitle = Label(main, text = "Video Title")
#vTitle.pack(side = TOP)
main.mainloop()