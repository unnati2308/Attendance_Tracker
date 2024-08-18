import cv2
import numpy as np
import face_recognition

imgObama= face_recognition.load_image_file('images/obama.jpg')
imgObama=cv2.cvtColor(imgObama,cv2.COLOR_BGR2RGB)
imgTest=face_recognition.load_image_file('images/obamaTest.jpg')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc= face_recognition.face_locations(imgObama)[0]
encodeObama= face_recognition.face_encodings(imgObama)[0]
cv2.rectangle(imgObama,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(225,0,225),2)

faceLocTest= face_recognition.face_locations(imgTest)[0]
encodeTest= face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(225,0,225),2)


results=face_recognition.compare_faces([encodeObama],encodeTest)
faceDis=face_recognition.face_distance([encodeObama],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow('obama',imgObama)
cv2.imshow('obama test',imgTest)
cv2.waitKey(0)
