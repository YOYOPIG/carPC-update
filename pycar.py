import tkinter as tk  # Use tkinter as GUI
from tkinter import *
from tkinter.ttk import *
import os
import pygame
import glob
from PIL import ImageTk, Image
import cv2

def fun():
    return

def play_music():
    song = song_box.get(ACTIVE)
    # song = f'./music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Main program starts here
# Create window
window = tk.Tk()
window.title('Car PC')
window.geometry('800x480') # Set window size(L*W)
# window.state("zoomed")
window.resizable(0,0)
background_image = PhotoImage(file = "./resources/bg2.png") 
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

main_frame = tk.Frame(window)
nav_frame = tk.Frame(window)

nav_frame.grid(row=0, column=0, rowspan=20, padx=1, pady=1)
main_frame.grid(row=0, column=1, rowspan=20, padx=1, pady=1)

pygame.mixer.init()

# Load images
img_home = PhotoImage(file = "./resources/home1.png") 
img_home2 = PhotoImage(file = "./resources/home2.png") 
img_map = PhotoImage(file = "./resources/map1.png") 
img_map2 = PhotoImage(file = "./resources/map2.png") 
img_music = PhotoImage(file = "./resources/music1.png") 
img_music2 = PhotoImage(file = "./resources/music2.png")
img_rear = PhotoImage(file = "./resources/rear1.png") 
img_rear2 = PhotoImage(file = "./resources/rear2.png")

# Resize
sample_rate = 3
img_home = img_home.subsample(sample_rate, sample_rate)
img_home2 = img_home2.subsample(sample_rate, sample_rate)
img_map = img_map.subsample(sample_rate, sample_rate)
img_map2 = img_map2.subsample(sample_rate, sample_rate)
img_music = img_music.subsample(sample_rate, sample_rate)
img_music2 = img_music2.subsample(sample_rate, sample_rate)
img_rear = img_rear.subsample(sample_rate, sample_rate)
img_rear2 = img_rear2.subsample(sample_rate, sample_rate)

bg_color = '#2f3136'

# Nav panel buttons
button_home = tk.Button(nav_frame, image = img_home,command=fun, bd = 0, bg = bg_color)
button_map = tk.Button(nav_frame, image = img_map,command=fun, bd = 0, bg = bg_color)
button_music = tk.Button(nav_frame, image = img_music,command=fun, bd = 0, bg = bg_color)
button_rearcam = tk.Button(nav_frame, image = img_rear,command=fun, bd = 0, bg = bg_color)

button_home.pack()
button_map.pack()
button_music.pack()
button_rearcam.pack()


# Music player
music_frame = tk.Frame(window)
# button_home2 = tk.Button(music_frame, image = img_home,command=fun, bd = 0, bg = bg_color)
# button_home2.pack()
# main_frame = music_frame
# main_frame.grid(row=0, column=0, rowspan=20, padx=1, pady=1)

music_frame = tk.Frame(window)
play_btn = Button(music_frame ,text='Play',command=play_music)
pause_btn = Button(music_frame, text='Pause',command=fun)
forward_btn = Button(music_frame, text='Next',command=fun)
prev_btn = Button(music_frame, text='Prev',command=fun)
song_box = Listbox(music_frame, bg='black', fg='white', width=60)

song_box.pack(pady=20)
play_btn.pack()
pause_btn.pack()
forward_btn.pack()
prev_btn.pack()
music_frame.grid(row = 0, column = 1, sticky ="nsew")

# Add songs
for song in glob.glob("./music/*.mp3"):
    tmp = song
    # tmp = song.replace("./music/", "")
    # tmp = tmp.replace(".mp3", "")
    song_box.insert(END, tmp)



# cam
cap = cv2.VideoCapture(0)
cam_frame = tk.Frame(window)
lmain = Label(cam_frame)
lmain.grid()
cam_frame.grid(row=0, column=2, rowspan=20, padx=1, pady=1)
# function for video streaming
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 

# # Set fonts
# bold_font = 'Open sans bold'
# norm_font = 'Open sans'

# # Set colors
# bg_color = '#2f3136'
# fg_color = 'white'
# checkbox_color = '#7a6bff'

# # Variable declarations for ui
# pos0_on = tk.BooleanVar()
# pos1_on = tk.BooleanVar()
# pos2_on = tk.BooleanVar()
# pos3_on = tk.BooleanVar()
# pos4_on = tk.BooleanVar()
# pos5_on = tk.BooleanVar()
# pos6_on = tk.BooleanVar()
# pos7_on = tk.BooleanVar()
# # features
# pm10_on = tk.BooleanVar()
# pm25_on = tk.BooleanVar()
# pm100_on = tk.BooleanVar()
# temp_on = tk.BooleanVar()
# humid_on = tk.BooleanVar()
# var = tk.StringVar()
# plot_time = tk.IntVar()

# # Icons
# # Creating a photoimage object to use image 
# pi_scatter = PhotoImage(file = "./resources/home1.png") 
# pi_detail = PhotoImage(file = "./resources/home1.png") 
# pi_corr = PhotoImage(file = "./resources/home1.png") 
# pi_box = PhotoImage(file = "./resources/home1.png") 
# pi_map = PhotoImage(file = "./resources/home1.png") 
# pi_line = PhotoImage(file = "./resources/home1.png")
# pi_dl = PhotoImage(file = "./resources/home1.png")
# pi_logo = PhotoImage(file = "./resources/home1.png")
# # Resizing image to fit on button 
# sample_rate = 8
# scatter_icon = pi_scatter.subsample(sample_rate, sample_rate)
# detail_icon = pi_detail.subsample(sample_rate, sample_rate) 
# corr_icon = pi_corr.subsample(sample_rate, sample_rate) 
# box_icon = pi_box.subsample(sample_rate, sample_rate) 
# map_icon = pi_map.subsample(sample_rate, sample_rate) 
# line_icon = pi_line.subsample(sample_rate, sample_rate) 
# dl_icon = pi_dl.subsample(6, 6)
# logo_icon = pi_logo.subsample(1, 1)

# # Declare widgets
# button_dl_data = tk.Button(window, image = dl_icon, compound = LEFT, command=fun, bd = 0, bg = bg_color, activeforeground=fg_color, activebackground=bg_color)
# button_scatter = tk.Button(window, image = scatter_icon, compound = LEFT, command=fun, bd = 0, bg = bg_color, activeforeground=fg_color, activebackground=bg_color)
# button_line = tk.Button(window, image = line_icon, compound = LEFT, command=fun, bd = 0, bg = bg_color, activeforeground=fg_color, activebackground=bg_color)
# button_detail = tk.Button(window, image = detail_icon, compound = LEFT, command=fun, bd = 0, bg = bg_color, activeforeground=fg_color, activebackground=bg_color)
# button_corr = tk.Button(window, image = corr_icon, compound = LEFT, command=fun, bd = 0, bg = bg_color, activeforeground=fg_color, activebackground=bg_color)
# button_box = tk.Button(window, image = box_icon, compound = LEFT, command=fun, bd = 0, bg = bg_color, activeforeground=fg_color, activebackground=bg_color)
# button_map = tk.Button(window, image = map_icon, compound = LEFT, command=fun, bd = 0, bg = bg_color, activeforeground=fg_color, activebackground=bg_color)


# # Place widgets on the window

# window.grid_rowconfigure(11, minsize=50) # empty row
# button_scatter.grid(row=12, column=0, padx=2, pady=2)
# button_detail.grid(row=13, column=0, padx=2, pady=2)


# window.grid_columnconfigure(3, minsize=20)
# main_frame.grid(row=0, column=4, rowspan=20, padx=1, pady=1)


# At the end, start the window loop
window.mainloop()