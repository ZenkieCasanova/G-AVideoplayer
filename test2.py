from moviepy.editor import *
from moviepy.video.fx.resize import resize
import pygame
import tkinter as tk
from glob import glob

pygame.display.set_mode((1280, 800))

def launch(movie):
    # root.destroy()
    print(movie)
    pygame.display.set_caption('Hello World!')
    clip = VideoFileClip(movie)
    clip.preview(fps=30,fullscreen=True)
    pygame.quit()


# launch("00.mp4")

root = tk.Tk()
root.geometry("400x300")
root.title("Double click to start")
x = tk.StringVar(value=[m for m in glob("C:/Users/Mark Renzkie/PycharmProjects/pythonProject1/*.mp4")])

ls = tk.Listbox(root, listvariable=x)
ls.pack(fill="both", expand=1)
ls.bind("<Double-Button>", lambda x: launch(ls.get(ls.curselection())))

root.mainloop()