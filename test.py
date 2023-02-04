# import the opencv library
import cv2
import numpy as np  
  
# define a video capture object
vid = cv2.VideoCapture(1)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    frame = cv2.flip(frame, 1) 
    
    height = len(frame)
    width = len(frame[0])
      
    # b = frame[:, :, :1]
    # g = frame[:, :, 1:2]
    # r = frame[:, :, 2:]
  
    # computing the mean
    r_mean = frame[int(height/2)][int(width/2)][0]
    g_mean = frame[int(height/2)][int(width/2)][1]
    b_mean = frame[int(height/2)][int(width/2)][2]
  
    # print(round(r_mean), round(g_mean), round(b_mean))
    for row in frame:
        for pixel in row:
            pixel[0] = r_mean
            pixel[1] = g_mean
            pixel[2] = b_mean
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