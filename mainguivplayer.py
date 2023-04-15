from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
import functionsys
import random
from functionsys import ytseng, AGsearch, get_thumbnail,end1
import webbrowser
from viddownloader import download1low,download2low,download3low,download4low,download5low,download6low,download1high,download2high,download3high,download4high,download5high,download6high



def mainguivplay():
    AGsearch()
    ytseng()
    get_thumbnail()

    windowDesign = Tk()
    IconPhoto = PhotoImage(master=windowDesign, file='C:/Users/Mark Renzkie/Downloads/logosys.png')
    windowDesign.title('Gender and Age Video Player')
    windowDesign.geometry('770x720+341+257')
    windowDesign.resizable(width=False, height=False)
    windowDesign.iconphoto(False, IconPhoto)


    # CHANGE GUI COLOR FUNCTION
    if functionsys.gender == 'Male':
        bgcolor = '#63e5ff'
    if functionsys.gender == 'Female':
        bgcolor = '#FFC0CB'


    #SEARCH FUNCTION
    def get_searchdata():
        ytsearched = Entry1.get()
        functionsys.ytsearched2 = ytsearched
        windowDesign.destroy()
        from functionsys import end1
        end1()

    #OPEN FUNCTION
    def openurl1():
        webbrowser.open(ytseng.ytdatalink1)
        windowDesign.destroy()
        from functionsys import end1
        end1()

    def openurl2():
        webbrowser.open(ytseng.ytdatalink2)
        windowDesign.destroy()
        from functionsys import end1
        end1()

    def openurl3():
        webbrowser.open(ytseng.ytdatalink3)
        windowDesign.destroy()
        from functionsys import end1
        end1()

    def openurl4():

        webbrowser.open(AGsearch.ytdatalink4)
        windowDesign.destroy()
        from functionsys import end1
        end1()

    def openurl5():

        webbrowser.open(AGsearch.ytdatalink5)
        windowDesign.destroy()
        from functionsys import end1
        end1()

    def openurl6():

        webbrowser.open(AGsearch.ytdatalink6)
        windowDesign.destroy()
        from functionsys import end1
        end1()

    #DOWNLOAD FUNCTION
    def DLurl1():
        windowDesign.destroy()
        dltime = 1000
        loadingscreen(dltime)
        download1low()
        end1()

    def DLurl2():
        windowDesign.destroy()
        dltime = 1000
        loadingscreen(dltime)
        download2low()
        end1()

    def DLurl3():
        windowDesign.destroy()
        dltime = 1000
        loadingscreen(dltime)
        download3low()
        end1()

    def DLurl4():
        windowDesign.destroy()
        dltime = 1000
        loadingscreen(dltime)
        download4low()
        end1()

    def DLurl5():
        windowDesign.destroy()
        dltime = 1000
        loadingscreen(dltime)
        download5low()
        end1()

    def DLurl6():
        windowDesign.destroy()
        dltime = 1000
        loadingscreen(dltime)
        download6low()
        end1()

    def DLurl1H():
        windowDesign.destroy()
        dltime=1000
        loadingscreen(dltime)
        download1high()
        end1()

    def DLurl2H():
        windowDesign.destroy()
        dltime = 1000
        loadingscreen(dltime)
        download2high()
        end1()

    def DLurl3H():
        windowDesign.destroy()
        dltime = 1000
        loadingscreen(dltime)
        download3high()
        end1()

    def DLurl4H():
        windowDesign.destroy()
        dltime = 1000
        loadingscreen(dltime)
        download4high()
        end1()

    def DLurl5H():
        windowDesign.destroy()
        dltime = 1000
        loadingscreen(dltime)
        download5high()
        end1()

    def DLurl6H():
        windowDesign.destroy()
        dltime = 1000
        loadingscreen(dltime)
        download6high()
        end1()

    #IMAGE FACE RESIZED
    faceimg1 = Image.open('./face.jpg')
    resized_face1 = faceimg1.resize((70, 70))
    #IMAGE THUMBNAIL names

    thumbimg1 = Image.open('./thumb1.png')
    resized_thumb1 = thumbimg1.resize((150, 113))
    thumbimg2 = Image.open('./thumb2.png')
    resized_thumb2 = thumbimg2.resize((150, 113))
    thumbimg3 = Image.open('./thumb3.png')
    resized_thumb3 = thumbimg3.resize((150, 113))
    thumbimg4 = Image.open('./thumb4.png')
    resized_thumb4 = thumbimg4.resize((150, 113))
    thumbimg5 = Image.open('./thumb5.png')
    resized_thumb5 = thumbimg5.resize((150, 113))
    thumbimg6 = Image.open('./thumb6.png')
    resized_thumb6 = thumbimg6.resize((150, 113))

    selectedFont22 = font.Font(name='font_22', family='Arial', size=9, weight='bold', slant='roman', underline=0,
                               overstrike=0)
    selectedFont21 = font.Font(name='font_21', family='Arial', size=9, weight='bold', slant='roman', underline=0,
                               overstrike=0)
    selectedFont23 = font.Font(name='font_23', family='Arial', size=10, weight='normal', slant='roman', underline=0,
                               overstrike=0)
    selectedFont24 = font.Font(name='font_24', family='Arial', size=10, weight='normal', slant='roman', underline=0,
                               overstrike=0)
    selectedFont3 = font.Font(name='font_3', family='Arial', size=9, weight='normal', slant='roman', underline=0,
                              overstrike=0)
    selectedFont20 = font.Font(name='font_20', family='Arial', size=9, weight='bold', slant='roman', underline=0,
                               overstrike=0)
    selectedFont8 = font.Font(name='font_8', family='Arial', size=9, weight='bold', slant='roman', underline=0,
                              overstrike=0)
    selectedFont7 = font.Font(name='font_7', family='Arial', size=9, weight='normal', slant='roman', underline=0,
                              overstrike=0)
    selectedFont25 = font.Font(name='font_25', family='Arial', size=9, weight='bold', slant='roman', underline=0,
                               overstrike=0)
    selectedFont26 = font.Font(name='font_26', family='Arial', size=9, weight='bold', slant='roman', underline=0,
                               overstrike=0)
    selectedFont27 = font.Font(name='font_27', family='Arial', size=9, weight='bold', slant='roman', underline=0,
                               overstrike=0)
    selectedFont9 = font.Font(name='font_9', family='Arial', size=9, weight='bold', slant='roman', underline=0,
                              overstrike=0)
    selectedFont28 = font.Font(name='font_28', family='Segoe UI', size=9, weight='bold', slant='roman', underline=0,
                               overstrike=0)
    selectedFont29 = font.Font(name='font_29', family='Arial', size=10, weight='bold', slant='roman', underline=1,
                               overstrike=0)
    selectedFont31 = font.Font(name='font_31', family='Arial', size=9, weight='bold', slant='roman', underline=0,
                               overstrike=0)
    selectedFont32 = font.Font(name='font_32', family='Arial', size=9, weight='bold', slant='roman', underline=0,
                               overstrike=0)

    image_1 = ImageTk.PhotoImage(resized_face1)
    image_4 = ImageTk.PhotoImage(resized_thumb1)
    image_5 = ImageTk.PhotoImage(resized_thumb2)
    image_6 = ImageTk.PhotoImage(resized_thumb3)
    image_7 = ImageTk.PhotoImage(resized_thumb4)
    image_8 = ImageTk.PhotoImage(resized_thumb5)
    image_9 = ImageTk.PhotoImage(resized_thumb6)

    Frame1 = Frame(background='#ffffff', borderwidth=2, relief='solid', takefocus=True, )
    Frame1.place(x=-2, y=-1, height=722, width=775, anchor='nw')

    #LABELFRAMES
    LabelFrame1 = LabelFrame(background=bgcolor, font='font_22', relief='ridge', takefocus=True,
                             text='USER PROFILE', )
    LabelFrame1.place(x=7, y=5, height=163, width=238, anchor='nw')
    LabelFrame2 = LabelFrame(background=bgcolor, font='font_21', relief='ridge', takefocus=True, text='SEARCH', )
    LabelFrame2.place(x=248, y=5, height=163, width=387, anchor='nw')
    LabelFrame3 = LabelFrame(background=bgcolor, font='font_20', takefocus=True, text='RETRY FACE', )
    LabelFrame3.place(x=640, y=6, height=164, width=130, anchor='nw')
    LabelFrame4 = LabelFrame(background=bgcolor, font='font_8', takefocus=True, text='SEARCHED VIDEOS', )
    LabelFrame4.place(x=8, y=172, height=542, width=392, anchor='nw')
    LabelFrame5 = LabelFrame(background=bgcolor, font='font_9', takefocus=True, text='RECOMMENDED FOR YOU', )
    LabelFrame5.place(x=405, y=712, height=540, width=360, anchor='sw')


    Label1 = Label(font='TkDefaultFont', image=image_1, takefocus=True, text='Label1', )
    Label1.place(x=93, y=97, height=70, width=70, anchor='sw')
    Label2 = Label(background=bgcolor, font='font_23', image='', takefocus=True, text='Age: '+functionsys.age, )
    Label2.place(x=64, y=101, height=30, width=122, anchor='nw')
    Label3 = Label(background=bgcolor, font='font_24', image='', takefocus=True, text='Gender: '+functionsys.gender, )
    Label3.place(x=64, y=125, height=30, width=122, anchor='nw')
    Label4 = Label(font='TkDefaultFont', image=image_1, takefocus=True, text='Label4', )
    Label4.place(x=668, y=65, height=71, width=70, anchor='nw')
    Label5 = Label(image=image_4)
    Label5.place(x=34, y=233, height=116, width=152, anchor='nw')
    Label6 = Label(background='#ffffff', font='font_25', image='', takefocus=True,
                   text=ytseng.ytdatatitle1, )
    Label6.place(x=28, y=203, height=30, width=354, anchor='nw')
    Label7 = Label(image=image_5)
    Label7.place(x=36, y=401, height=112, width=152, anchor='nw')
    Label8 = Label(image=image_6)
    Label8.place(x=35, y=580, height=115, width=154, anchor='nw')
    Label9 = Label(background='#ffffff', font='font_26', image='', takefocus=True,
                   text=ytseng.ytdatatitle2, )
    Label9.place(x=382, y=369, height=30, width=352, anchor='ne')
    Label10 = Label(background='#ffffff', font='font_27', image='', takefocus=True,
                    text=ytseng.ytdatatitle3, )
    Label10.place(x=32, y=545, height=30, width=347, anchor='nw')
    Label11 = Label(image=image_7)
    Label11.place(x=412, y=253, height=114, width=151, anchor='nw')
    Label12 = Label(background='#ffffff', font='font_28', image='', takefocus=True, text=AGsearch.ytdatatitle4, )
    Label12.place(x=756, y=220, height=30, width=345, anchor='ne')
    Label13 = Label(background='#ffffff', font='font_29', image='', takefocus=True,
                    text='BASED FROM YOUR AGE AND GENDER', )
    Label13.place(x=756, y=190, height=30, width=345, anchor='ne')
    Label14 = Label(background='#ffffff', font='font_31', image='', takefocus=True, text=AGsearch.ytdatatitle5, )
    Label14.place(x=755, y=382, height=30, width=345, anchor='ne')
    Label15 = Label(image=image_8)
    Label15.place(x=413, y=418, height=110, width=152, anchor='nw')
    Label16 = Label(background='#ffffff', font='font_32', image='', takefocus=True, text=AGsearch.ytdatatitle6, )
    Label16.place(x=414, y=546, height=30, width=342, anchor='nw')
    Label17 = Label(image=image_9)
    Label17.place(x=413, y=578, height=121, width=154, anchor='nw')

    Message1 = Message(aspect=1000, background=bgcolor, font='font_7', takefocus=True, text='CURRENT FACE', )
    Message1.place(x=646, y=137, height=30, width=115, anchor='nw')

    Entry1 = Entry(exportselection=True, font='TkDefaultFont', takefocus=True, )
    Entry1.place(x=302, y=68, height=19, width=293, anchor='nw')

    Button1 = Button(font='font_3', image='', relief='raised', takefocus=True, text='SEARCH', command=get_searchdata)
    Button1.place(x=406, y=109, height=30, width=70, anchor='nw')
    Button2 = Button(background='#ff0000', font='TkDefaultFont', image='', takefocus=True, text='CONFIRM', )
    Button2.place(x=672, y=30, height=26, width=59, anchor='nw')
    #video1 buttons
    Button3 = Button(font='TkDefaultFont', image='', takefocus=True, text='OPEN', command = openurl1)
    Button3.place(x=243, y=237, height=30, width=70, anchor='nw')
    Button4 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - LOW Q.', command = DLurl1)
    Button4.place(x=216, y=273, height=30, width=133, anchor='nw')
    Button5 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - HIGH Q.', command = DLurl1H)
    Button5.place(x=216, y=311, height=30, width=133, anchor='nw')
    #video2 buttons
    Button6 = Button(font='TkDefaultFont', image='', takefocus=True, text='OPEN',command = openurl2)
    Button6.place(x=248, y=402, height=30, width=70, anchor='nw')
    Button7 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - LOW Q.', command = DLurl2)
    Button7.place(x=219, y=440, height=30, width=130, anchor='nw')
    Button8 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - HIGH Q.', command = DLurl2H)
    Button8.place(x=219, y=478, height=30, width=130, anchor='nw')
    #video3 buttons
    Button9 = Button(font='TkDefaultFont', image='', takefocus=True, text='OPEN', command = openurl3)
    Button9.place(x=246, y=580, height=30, width=70, anchor='nw')
    Button10 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - LOW Q.', command = DLurl3)
    Button10.place(x=220, y=620, height=30, width=127, anchor='nw')
    Button11 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - HIGH Q.', command = DLurl3H)
    Button11.place(x=219, y=660, height=30, width=128, anchor='nw')
    #video4 buttons
    Button12 = Button(font='TkDefaultFont', image='', takefocus=True, text='OPEN', command = openurl4)
    Button12.place(x=622, y=254, height=30, width=70, anchor='nw')
    Button13 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - LOW Q.', command = DLurl4)
    Button13.place(x=593, y=294, height=30, width=124, anchor='nw')
    Button14 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - HIGH Q.', command = DLurl4H)
    Button14.place(x=717, y=334, height=30, width=124, anchor='ne')
    #video 5 buttons
    Button15 = Button(font='TkDefaultFont', image='', takefocus=True, text='OPEN', command = openurl5)
    Button15.place(x=620, y=419, height=30, width=70, anchor='nw')
    Button16 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - LOW Q.', command = DLurl5)
    Button16.place(x=716, y=458, height=30, width=123, anchor='ne')
    Button17 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - HIGH Q.', command = DLurl5H)
    Button17.place(x=716, y=497, height=30, width=124, anchor='ne')
    # video 6 buttons
    Button18 = Button(font='TkDefaultFont', image='', takefocus=True, text='OPEN', command = openurl6)
    Button18.place(x=623, y=584, height=30, width=70, anchor='nw')
    Button19 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - LOW Q.', command = DLurl6)
    Button19.place(x=716, y=624, height=30, width=125, anchor='ne')
    Button20 = Button(font='TkDefaultFont', image='', takefocus=True, text='DOWNLOAD - HIGH Q.', command = DLurl6H)
    Button20.place(x=591, y=662, height=30, width=125, anchor='nw')
    windowDesign.mainloop()


def loadingscreen(dltime):
    windowDesign2 = Tk()
    IconPhoto = PhotoImage(master=windowDesign2, file='C:/Users/Mark Renzkie/Downloads/logosysico.png')
    windowDesign2.title('Gender and Age Video Player')
    windowDesign2.geometry('600x465+341+257')
    windowDesign2.resizable(width=False, height=False)
    windowDesign2.iconphoto(False, IconPhoto)

    if functionsys.gender == 'Male':
        bgcolor = '#63e5ff'
    if functionsys.gender == 'Female':
        bgcolor = '#FFC0CB'

    dltitle = ["Loading...", "Processing...", "Getting Data...", "Downloading..."]
    dltitle = random.choice(dltitle)

    selectedFont3 = font.Font(name='font_3', family='Terminal', size=18, weight='bold', slant='roman', underline=0,
                              overstrike=0)
    selectedFont4 = font.Font(name='font_4', family='Terminal', size=18, weight='bold', slant='roman', underline=0,
                              overstrike=0)
    Image7 = PhotoImage(name='image_7', file='C:/Users/Mark Renzkie/Downloads/logosysico.png')
    Frame1 = Frame(background=bgcolor, borderwidth=2, relief='solid', takefocus=True, )
    Frame1.place(x=0, y=1, height=464, width=599, anchor='nw')
    Label1 = Label(font='TkDefaultFont', image='image_7', takefocus=True, text='Label1', )
    Label1.place(x=196, y=82, height=194, width=202, anchor='nw')
    Label2 = Label(background=bgcolor, font='font_3', image='', takefocus=True, text=dltitle, )
    Label2.place(x=155, y=302, height=30, width=295, anchor='nw')
    Label3 = Label(background=bgcolor, font='font_4', image='', takefocus=True, text='PLEASE WAIT', )
    Label3.place(x=191, y=348, height=30, width=206, anchor='nw')
    windowDesign2.after(dltime, windowDesign2.destroy)
    windowDesign2.mainloop()


if __name__ == '__main__':
    windowDesign.destroy()
    mainguivplay()
    get_searchdata()
    windowDesign.destroy()


