# The following code is used to watch a video stream, detect Aruco markers, and use
# a set of markers to determine the posture of the camera in relation to the plane
# of markers.
#
# Assumes that all markers are on the same plane, for example on the same piece of paper
#
# Requires camera calibration (see the rest of the project for example calibration)

import numpy
import cv2
import cv2.aruco as aruco
import os
import pickle
import math
import time

# Check for camera calibration data
if not os.path.exists('./calibration.pckl'):
    print("You need to calibrate the camera you'll be using. See calibration project directory for details.")
    exit()
else:
    f = open('calibration.pckl', 'rb')
    (cameraMatrix, distCoeffs) = pickle.load(f)
    f.close()
    if cameraMatrix is None or distCoeffs is None:
        print("Calibration issue. Remove ./calibration.pckl and recalibrate your camera with CalibrateCamera.py.")
        exit()

# Constant parameters used in Aruco methods
ARUCO_PARAMETERS = aruco.DetectorParameters_create()
ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_5X5_250)

# Create grid board object we're using in our stream
board = aruco.GridBoard_create(
        markersX=5,
        markersY=7,
        markerLength=0.09,
        markerSeparation=0.01,
        dictionary=ARUCO_DICT)

# Create vectors we'll be using for rotations and translations for postures
rvecs, tvecs = None, None

cam = cv2.VideoCapture('aruco_calib.mp4')
# cam = cv2.VideoCapture(0, cv2.CAP_ANY)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,720)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
while(cam.isOpened()):
    start_time = time.time()
    # Capturing each frame of our video stream
    ret, QueryImg = cam.read()
    if ret == True:
        # grayscale image
        gray = cv2.cvtColor(QueryImg, cv2.COLOR_BGR2GRAY)

        # Detect Aruco markers
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, ARUCO_DICT, parameters=ARUCO_PARAMETERS)
        # Refine detected markers
        # Eliminates markers not part of our board, adds missing markers to the board
        corners, ids, rejectedImgPoints, recoveredIds = aruco.refineDetectedMarkers(
                image = gray,
                board = board,
                detectedCorners = corners,
                detectedIds = ids,
                rejectedCorners = rejectedImgPoints,
                cameraMatrix = cameraMatrix,
                distCoeffs = distCoeffs)

        ###########################################################################
        # TODO: Add validation here to reject IDs/corners not part of a gridboard #
        ###########################################################################

        # Outline all of the markers detected in our image
        QueryImg = aruco.drawDetectedMarkers(QueryImg, corners, borderColor=(255, 0, 0))

        # Require 15 markers before drawing axis
        if ids is not None and len(ids) > 0:
            # Estimate the posture of the gridboard, which is a construction of 3D space based on the 2D video
            #pose, rvec, tvec = aruco.estimatePoseBoard(corners, ids, board, cameraMatrix, distCoeffs)
            #if pose:
            #    # Draw the camera posture calculated from the gridboard
            #    QueryImg = aruco.drawAxis(QueryImg, cameraMatrix, distCoeffs, rvec, tvec, 0.3)
            # Estimate the posture per each Aruco marker
            (rvecs,tvecs, _) = aruco.estimatePoseSingleMarkers(corners, 1, cameraMatrix, distCoeffs)
            for rvec, tvec in zip(rvecs, tvecs):
                QueryImg = aruco.drawAxis(QueryImg, cameraMatrix, distCoeffs, rvec, tvec, 2)
                QueryImg = aruco.drawDetectedMarkers(QueryImg, corners, ids)
                strPosition = "MARKER Position  X: %4.0f   Y: %4.0f   Z: %4.0f"%(tvec[0][0], tvec[0][1], tvec[0][2])
                print(ids)
                cv2.putText(QueryImg, strPosition, (100,100), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2, cv2.LINE_AA)
        # Display our image
        cv2.putText(QueryImg, f'FPS: {math.floor(1.0 / (time.time() - start_time))}', (8, 16), cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

        cv2.imshow('QueryImage', QueryImg)

    # Exit at the end of the video on the 'q' keypress
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

cv2.destroyAllWindows()
