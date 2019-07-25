from djitellopy import Tello

import numpy as np
import cv2
import time

def run():
    tello = Tello()
    counter = 0

    if not tello.connect():
        print("Tello not connected")
        return
    # In case streaming is on. This happens when we quit this program without the escape key.
    if not tello.streamoff():
        print("Could not stop video stream")
        return
    if not tello.streamon():
        print("Could not start video stream")
        return
    frame_read = tello.get_frame_read()

    while(True):
        # Our operations on the frame come here
        frame = frame_read.frame
        time.sleep(10)

        cv2.imwrite('frame-{}.png'.format(counter), frame_read.frame)
        counter += 1
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

run()
