import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('img.jpg',1)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img,1.5, 7)
print(faces)

for (x,y,w,h) in faces:
    print(x,y,w,h)
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),5)
    #roi_color = img[y:y+h, x:x+w] 

resized = cv2.resize(img, (500,500))     


cv2.imshow('img',img)
cv2.imshow('img', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
