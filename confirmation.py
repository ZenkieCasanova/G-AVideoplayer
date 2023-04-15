from tkinter import *
from tkinter import font
import classifier
from PIL import Image,ImageTk

import start


def window3():

    windowDesign = Tk()
    IconPhoto = PhotoImage(master = windowDesign, file = 'C:/Users/Mark Renzkie/Downloads/logosys.png')
    windowDesign.title('Design Window')
    windowDesign.geometry('768x550+341+257')
    windowDesign.resizable(width = False, height = False)
    windowDesign.iconphoto(False, IconPhoto)

    def goback():
        windowDesign.destroy()
        start.window1()

    selectedFont1 = font.Font(name = 'font_1', family='8514oem', size = 12, weight = 'bold', slant = 'roman', underline = 0, overstrike = 0)
    Frame1 = Frame(background = '#ffffff', borderwidth = 2, highlightbackground = '#400040', highlightcolor = '#ffffff', relief = 'solid', takefocus = True, )
    Frame1.place(x = 0, y = 0, height = 548, width = 765, anchor = 'nw')

    faceimg = Image.open('C:/Users/Mark Renzkie/PycharmProjects/pythonProject5/face.jpg')
    resized_image = faceimg.resize((200, 200))
    Img = ImageTk.PhotoImage(resized_image)

    Button1 = Button(background = '#00ff80', font = 'TkDefaultFont', image = '', takefocus = True, text = 'YES', )
    Button1.place(x = 344, y = 379, height = 30, width = 70, anchor = 'nw')
    Button2 = Button(background = '#ff0000', font = 'TkDefaultFont', image = '', takefocus = True, text = 'NO',command=goback )
    Button2.place(x = 344, y = 423, height = 30, width = 70, anchor = 'nw')
    Label1 = Label(background = '#ffffff', font = 'font_1', image = '', takefocus = True, text = 'CLASSIFIED AS: '+ age + ' yrs old ' + gender, )
    Label1.place(x = 244, y = 84, height = 30, width = 391, anchor = 'nw')
    Label2 = Label(image=Img)
    Label2.place(x=384, y=234, height=210, width=210, anchor='center')

    windowDesign.mainloop()

if __name__ == '__main__':
    window3()