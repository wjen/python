from tkinter import *
# set a tkinter instance
root = Tk()

root.title('MP3 Player')
root.geometry('500x400')

# put in root window
playlist_box = Listbox(root, bg='black', fg='green', width=60)
# two way to put on screen pack or grid
playlist_box.pack(pady=20)

# Define button images for controls
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img = PhotoImage(file='images/forward50.png')
play_btn_img = PhotoImage(file='images/play50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')

# create button frame
control_frame = Frame(root)
control_frame.pack(pady=20)

# Create play stop buttons
back_button = Button(control_frame, image=back_btn_img)
forward_button = Button(control_frame, image=forward_btn_img)
play_button = Button(control_frame, image=play_btn_img)
pause_button = Button(control_frame, image=pause_btn_img)
stop_button = Button(control_frame, image=stop_btn_img)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# loop needed to start app, always running picking up changes
root.mainloop()