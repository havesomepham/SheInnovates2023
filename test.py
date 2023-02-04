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

    # mean calculation version A (total mean)
    # r = frame[:, :, :1]
    # g = frame[:, :, 1:2]
    # b = frame[:, :, 2:]

    # r_mean = np.mean(r)
    # g_mean = np.mean(g)
    # b_mean = np.mean(b)

    # mean calculation version B (single-pixel)
    # r_mean = frame[int(height/2)][int(width/2)][0]
    # g_mean = frame[int(height/2)][int(width/2)][1]
    # b_mean = frame[int(height/2)][int(width/2)][2]

    # mean calculation version C (small-area)
    ymin = int(height/2 - 20)
    ymax = int(height/2 + 20)
    xmin = int(width/2 - 20)
    xmax = int(width/2 + 20)
    r = frame[ymin:ymax, xmin:xmax, 0]
    g = frame[ymin:ymax, xmin:xmax, 1]
    b = frame[ymin:ymax, xmin:xmax, 2]

    r_mean = np.mean(r)
    g_mean = np.mean(g)
    b_mean = np.mean(b)
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
