# Import module and packages
import keyPressModule as kp
from djitellopy import tello
import time
import cv2 as cv

# Initialize the drone
kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())
global img

# Image capture
drone.streamon()

# Key controls input


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    # Left key
    if kp.getKey('LEFT'):
        lr = -speed
    # Right key
    elif kp.getKey('RIGHT'):
        lr = speed

    # Forward key
    if kp.getKey('UP'):
        fb = speed
    # Backward key
    elif kp.getKey('DOWN'):
        fb = -speed

    # Up key
    if kp.getKey('w'):
        ud = speed
    # Down key
    elif kp.getKey('s'):
        ud = -speed

     # Rotate left
    if kp.getKey('a'):
        yv = -speed
    # Rotate right
    elif kp.getKey('d'):
        yv = speed

    # Takeoff key
    if kp.getKey('e'):
        drone.takeoff()

    # Landing key
    if kp.getKey('q'):
        drone.land()
        time.sleep(3)

    # Take pic key
    if kp.getKey("z"):
        cv.imwrite(
            f'Project 1 - Surveillance\Resources\Images{time.time()}.jpg', img)

        time.sleep(0.3)

    return [lr, fb, ud, yv]


# Drone movement
while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = drone.get_frame_read().frame
    img = cv.resize(img, (360, 240))
    cv.imshow('Image', img)
    cv.waitKey(1)
