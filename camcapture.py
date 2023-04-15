# -*- coding: utf-8 -*-
from tkinter import *
import cv2
import os
import sys
from PIL import Image, ImageTk
import time


class App:
    def __init__(self, video_source=0):
        self.appName = "Gender and Age Video Player Capture"
        self.window = Tk()
        self.window.title(self.appName)
        self.window.resizable(0, 0)
        self.video_source = video_source

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = Canvas(self.window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        # Button that lets the user take a snapshot
        def kill2():
            self.snapshot()
            self.update()
            cropping()
            self.window.destroy()
            from classifier import classify1
            from confirmation import window3
            self.app = classify1()
            self.app = window3()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()
        self.btn_snapshot = Button(self.window, text="CAPTURE!", width=50,
                                   command=lambda: [self.snapshot, kill2()])

        self.btn_snapshot.pack(anchor=CENTER, expand=True)

        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("face.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


def cropping():
    img = cv2.imread('C:/Users/Mark Renzkie/PycharmProjects/pythonProject5/face.jpg')

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def crop_boundary(top, bottom, left, right, faces):
        if faces:
            top += 7
            left += 7
            right += 7
            bottom += 7
        else:
            top = max(0, top - 50)
            left = max(0, left - 50)
            right += 50
            bottom += 50

        return (top, bottom, left, right)

    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        top, bottom, left, right = crop_boundary(y, y + h, x, x + w, 2)
        faces = img[top: bottom, left: right]
        cv2.imwrite('face.jpg', faces)

    # Display the output
    cv2.imwrite('detected.jpg', img)
    cv2.waitKey()


if __name__ == "__main__":
    App()


