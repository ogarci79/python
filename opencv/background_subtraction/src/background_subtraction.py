#!/usr/bin/env python

import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt
from scipy import linalg 

def main():
    cap = cv2.VideoCapture('vtest.avi')
    fgbg = cv2.BackgroundSubtractorMOG()

    while(1) :
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        #cv2.imshow('frame',frame)
        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27 :
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
