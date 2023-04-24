import cv2

img=cv2.imread("solar-system.jpg")

cv2.putText(img,"sun",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,250))
cv2.putText(img,"mercury",(100,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,250,250))
cv2.putText(img,"venus",(195,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,250,250))
cv2.putText(img,"earth",(290,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,250,250))
cv2.putText(img,"moon",(310,160),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,250,250))
cv2.putText(img,"marse",(380,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,250,250))
cv2.putText(img,"jupiter",(580,40),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,250,250))
cv2.putText(img,"saturn",(780,120),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,250,250))
cv2.putText(img,"uranus",(970,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,250,250))
cv2.putText(img,"neptune",(1120,145),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,250,250))

cv2.imwrite("solar system.jpg",img)
cv2.imshow("output",img)
cv2.waitKey(0)