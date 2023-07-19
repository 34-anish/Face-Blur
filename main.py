# import the opencv library
import cv2
from cvzone.FaceDetectionModule import FaceDetector

# define a video capture object
vid = cv2.VideoCapture(0)
# vid.set(3,640)
# vid.set(3,480)
detector =FaceDetector(minDetectionCon=0.75)

while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()
	frame,bboxs=detector.findFaces(frame,draw= True)
	if bboxs:
        
		for i ,bbox in enumerate(bboxs):
			x,y,w,h = bbox['bbox']
			imgCrop = frame[y:y+h,x:x+w]
						# ksize
			ksize = (30, 30)
			
			# Using cv2.blur() method 
			imgCrop= cv2.blur(imgCrop, ksize, cv2.BORDER_DEFAULT) 
			frame[y:y+h,x:x+w] = imgCrop
			# cv2.imshow(f'Img cropped{i}',imgCrop)

	# Display the resulting frame
	cv2.imshow('frame', frame)
	
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
