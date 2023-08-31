import cv2 as cv

video = cv.VideoCapture('people.mp4')

"""
createBackgroundSubtractorMOG2: https://www.geeksforgeeks.org/background-subtraction-opencv/
Background subtraction is a way of eliminating the background from image. 
To achieve this we extract the moving foreground from the static background.
"""

substractor = cv.createBackgroundSubtractorMOG2(200, 300)

# Process the video by each iteration
# get a return value and a frame.
while True:

    # return valule / current frame of the video
    ret, frame = video.read()

    # Process the video if exist (if a return value was given)
    if ret:
        mask = substractor.apply(frame)
        cv.imshow('Mask', mask) # ?

        # Cierra el programa (Mask)
        # https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7
        if cv.waitKey(5) == ord('X'):
            break

    # Repeat the video if it ended    
    else:
        video = cv.VideoCapture('people.mp4')


cv.destroyAllWindows()
video.release()