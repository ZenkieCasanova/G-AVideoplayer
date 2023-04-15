from tkinter import *
from tkinter import font,filedialog
import cv2
import os

def window1():

    windowDesign = Tk()
    IconPhoto = PhotoImage(master=windowDesign, file='C:/Users/Mark Renzkie/Downloads/logosysico.png')
    windowDesign.title('Gender and Age Video Player')
    windowDesign.geometry('768x550+341+257')
    windowDesign.resizable(width=True, height=True)
    windowDesign.iconphoto(False, IconPhoto)

    def cam1():
        windowDesign.destroy()
        from camcapture import App
        App()

    def importer():
        from camcapture import cropping
        open_file()
        cropping()
        windowDesign.destroy()
        from classifier import classify1
        from confirmation import window3
        classify1()
        window3()
    def open_file():
        file = filedialog.askopenfile(mode='r', filetypes=[('Image File', '*.jpg')])
        if file:
            filepath = os.path.abspath(file.name)
            print("The File is located at : " + str(filepath))
            img = cv2.imread(str(filepath))
            path = r'C:\Users\Mark Renzkie\PycharmProjects\pythonProject5'
            cv2.imwrite(os.path.join(path, 'face.jpg'), img)

    selectedFont9 = font.Font(name='font_9', family='8514oem', size=13, weight='bold', slant='roman', underline=0,
                              overstrike=0)
    selectedFont5 = font.Font(name='font_5', family='8514oem', size=27, weight='bold', slant='roman', underline=0,
                              overstrike=0)
    selectedFont8 = font.Font(name='font_8', family='8514oem', size=13, weight='bold', slant='roman', underline=0,
                              overstrike=0)
    Image2 = PhotoImage(name='image_2', file='C:/Users/Mark Renzkie/Downloads/logosysico.png')

    Frame1 = Frame(background='#400040', borderwidth=2, relief='solid', takefocus=True, )
    Frame1.place(x=0, y=-4, height=554, width=768, anchor='nw')
    Label1 = Label(background='#400040', font='TkDefaultFont', image='image_2', takefocus=True, text='Label1', )
    Label1.place(x=260, y=10, height=293, width=223, anchor='nw')
    Label2 = Label(activebackground='#000040', background='#400040', font='font_5', foreground='#c3063c', image='',
                   takefocus=True, text='Gender and Age Video Player', )
    Label2.place(x=104, y=282, height=41, width=574, anchor='nw')
    Button1 = Button(background='#0000a0', font='font_9', foreground='#ff0000', image='', takefocus=True, command=cam1,
                     text='START', )
    Button1.place(x=339, y=373, height=30, width=70, anchor='nw')
    Button2 = Button(background='#0000a0', font='font_8', foreground='#ff0000', image='', takefocus=True, command= importer,
                     text='IMPORT', )
    Button2.place(x=339, y=421, height=30, width=70, anchor='nw')

    windowDesign.mainloop()


if __name__ == '__main__':
    window1()
