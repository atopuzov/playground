import cv, sys, os.path

if len(sys.argv) < 2:
    exit(0)
if not os.path.isfile(sys.argv[1]):
    exit(0)

image = cv.LoadImage(sys.argv[1]) # input image

w = image.width / 640.0
h = image.height / 480.0

print w,h
image_scale = h if h>w else w

gray = cv.CreateImage((image.width, image.height), 8, 1)
img = cv.CreateImage((cv.Round(image.width / image_scale),cv.Round (image.height / image_scale)), 8 ,1)

cv.CvtColor(image, gray, cv.CV_BGR2GRAY)
cv.Resize(gray, img, cv.CV_INTER_LINEAR)


# loading the classifiers
haarFace = cv.Load('haarcascade_frontalface_default.xml')
haarEyes = cv.Load('haarcascade_eye.xml')

storage = cv.CreateMemStorage()
detectedFace = cv.HaarDetectObjects(img, haarFace, storage)
detectedEyes = cv.HaarDetectObjects(img, haarEyes, storage)

# draw a green rectangle where the face is detected
if detectedFace:
    for face in detectedFace:
        cv.Rectangle(img,(face[0][0],face[0][1]),
                     (face[0][0]+face[0][2],face[0][1]+face[0][3]),
                     cv.RGB(155, 255, 25),2)

# draw a purple rectangle where the eye is detected
if detectedEyes:
    for face in detectedEyes:
        cv.Rectangle(img,(face[0][0],face[0][1]),
                     (face[0][0]+face[0][2],face[0][1]+face[0][3]),
                     cv.RGB(155, 55, 200),2)

cv.NamedWindow('Face Detection', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Face Detection', img) 
cv.WaitKey(0);

