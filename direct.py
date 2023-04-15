from tkinter import *
from tkinter import font

windowDesign = Tk()

windowDesign.title('Design Window')
windowDesign.geometry('768x550+341+257')


selectedFont1 = font.Font(name = 'font_1', family = 'Lucida Sans', size = 12, weight = 'bold', slant = 'roman', underline = 1, overstrike = 0)
selectedFont2 = font.Font(name = 'font_2', family = 'Lucida Sans', size = 11, weight = 'bold', slant = 'roman', underline = 0, overstrike = 0)
Button1 = Button(font = 'font_2', image = '', takefocus = True, text = 'ENTER', )
Button1.place(x = 351, y = 360, height = 30, width = 70, anchor = 'nw')
Entry1 = Entry(exportselection = True, font = 'TkDefaultFont', takefocus = True, )
Entry1.place(x = 226, y = 229, height = 20, width = 364, anchor = 'nw')
Label1 = Label(font = 'TkDefaultFont', highlightthickness = 1, image = '', takefocus = True, text = 'File Location:', )
Label1.place(x = 154, y = 224, height = 30, width = 70, anchor = 'nw')
Label2 = Label(font = 'font_1', image = '', takefocus = True, text = 'Enter the Directory of the Program', )
Label2.place(x = 243, y = 113, height = 30, width = 299, anchor = 'nw')
Label3 = Label(font = 'TkDefaultFont', image = '', takefocus = True, text = 'Ex. C:\\Users\\UserXY\\OneDrive\\Desktop', )
Label3.place(x = 272, y = 255, height = 30, width = 257, anchor = 'nw')

windowDesign.mainloop()
