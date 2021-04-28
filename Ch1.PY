# OpenCV Tutorials Begin Here
# Getting started with images
# In this tutorial we will learn how to:
# Read an image from file.
# Display an image in an OpenCV window.
# Write an image to a file.

# We begin with importing required modules
import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("resources/phoenix.png"))

if img is None:
    sys.exit("Could not find image.")

cv.imshow("Output", img)
k = cv.waitKey(0)

if k == ord("x"):
    cv.imwrite("resources/AAA.jpeg", img)
