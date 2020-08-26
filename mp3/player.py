from tkinter import *
# set a tkinter instance
root = Tk()

root.title('MP3 Player')
root.geometry('500x400')

# put in root window
playlist_box = Listbox(root, bg='black', fg='green', width=60)
# two way to put on screen pack or grid
playlist_box.pack(pady=20)

# loop needed to start app, always running picking up changes
root.mainloop()