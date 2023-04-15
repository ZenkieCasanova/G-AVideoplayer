import cv2

# Read the input image
img = cv2.imread('C:/Users/Mark Renzkie/PycharmProjects/pythonProject1/face.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def crop_boundary(top, bottom, left, right, faces):
    if faces:
        top += 10
        left += 10
        right = max(0, right - 10)
        bottom = max(0, bottom - 10)
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