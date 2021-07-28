from tkinter import *
import pygame
from tkinter import filedialog
from PIL import ImageTk,Image
root=Tk()
root.geometry("500x400")
root.title("MP3 Player")
#pygame
pygame.mixer.init()

#frame
frame=Frame(root,bg="blue")
frame.pack()

#listbox
song_box=Listbox(frame,width=50,height=15,selectbackground="khaki1",selectforeground="navy")
song_box.pack(pady=10)

def resume_music():
    pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

def  stop_music():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

def play_music():
   get_song=song_box.get(ACTIVE)
   get_song=str.format("C:/Users/User/Desktop/songs/{}.mp3".format(get_song))
   #get_song=f'C:/Users/User/Desktop/songs/{get_song}.mp3'
   print(get_song)
   pygame.mixer.music.load(get_song)
   pygame.mixer.music.play(loops=0)    

def forward_song():
   
    current_song_tuple=song_box.curselection()
    #It is returning tuple not exact location
    print(current_song_tuple)
    
    # now to get exact location
    current_song=current_song_tuple[0]
    print(current_song)

    next_song=current_song+1
    print(next_song)
    get_song=song_box.get(next_song)
    print(get_song)
    get_song=str.format("C:/Users/User/Desktop/songs/{}.mp3".format(get_song))
    #get_song=f'C:/Users/User/Desktop/songs/{get_song}.mp3'
    #print(get_song)
    pygame.mixer.music.load(get_song)
    pygame.mixer.music.play(loops=0)
    # clear selector and then move
    song_box.selection_clear(0,END)
    song_box.activate(next_song)
    # SET ACTIVE BAR
    song_box.selection_set(next_song,last=None)
    length=song_box.size()
    print(length)
    #if next_song ==length-1:
     #  pygame.mixer.music.play(next_song)
      # song_box.selection_clear(0,END)
       #song_box.activate(0)
       #song_box.selection_set(0,last=None)
       
       


def previous_song():
    current_song_tuple=song_box.curselection()
    #It is returning tuple not exact location
    print(current_song_tuple)
    
    # now to get exact location
    current_song=current_song_tuple[0]
    print(current_song)

    previous_song=current_song-1
    
    get_song=song_box.get(previous_song)
    print(get_song)
    get_song=str.format("C:/Users/User/Desktop/songs/{}.mp3".format(get_song))
    print(get_song)
    pygame.mixer.music.load(get_song)
    pygame.mixer.music.play(loops=0)
    # clear selector and then move
    song_box.selection_clear(0,END)
    song_box.activate(previous_song)
    # SET ACTIVE BAR
    song_box.selection_set(previous_song,last=None)
    print(previous_song)
    
    


def add_one_song():
    song=filedialog.askopenfilename(initialdir='desktop/songs/',title="Select a song",filetypes=(("mp3 files","*.mp3"),("all song","*.*")))
    song=song.replace("C:/Users/User/Desktop/songs/","")
    song=song.replace(".mp3","")
    song_box.insert(END,song)

def add_many_songs():
    many_songs=filedialog.askopenfilenames(initialdir='desktop/songs/',title="Select a song",filetypes=(("mp3 files","*.mp3"),("all song","*.*")))
    for item in many_songs:
        item=item.replace("C:/Users/User/Desktop/songs/","")
        item=item.replace(".mp3","")
        song_box.insert(END,item)

def delete_one_song():
    song_box.delete(ANCHOR)
    #song_box.delete(ACTIVE)
    pygame.mixer.music.stop()

def delete_all_song():
    song_box.delete(0,END)
    pygame.mixer.music.stop()

# menubar
menu_bar=Menu(root)
root.config(menu=menu_bar)
song_menu=Menu(menu_bar)
menu_bar.add_cascade(label="Add Song",menu=song_menu)
song_menu.add_command(label="Add one song",command=add_one_song)
song_menu.add_command(label="Add Many song",command=add_many_songs)

delete_menu=Menu(menu_bar)
menu_bar.add_cascade(label="Delete song",menu=delete_menu)
delete_menu.add_command(label="Delete one song",command=delete_one_song)
delete_menu.add_command(label="Delete All song",command=delete_all_song)


#resize img

music_img=Image.open("desktop/music.png")
resize_music_img=music_img.resize((58,58),Image.ANTIALIAS)
new_music_img=ImageTk.PhotoImage(resize_music_img)

pause_img=Image.open("desktop/pause.png")
resize_pause_img=pause_img.resize((70,70),Image.ANTIALIAS)
new_pause_img=ImageTk.PhotoImage(resize_pause_img)

resume_img=Image.open("desktop/play.png")
resize_resume_img=resume_img.resize((50,50),Image.ANTIALIAS)
new_resume_img=ImageTk.PhotoImage(resize_resume_img)

stop_img=Image.open("desktop/stop.png")
resize_stop_img=stop_img.resize((50,50),Image.ANTIALIAS)
new_stop_img=ImageTk.PhotoImage(resize_stop_img)

forward_img=Image.open("desktop/forwardbutton.png")
resize_forward_img=forward_img.resize((90,55),Image.ANTIALIAS)
new_forward_img=ImageTk.PhotoImage(resize_forward_img)

previous_img=Image.open("desktop/backbutton.png")
resize_previous_img=previous_img.resize((50,50),Image.ANTIALIAS)
new_previous_img=ImageTk.PhotoImage(resize_previous_img)

stop_btn=Button(root,image=new_stop_img,borderwidth=0,command=stop_music)
stop_btn.place(x=190,y=300)

stop_label=Label(root,text="Stop",fg="red")
stop_label.place(x=200,y=360)

previous_btn=Button(root,image=new_previous_img,borderwidth=0,command=previous_song)
previous_btn.place(x=30,y=300)

previous_label=Label(root,text="Previous Song",fg="red")
previous_label.place(x=10,y=360)

forward_btn=Button(root,image=new_forward_img,borderwidth=0,command=forward_song)
forward_btn.place(x=395,y=298)

forward_label=Label(root,text="Next Song",fg="red")
forward_label.place(x=410,y=360)

pause_btn=Button(root,image=new_pause_img,borderwidth=0,command=pause_music)
pause_btn.place(x=255,y=290)

pause_label=Label(root,text="Pause",fg="red",)
pause_label.place(x=270,y=360)

music_btn=Button(root,image=new_music_img,borderwidth=0,command=play_music)
music_btn.place(x=110,y=295)

music_label=Label(root,text="Music",fg="red")
music_label.place(x=120,y=360)

resume_btn=Button(root,image=new_resume_img,borderwidth=0,command=resume_music)
resume_btn.place(x=340,y=300)

resume_label=Label(root,text="Resume",fg="red")
resume_label.place(x=340,y=360)

root.mainloop()