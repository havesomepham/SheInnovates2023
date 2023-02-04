# import the opencv library
import cv2
import numpy as np

# define a video capture object
vid = cv2.VideoCapture(1)

height = 1080
width = 1920
while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    
    # this doesn't work as it should
    # b = frame[:, :, :1]
    # g = frame[:, :, 1:2]
    # r = frame[:, :, 2:]
  
    # b_mean = np.mean(b)
    # g_mean = np.mean(g)
    # r_mean = np.mean(r)
    
    r_mean = frame[int(height/2)][int(width/2)][0]
    g_mean = frame[int(height/2)][int(width/2)][1]
    b_mean = frame[int(height/2)][int(width/2)][2]
    
    pixel = np.array([r_mean, g_mean, b_mean])

    frame[:] = pixel

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
