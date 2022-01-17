# The following code block was run as a separate python file.

# import the opencv library
import cv2
import os


DIR_NAME2 = 'Frame_Q2'
NUM_OF_FRAMES2 = 0
# Read the video from specified path
cam = cv2.VideoCapture(0)


# Creating directory while the frames from the video will be added
if not os.path.exists(DIR_NAME2):
    os.makedirs(DIR_NAME2)

Begin = True

if not (cam.isOpened()):
    print("Could not open the webcam!")
    Begin = False
  
# frame
currentframe = 0
  
while(Begin):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        name = './' + DIR_NAME2 + '/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
        cv2.imshow('preview', frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


NUM_OF_FRAMES2 = currentframe
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()

