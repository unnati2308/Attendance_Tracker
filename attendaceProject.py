import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'images'
Images = []
classNames = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    Images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
    print(classNames)

def findEncodings(Images):
    encodeList = []
    for img in Images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('attendance.csv','r+') as f:
        myDataList=f.readlines()
        nameList= []
        for line in myDataList:
            entry=line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString= now.strftime('%H:%M:%S')
            DString= now.strftime('%m/%d/%Y')
            f.writelines(f'\n{name},{dtString},{DString}')
encodeListKnown = findEncodings(Images)
print('encoding complete')

cap = cv2.VideoCapture(0)

while True:
       success, img = cap.read()
       imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
       imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

       facesCurFrame = face_recognition.face_locations(imgS)
       encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

       for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):

           matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
           faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
           print(faceDis)
           matchIndex= np.argmin(faceDis)

           if matches[matchIndex]:
               name= classNames[matchIndex].upper()
               print(name)
               y1,x2,x1,y2=faceLoc
               y1, x2, x1, y2=y1*4,x2*4,x1*4,y2*4
               cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
               cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
               cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
               markAttendance(name)

       cv2.imshow('webcam',img)
       cv2.waitKey(1)


# faceLoc= face_recognition.face_locations(imgObama)[0]
# encodeObama= face_recognition.face_encodings(imgObama)[0]
# cv2.rectangle(imgObama,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(225,0,225),2)
# faceLocTest= face_recognition.face_locations(imgTest)[0]
# encodeTest= face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(225,0,225),2)
# results=face_recognition.compare_faces([encodeObama],encodeTest)
# faceDis=face_recognition.face_distance([encodeObama],encodeTest)
