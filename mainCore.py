from tkinter import messagebox
from pytube import YouTube
from customtkinter import *
from PIL import Image, ImageTk
import threading


def checkButtonHandler(master, textBox):
    threading.Thread(target=checkButton, args=(master, textBox,)).start()

def checkButton(master, textBox):
    text = textBox.get('1.0', 'end')
    if len(text) == 0:
        messagebox.showerror('Error!', 'Unavailable url')
    else:
        # noinspection PyBroadException
        try:
            yt = YouTube(text)
            yt_title = yt.title
            check = messagebox.askyesnocancel('Download', f"Are you trying to download video: '{yt_title}' ??")
            if check == YES:
                messagebox.showinfo('Download Start', 'Your download has been started in the background just wait a bit!!')
                yd= yt.streams.get_highest_resolution()
                yd.download()
                messagebox.showinfo('Download Start', 'Your download has been ended successfully')
            elif check == NO:
                master.destroy()
            else:
                pass

        except Exception as e:
            messagebox.showerror('Error', 'Check your video url and try again!!')


class App(CTk):

    def __init__(self):
        super().__init__()
        self.videoImage = None
        self.frame1 = None
        self.frame2 = None
        self.frame3 = None
        self.frame4 = None
        self.textBox = None
        self.title('Youtube Downloader_v.1-Beta')
        self.eval('tk::PlaceWindow . center')
        self.geometry('400x213')
        self.resizable(False, False)

        self.firstFrame()
        self.secondFrame()

    def firstFrame(self):
        self.frame1 = CTkFrame(self, fg_color='black', bg_color='black')
        self.frame1.pack(fill=BOTH)
        image = ImageTk.PhotoImage(Image.open('assets/logo.png').resize((200, 100)))
        CTkLabel(self.frame1, text='', image=image).grid(row=0, column=0, sticky='n', pady=(5, 0))
        CTkLabel(self.frame1, text_color='white', text='|_->This script use python to download any video from\n'
                                                       '|_->Youtube with any resolution your want!', font=('Arial', 15, 'bold'))\
            .grid(row=1, column=0, sticky='n', padx=10, pady=(0, 5))

    def secondFrame(self):
        self.frame2 = CTkFrame(self, fg_color='black', bg_color='black')
        self.frame2.pack(fill=BOTH)
        CTkLabel(self.frame2, text='Link / URL: ', font=('Arial', 15, 'bold'), text_color='white').grid(row=0, column=0, padx=10, pady=(3, 0))
        self.textBox = CTkTextbox(self.frame2, width=300, height=5)
        self.textBox.grid(row=0, column=1, pady=(3, 0))
        CTkButton(self.frame2, text='Get the video', hover_color='#cccccc', fg_color='#999999',
                  text_color='black', command=lambda: checkButtonHandler(self, self.textBox)).grid(row=1,
                                                                                      column=0,
                                                                                      columnspan=2,
                                                                                      ipadx=130,
                                                                                      pady=3)

    def thirdFrame(self):
        pass

    def forthFrame(self):
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()
